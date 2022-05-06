import json

from app.main.dao.comments_dao import CommentsDAO
from functions import clear_punctuation


class PostsDAO:
    """
    DAO для обработки данных из json файла с постами
    """
    def __init__(self, path):
        """
        :param path: путь до json файла
        """
        self.path = path  # путь до директории до json файла с постами

    def load_post(self):
        """
        Функция загрузки данных из json файла
        """
        with open(self.path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data

    def get_post_all(self):
        """
        Функция получения листа со всеми постами
        """
        all_post = self.load_post()
        return all_post

    def get_posts_by_user(self, username: str):
        """
        Возвращает посты определенного пользователя
        :param username: имя пользователя
        :return: list
        """
        all_post = self.load_post()
        return list(filter(lambda x: username.lower() == x['poster_name'].lower(), all_post))

    def search_for_posts(self, query: str):
        """
        Поиск постов по ключевому слову
        :param query: слово
        :return:
        """
        all_post = self.load_post()
        return list(filter(lambda x: query.lower() in clear_punctuation(x['content']).lower().split(), all_post))

    def get_post_by_pk(self, pk: int):
        """
        Получение поста по ключу
        """
        all_post = self.load_post()
        return next(filter(lambda x: pk == x['pk'], all_post))

    def get_post_by_tag(self, tag: str):
        """
        Получение постов по тегу
        """
        all_post = self.load_post()
        return list(filter(lambda x: x['content'].count(f"#{tag}"), all_post))
