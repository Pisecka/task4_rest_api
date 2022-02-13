import pytest


def test_status_200(dog_api_random):
    assert dog_api_random.status_code == 200


def test_status_success(dog_api_random):
    d = dog_api_random.json()
    assert d['status'] == 'success'


def test_message(dog_api_random):
    d = dog_api_random.json()
    assert d['message']


@pytest.mark.parametrize("breed", ['akita', 'borzoi', 'chihuahua', 'corgi'])
def test_check_breed(dog_api_all_breeds, breed):
    d = dog_api_all_breeds.json()
    assert breed in d['message']


@pytest.mark.parametrize("sub_breed", ['afghan', 'basset', 'blood', 'english', 'ibizan', 'plott', 'walker'])
def test_check_sub_breed(dog_api_sub_breed, sub_breed):
    d = dog_api_sub_breed.json()
    assert sub_breed in d['message']
