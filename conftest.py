from fixtures.application import Application
import pytest
__author__ = 'pzqa'


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
