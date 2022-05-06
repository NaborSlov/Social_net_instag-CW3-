import pytest

import run
from app.bookmarks.dao.bookmarks_dao import BookmarkDAO
from app.main.dao.posts_dao import PostsDAO
from app.main.dao.comments_dao import CommentsDAO


@pytest.fixture()
def test_client():
    app = run.app
    return app.test_client()


@pytest.fixture()
def bookmarks_instance():
    return BookmarkDAO('data/bookmarks.json')


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO('data/posts.json')
    return posts_dao_instance


@pytest.fixture()
def comments_dao():
    comments_dao_instance = CommentsDAO('data/comments.json')
    return comments_dao_instance
