from flask import Blueprint, render_template, jsonify, request

from app.main.dao.posts_dao import PostsDAO
from app.main.dao.comments_dao import CommentsDAO
from app.bookmarks.dao.bookmarks_dao import BookmarkDAO

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
posts_dao_instance = PostsDAO('data/posts.json')
comments_dao_instance = CommentsDAO('data/comments.json')
bookmarks_instance = BookmarkDAO('data/bookmarks.json')


@main_blueprint.route('/')
def all_post():
    bookmarks_all = bookmarks_instance.get_all_bookmarks()
    len_bookmarks = len(bookmarks_all)
    post_all = posts_dao_instance.get_post_all()
    return render_template('index.html', post_all=post_all, len_bookmarks=len_bookmarks)


@main_blueprint.route('/posts/<int:post_id>')
def search_comment_post(post_id):
    post = posts_dao_instance.get_post_by_pk(post_id)
    comments = comments_dao_instance.get_comments_by_post_id(post_id)
    comments_len = len(comments)
    return render_template('post.html', comments=comments, post=post, comments_len=comments_len)


@main_blueprint.route('/search')
def search_post_by_keyword():
    keyword = request.args.get('kw')
    posts = posts_dao_instance.search_for_posts(keyword)
    len_posts = len(posts)
    return render_template('search.html', posts=posts, len_posts=len_posts)


@main_blueprint.route('/users/<username>')
def search_post_by_username(username):
    posts = posts_dao_instance.get_posts_by_user(username)
    username = username.lower().title()
    return render_template('user-feed.html', posts=posts, username=username)


@main_blueprint.route('/tag/<tag>')
def search_by_tag(tag):
    posts = posts_dao_instance.get_post_by_tag(tag)
    return render_template("user-feed.html", posts=posts)


@main_blueprint.route("/api/posts")
def api_posts():
    posts = posts_dao_instance.get_post_all()
    return jsonify(posts)


@main_blueprint.route('/api/posts/<int:post_id>')
def api_post_by_post_id(post_id):
    post = posts_dao_instance.get_post_by_pk(post_id)
    return jsonify(post)
