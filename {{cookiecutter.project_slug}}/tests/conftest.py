import pytest

from tests.factories import *  # noqa


@pytest.fixture()
def admin(user_factory):
    return user_factory(is_staff=True, is_superuser=True)