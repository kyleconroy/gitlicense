from nose import tools
from web import is_license


def test_license_files():
    for path in ["license.txt", "LICENSE", "LICENSE.txt", "MIT-LICENSE"]:
        yield check_license, path


def check_license(path):
    tools.assert_true(is_license(path))
