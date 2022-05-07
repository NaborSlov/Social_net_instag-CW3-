import pytest


class TestViewsBookmark:

    def test_add_bookmark(self, test_client):
        response = test_client.get('/bookmarks/add/1')
        assert response.status_code == 302, 'Статус код добавления заметки неправильный'

    def test_get_all_bookmarks(self, test_client):
        resource = test_client.get('/bookmarks')
        assert resource.status_code == 200, 'Статус код вывода всех заметок неправильный'

    def test_remove_bookmark(self, test_client):
        resource = test_client.get('/bookmarks/remove/1')
        assert resource.status_code == 302, 'Статус код удаления заметок неправильный'
