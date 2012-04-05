# GitLicense

REST API for what license a project is under

## Algorithm

The current algorithm is really simple. I look for a `LICENSE` or `LICENSE.*` file, and see if it matches any of the licenses I support.

### Supported Licenses

* MIT license (MIT)
* ISC License (ISC)
* Apache License 2.0 (Apache-2.0)
* GNU General Public License, version 3 (GPL-3.0)
* GNU AFFERO GENERAL PUBLIC LICENSE, Version 3 (AGPL-3.0)
* BSD License

## TODO

* Improve the license matching algorithm
* Support more licenses

