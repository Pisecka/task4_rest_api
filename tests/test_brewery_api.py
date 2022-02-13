import requests
import pytest


@pytest.mark.parametrize('city', ['san_diego', 'new_york', 'los_angeles'])
def test_status_code(city, brewery_api_url):
    r = requests.get(brewery_api_url + "/breweries", params={'by_city': city})
    assert r.status_code == 200


@pytest.mark.parametrize('city', ['san_diego', 'new_york', 'los_angeles'])
def test_check_city(city, brewery_api_url):
    r = requests.get(brewery_api_url + "/breweries", params={'by_city': city})
    assert r.json() != []


@pytest.mark.parametrize('state', ['ohio', 'colorado', 'california'])
def test_check_state(state, brewery_api_url):
    r = requests.get(brewery_api_url + "/breweries", params={'by_state': state})
    assert r.json() != []


def test_single_brewery(brewery_api_url):
    r = requests.get(brewery_api_url + "/breweries" + "/madtree-brewing-cincinnati")
    d = r.json()
    assert d['city'] == "Cincinnati"
    assert d['state'] == "Ohio"


@pytest.mark.parametrize('name', ['dog', 'cat', 'horse'])
def test_search_by_name(name, brewery_api_url):
    r = requests.get(brewery_api_url + "/breweries" + "/search", params={'query': name})
    assert r.json() != []
