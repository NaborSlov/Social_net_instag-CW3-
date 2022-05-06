from flask import Flask

from app.main.views import main_blueprint
from app.bookmarks.views import bookmarks_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(bookmarks_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
