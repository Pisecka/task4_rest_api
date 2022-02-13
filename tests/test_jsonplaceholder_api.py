import requests
import pytest
import json

@pytest.mark.parametrize('post', [1,2,3,4,5,6])
def test_status_code(post, jsonplaceholder_api_url):
    r = requests.get(jsonplaceholder_api_url + f'/{post}')
    assert r.status_code == 200


@pytest.mark.parametrize('post', [1,2,3,4,5,6])
def test_content_not_empty(post, jsonplaceholder_api_url):
    r = requests.get(jsonplaceholder_api_url + f'/{post}')
    d = r.json()
    assert d != {}


def test_create_post(jsonplaceholder_api_url):
    params = json.dumps({'id':101, 'title': 'foo', 'body': 'bar content is fine', 'userId': 1})
    r = requests.post(jsonplaceholder_api_url,
                      params=params,
                      headers={'Content-type': 'application/json; charset=UTF-8'}
                      )
    assert r.status_code == 201


def test_update_post(jsonplaceholder_api_url):
    params = json.dumps({'id':1, 'title': 'fooFOO', 'body': 'barBAR content is fine', 'userId': 1})
    r = requests.put(jsonplaceholder_api_url+'/1',
                      params=params,
                      headers={'Content-type': 'application/json; charset=UTF-8'}
                      )
    assert r.status_code == 200


def test_delete_post(jsonplaceholder_api_url):
    r = requests.delete(jsonplaceholder_api_url+'/1')
    assert r.status_code == 200