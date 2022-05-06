import pytest

key_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}


class TestPostDao:

    def test_get_post_all(self, posts_dao):
        all_post = posts_dao.get_post_all()
        assert type(all_post) == list, "Возвращается не список"
        assert len(all_post) > 0, "Возвращается пустой список"
        assert all_post[0].keys() == key_should_be, "Неверный список ключей"

    def test_search_for_posts(self, posts_dao):
        posts = posts_dao.search_for_posts('Квадратная')
        assert type(posts) == list, "Возвращается не список"
        assert len(posts) > 0, "Возвращается пустой список"
        assert posts[0].get('pk') == 1, "Неверный поиск по ключевому слову"

    def test_get_post_by_pk(self, posts_dao):
        post = posts_dao.get_post_by_pk(1)
        assert type(post) == dict, "Возвращается не словарь"
        assert post['pk'] == 1, "Неверный поиск по pk"
