from .common import *  # noqa


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": TESTS_DIR / "db.sqlite3",
    }
}