import requests


def test_url_status(url_adoption, status_code_adoptation):
    r = requests.get(url_adoption)
    assert r.status_code == int(status_code_adoptation)
