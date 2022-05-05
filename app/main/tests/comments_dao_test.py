import pytest

from app.main.dao.comments_dao import CommentsDAO


@pytest.fixture()
def comments_dao():
    comments_dao_instance = CommentsDAO('data/comments.json')
    return comments_dao_instance


key_should_be = {'post_id', 'commenter_name', 'comment', 'pk'}


class TestCommentsDAO:

    def test_get_all_comments(self, comments_dao):
        comments = comments_dao.load_comments()
        assert type(comments) == list, "Возвращается не список"
        assert len(comments) > 0, "Возвращается пустой список"
        assert set(comments[0].keys()) == key_should_be, "Неверный список ключей"

    def test_get_comments_by_post_id(self, comments_dao):
        comments = comments_dao.get_comments_by_post_id(1)
        comment = comments[0]
        assert comment['pk'] == 1, 'Возвращаются неправильно комментарии по номеру посту'
        assert set(comment.keys()) == key_should_be, "Неверный список ключей"


