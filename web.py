from flask import Flask, jsonify, abort, make_response
import os
import requests
import json
import re

repo_url = "https://api.github.com/repos/{}/{}"
branch_url = "https://api.github.com/repos/{}/{}/branches"
tree_url = "https://api.github.com/repos/{}/{}/git/trees/{}"
blob_url = "https://api.github.com/repos/{}/{}/git/blobs/{}"


def clean(blob, remove_numbers=True):
    if remove_numbers:
        return re.sub(r"\s|\*|\"|[0-9]\.|'", "", blob).lower()
    else:
        return re.sub(r"\s|\*|\"|\.|'", "", blob).lower()


LICENSES = [
    {
        'name': 'MIT License',
        'shorthand': 'MIT License',
        'text': clean(open("licenses/mitlite.txt").read()),
    },
    {
        'name': 'MIT License',
        'shorthand': 'MIT License',
        'text': clean(open("licenses/mit.txt").read()),
    },
    {
        'name': 'ISC License',
        'shorthand': 'ISC License',
        'text': clean(open("licenses/isc.txt").read()),
    },
    {
        'name': 'Apache License 2.0',
        'shorthand': 'Apache-2.0',
        'text': clean(open("licenses/apache-2.0.txt").read()),
    },
    {
        'name': 'GNU General Public License Version 2',
        'shorthand': 'GPL-2.0',
        'text': clean(open("licenses/gpl-2.0.txt").read()),
    },
    {
        'name': 'Modified BSD License',
        'shorthand': 'Modified BSD',
        'texts': clean(open("licenses/modbsd.txt").read()).split("<split>"),
    },
    {
        'name': 'GNU Affero General Public License Version 3',
        'shorthand': 'AGPL-3.0',
        'text': clean(open("licenses/agpl-3.0.txt").read()),
    },
    {
        'name': 'GNU General Public License Version 3',
        'shorthand': 'GPL-3.0',
        'text': clean(open("licenses/gpl-3.0.txt").read()),
    },
    {
        'name': 'BSD-2 License',
        'shorthand': 'BSD License',
        'text': clean(open("licenses/bsd.txt").read()),
    },
    {
        'name': 'Mozilla Public License',
        'shorthand': 'MPL License',
        'text': clean(open("licenses/mpl.txt").read()),
    },
    {
        'name': 'Artistic License Version 2.0',
        'shorthand': 'Artistic-2.0',
        'text': clean(open("licenses/art-2.0.txt").read()),
        'url': 'http://www.opensource.org/licenses/Artistic-2.0',
    }
]

def is_license(path):
    return ("copying" in path.lower() or
            "license" in path.lower() or
            "readme" in path.lower())

def get_branch(repo, branches):
    for branch in branches:
        if branch['name'] == repo.get('master_branch', 'master'):
            return branch
    raise KeyError("No branch found")


def find_license_file(tree):
    for blob in tree['tree']:
        if is_license(blob['path']):
            yield blob

def find_license_by_name(tree):
    for blob in tree['tree']:
        for license in LICENSES:
            if license['shorthand'] in blob['path']:
                return license['name']


def find_file(tree, filename):
    for blob in tree['tree']:
        if filename in blob['path'].lower():
            return blob


def license_type(blob):
    blob = clean(blob.replace("GNU Library General Public License",
                              "GNU Lesser General Public License"))
    for license in LICENSES:
        try:
            if license['text'] in blob:
                return license['name']
        except:
            if all(text in blob for text in license['texts']):
                return license['name']
    return "Unknown License"


def license_mention(blob):
    blob = clean(blob, remove_numbers=False)
    for license in LICENSES:
        if clean(license['name'], remove_numbers=False) in blob:
            return license['name']


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

    for license in find_license_file(tree):
        resp = requests.get(license['url'],
                            headers={'Accept': 'application/vnd.github.v3.raw'})
        ltype = license_type(resp.text)
        if ltype != 'Unknown License':
            return ltype

    specific_name = find_license_by_name(tree)

    if specific_name:
        return specific_name

    for filename in ["readme", "package.yml"]:
        blob = find_file(tree, filename)

        if not blob:
            continue

        resp = requests.get(blob['url'],
                            headers={'Accept': 'application/vnd.github.v3.raw'})
        license = license_mention(resp.text)

        if license:
            return license

    return "No License Found"


app = Flask(__name__)

@app.route("/")
def index():
    index = """
<!DOCTYPE html>
<html>
    <body>
    <pre>
# GitLicense

REST API for discovering the license for a github repository.

## Usage

    curl -i http://gitlicense.herokuapp.com/:user/:repo

The return value will be a JSON object of the following form.

    {
        repo: ":user",
        user: ":repo",
        license: "MIT License"
    }
    </pre>
    </body>
</html>"""
    return make_response(index)

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

