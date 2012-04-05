import urllib
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/<user>/<repo>")
def index_with_url(user, repo):
    return jsonify({
        "user": user,
        "repo": repo,
        "license": "",
        })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

