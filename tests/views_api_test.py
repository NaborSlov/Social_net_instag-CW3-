import pytest

key_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


def test_api_posts(test_client):
    response = test_client.get('/api/posts')
    json = response.json
    assert response.status_code == 200, "Данные не получены"
    assert type(json) == list, "Неверный тип данных"
    assert json[0].keys() == key_should_be, "Неверный список ключей"


def test_api_post_by_post_id(test_client):
    resource = test_client.get('/api/posts/1')
    json = resource.json
    assert resource.status_code == 200, "Данные не получены"
    assert type(json) == dict, "Неверный тип данных"
    assert json.keys() == key_should_be, "Неверный список ключей"
