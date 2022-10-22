from .common import *  # noqa


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": PROJECT_DIR / "db-dev.sqlite3",
    }
}