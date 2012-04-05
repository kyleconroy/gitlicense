import urllib
import os
import github
from flask import Flask, jsonify, abort

app = Flask(__name__)

@app.route("/<user>/<repo>")
def index_with_url(user, repo):
    try:
        license_type = github.get_license(user, repo)
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

