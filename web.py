from flask import Flask, jsonify, abort
import os
import requests
import json
import re

repo_url = "https://api.github.com/repos/{}/{}"
branch_url = "https://api.github.com/repos/{}/{}/branches"
tree_url = "https://api.github.com/repos/{}/{}/git/trees/{}"
blob_url = "https://api.github.com/repos/{}/{}/git/blobs/{}"

LICENSES = [
    {
        'name': 'MIT license (MIT)',
        'text': open("licenses/mit.txt").read(),
    },
    {
        'name': 'ISC License (ISC)',
        'text': open("licenses/isc.txt").read(),
    },
    {
        'name': 'Apache License 2.0 (Apache-2.0)',
        'text': open("licenses/apache-2.0.txt").read(),
    },
    {
        'name': 'GNU General Public License, version 3 (GPL-3.0)',
        'text': open("licenses/gpl-3.0.txt").read(),
    },
    {
        'name': 'GNU AFFERO GENERAL PUBLIC LICENSE, Version 3 (AGPL-3.0)',
        'text': open("licenses/agpl-3.0.txt").read(),
    },
    {
        'name': 'BSD License',
        'text': open("licenses/bsd.txt").read(),
    },
]
    

def get_branch(repo, branches):
    for branch in branches:
        if branch['name'] == repo.get('master_branch', 'master'):
            return branch
    raise KeyError("No branch found")


def find_license_file(tree):
    for blob in tree['tree']:
        if blob['path'].startswith("LICENSE"):
            return blob
    raise KeyError("No LICENSE file found")


def license_type(blob):
    blob = re.sub(r"\s", "", blob)
    print blob
    for license in LICENSES:
        print re.sub(r"\s", "", license['text'])
        if re.sub(r"\s", "", license['text']) in blob:
            return license['name']
    return "Unknown License"


def get(*args, **kwargs):
    resp = requests.get(*args, **kwargs)
    data = json.loads(resp.text)

    if not resp.ok:
        raise ValueError("Github API Error: {}".format(data['message']))

    return data


def get_license(user, repo_name):
    repo = get(repo_url.format(user, repo_name))
    branches = get(repo['url'] + "/branches")
    branch = get_branch(repo, branches)
    tree = get(tree_url.format(user, repo_name, branch['commit']['sha']))
    license = find_license_file(tree)

    resp = requests.get(license['url'],
                        headers={'Accept': 'application/vnd.github.v3.raw'})

    return license_type(resp.text)


app = Flask(__name__)

@app.route("/<user>/<repo>")
def index_with_url(user, repo):
    try:
        license_type = get_license(user, repo)
    except (KeyError, ValueError) as e:
        resp = jsonify(message=unicode(e))
        resp.status_code = 400
        return resp
 
    return jsonify({
        'user': user,
        'repo': repo,
        'license': license_type,
        })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

