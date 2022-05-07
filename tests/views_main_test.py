import pytest


class TestViewsMain:

    def test_all_post(self, test_client):
        response = test_client.get('/')
        assert response.status_code == 200, 'Статус код вывода всех постов неправильный'

    def test_search_comment_post(self, test_client):
        response = test_client.get('/posts/1')
        assert response.status_code == 200, 'Статус код вывода постов по номеру неправильный'

    def test_search_post_by_keyword(self, test_client):
        response = test_client.get('/search?kw=еда')
        assert response.status_code == 200, 'Статус код вывода постов по ключевому слову неправильный'

    def test_search_post_by_username(self, test_client):
        response = test_client.get('/users/leo')
        assert response.status_code == 200, 'Статус код вывода постов по имени неправильный'

    def test_search_by_tag(self, test_client):
        response = test_client.get('/tag/food')
        assert response.status_code == 200, 'Статус код вывода всех постов по тегу неправильный'

