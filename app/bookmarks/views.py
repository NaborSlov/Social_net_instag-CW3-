from flask import Blueprint, render_template, redirect

from app.bookmarks.dao.bookmarks_dao import BookmarkDAO
from app.main.dao.posts_dao import PostsDAO

bookmarks_blueprint = Blueprint("bookmarks_blueprint", __name__, template_folder='templates')

bookmarks_instance = BookmarkDAO("data/bookmarks.json")
posts_instance = PostsDAO("data/posts.json")


@bookmarks_blueprint.route('/bookmarks/add/<int:post_id>')
def add_bookmark(post_id):
    """
    Фьюшка для добавления закладки
    :param post_id: номер поста
    :return: возвращает на главную страницу
    """
    post = posts_instance.get_post_by_pk(post_id)
    # обработка ошибки если добавляют один пост два раза
    try:
        bookmarks_instance.add_bookmark(post)
    except ValueError:
        return redirect('/')
    return redirect('/')


@bookmarks_blueprint.route('/bookmarks/remove/<int:post_id>')
def remove_bookmark(post_id):
    """
    Фьюшка для удаления закладки по номеру
    :param post_id: номер поста
    :return: возвращает на главную страницу
    """
    bookmarks_instance.remove_bookmark(post_id)
    return redirect('/')


@bookmarks_blueprint.route('/bookmarks')
def get_all_bookmarks():
    """
    Фьюшка для показа всех закладок
    """
    bookmarks = bookmarks_instance.get_all_bookmarks()
    return render_template('bookmarks.html', bookmarks=bookmarks)
