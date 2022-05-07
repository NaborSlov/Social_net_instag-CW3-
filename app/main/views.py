from flask import Blueprint, render_template, jsonify, request, abort
import json
import logging

from logger import create_logger
from app.main.dao.posts_dao import PostsDAO
from app.main.dao.comments_dao import CommentsDAO
from app.bookmarks.dao.bookmarks_dao import BookmarkDAO

create_logger()
logger = logging.getLogger('basik')

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
posts_dao_instance = PostsDAO('data/posts.json')
comments_dao_instance = CommentsDAO('data/comments.json')
bookmarks_instance = BookmarkDAO('data/bookmarks.json')


@main_blueprint.route('/')
def all_post():
    """
    Фьюшка для получения всех постов в ленте
    """
    try:
        bookmarks_all = bookmarks_instance.get_all_bookmarks()
        post_all = posts_dao_instance.get_post_all()
        len_bookmarks = len(bookmarks_all)
        return render_template('index.html', post_all=post_all, len_bookmarks=len_bookmarks)
    except (FileNotFoundError, json.JSONDecodeError):  # обработка ошибки если проблема в открываемом файле
        logger.error("Нет такого файла или не удалось преобразовать json")
        abort(404)


@main_blueprint.route('/posts/<int:post_id>')
def search_comment_post(post_id):
    """
    Фьюшка для поиска постов по номеру поста
    """
    try:
        post = posts_dao_instance.get_post_by_pk(post_id)
        comments = comments_dao_instance.get_comments_by_post_id(post_id)
        comments_len = len(comments)
        return render_template('post.html', comments=comments, post=post, comments_len=comments_len)
    except (FileNotFoundError, json.JSONDecodeError):  # обработка ошибки если проблема в открываемом файле
        logger.error("Нет такого файла или не удалось преобразовать json")
        abort(404)


@main_blueprint.route('/search')
def search_post_by_keyword():
    """
    Фьюшка для получения поста по ключевому слову
    """
    keyword = request.args.get('kw')  # получение слова из query-запроса
    try:
        posts = posts_dao_instance.search_for_posts(keyword)
        len_posts = len(posts)
    except (FileNotFoundError, json.JSONDecodeError):  # обработка ошибки если проблема в открываемом файле
        logger.error("Нет такого файла или не удалось преобразовать json")
        abort(404)
    else:
        return render_template('search.html', posts=posts, len_posts=len_posts)


@main_blueprint.route('/users/<username>')
def search_post_by_username(username):
    """
    Фьюшка для поиска поста по имени
    """
    try:
        posts = posts_dao_instance.get_posts_by_user(username)
        username = username.lower().title()
    except (FileNotFoundError, json.JSONDecodeError):  # обработка ошибки если проблема в открываемом файле
        logger.error("Нет такого файла или не удалось преобразовать json")
        abort(404)
    else:
        return render_template('user-feed.html', posts=posts, username=username)


@main_blueprint.route('/tag/<tag>')
def search_by_tag(tag):
    """
    Фьюшка для получения поста по тегу
    """
    try:
        posts = posts_dao_instance.get_post_by_tag(tag)
    except (FileNotFoundError, json.JSONDecodeError):  # обработка ошибки если проблема в открываемом файле
        logger.error("Нет такого файла или не удалось преобразовать json")
        abort(404)
    else:
        return render_template("user-feed.html", posts=posts)


@main_blueprint.route("/api/posts")
def api_posts():
    posts = posts_dao_instance.get_post_all()
    return jsonify(posts)


@main_blueprint.route('/api/posts/<int:post_id>')
def api_post_by_post_id(post_id):
    post = posts_dao_instance.get_post_by_pk(post_id)
    return jsonify(post)
