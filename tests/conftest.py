import pytest
import requests


@pytest.fixture(scope="session")
def dog_api_random():
    url = 'https://dog.ceo/api/breeds/image/random'
    r = requests.get(url)
    return r


@pytest.fixture()
def dog_api_all_breeds():
    url = 'https://dog.ceo/api/breeds/list/all'
    r = requests.get(url)
    return r


@pytest.fixture()
def dog_api_sub_breed():
    url = 'https://dog.ceo/api/breed/hound/list'
    r = requests.get(url)
    return r


@pytest.fixture()
def brewery_api_url():
    return 'https://api.openbrewerydb.org'


@pytest.fixture()
def jsonplaceholder_api_url():
    return 'https://jsonplaceholder.typicode.com/posts'


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        default=200,
        help="This is a status codes"
    )


@pytest.fixture
def url_adoption(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code_adoptation(request):
    return request.config.getoption("--status_code")
