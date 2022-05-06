import json


class BookmarkDAO:
    """
    DAO для обработки данных из json файла с закладками
    """
    def __init__(self, path: str):
        """
        :param path: путь до json файла
        """
        self.path = path

    def load_bookmarks(self):
        """
        Загрузка данных из json файла
        return: list
        """
        with open(self.path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data

    def get_all_bookmarks(self):
        """
        Получение всех закладок
        return: list
        """
        bookmarks = self.load_bookmarks()
        return bookmarks

    def add_bookmark(self, post):
        """
        Добавление выбранного поста в закладки
        param post:
        """
        bookmarks = self.load_bookmarks()
        # проверка на повторяющиеся посты в закладках
        for i in bookmarks:
            if post['pk'] == i['pk']:
                raise ValueError("Не должно быть два одинаковых поста")

        bookmarks.append(post)
        with open(self.path, 'w', encoding='UTF-8') as f:
            json.dump(bookmarks, f, indent=4, ensure_ascii=False)

    def remove_bookmark(self, pk: int):
        """
        Удаление поста по его pk
        :param pk:
        """
        bookmarks = self.load_bookmarks()
        data = list(filter(lambda x: x['pk'] != pk, bookmarks))
        with open(self.path, 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
