# GitLicense

REST API for discovering the license for a github repository.

## Usage

    curl -i http://gitlicense.herokuapp.com/{user}/{repo}

The return value will be a JSON object of the following form.

    {
        repo: ":user",
        user: ":repo",
        license: "MIT License"
    }

### Supported Licenses

* MIT license (MIT)
* ISC License (ISC)
* Apache License 2.0 (Apache-2.0)
* GNU General Public License, version 2 (GPL-2.0)
* GNU General Public License, version 3 (GPL-3.0)
* GNU AFFERO GENERAL PUBLIC LICENSE, Version 3 (AGPL-3.0)
* BSD License
* Modified BSD License
* Artisitic License 2.0
* Mozilla Public License
* Python Software Foundation License Version 2

## TODO

* Improve the license matching algorithm

