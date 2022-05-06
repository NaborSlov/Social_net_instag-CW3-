import pytest

key_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
test_post = {
    "poster_name": "test",
    "poster_avatar": "test",
    "pic": "test",
    "content": "test",
    "views_count": 0,
    "likes_count": 0,
    "pk": 999
}


class TestBookmarksDao:
    def test_add_bookmark(self, bookmarks_instance):
        bookmarks_before = bookmarks_instance.get_all_bookmarks()
        bookmarks_instance.add_bookmark(test_post)
        bookmarks_after = bookmarks_instance.get_all_bookmarks()
        assert len(bookmarks_after) == len(bookmarks_before) + 1, "Закладки не добавляются"

        with pytest.raises(ValueError):
            bookmarks_instance.add_bookmark(test_post)

    def test_get_all_bookmarks(self, bookmarks_instance, posts_dao):
        bookmarks = bookmarks_instance.get_all_bookmarks()
        assert type(bookmarks) == list, "Возвращается не список"
        assert set(bookmarks[0].keys()) == key_should_be, "Неправильный набор ключей"

    def test_remove_bookmark(self, bookmarks_instance):
        bookmarks_before = bookmarks_instance.get_all_bookmarks()
        bookmarks_instance.remove_bookmark(999)
        bookmarks_after = bookmarks_instance.get_all_bookmarks()
        assert len(bookmarks_after) == len(bookmarks_before) - 1, "Закладки не удаляются"
