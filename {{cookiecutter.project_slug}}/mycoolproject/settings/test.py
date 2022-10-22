from .common import *  # noqa
from .dev import DATABASES


DATABASES["default"]["TEST"] = {
    "NAME": TESTS_DIR / "db-test.sqlite3",  # Comment out to use :inmemory:
}