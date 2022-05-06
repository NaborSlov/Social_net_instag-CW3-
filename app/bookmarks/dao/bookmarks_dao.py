import json


class BookmarkDAO:

    def __init__(self, path):
        self.path = path

    def load_bookmarks(self):
        with open(self.path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data

    def get_all_bookmarks(self):
        bookmarks = self.load_bookmarks()
        return bookmarks

    def add_bookmark(self, bookmark):
        bookmarks = self.load_bookmarks()

        for i in bookmarks:
            if bookmark['pk'] == i['pk']:
                raise ValueError("Не должно быть два одинаковых поста")

        bookmarks.append(bookmark)
        with open(self.path, 'w', encoding='UTF-8') as f:
            json.dump(bookmarks, f, indent=4, ensure_ascii=False)

    def remove_bookmark(self, pk: int):
        bookmarks = self.load_bookmarks()
        data = list(filter(lambda x: x['pk'] != pk, bookmarks))
        with open(self.path, 'w', encoding='UTF-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
