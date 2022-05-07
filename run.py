from flask import Flask, render_template
import logging

from logger import create_logger
from app.main.views import main_blueprint
from app.bookmarks.views import bookmarks_blueprint

create_logger()
logger = logging.getLogger('basik')

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(main_blueprint)
app.register_blueprint(bookmarks_blueprint)


@app.errorhandler(404)
def bad_request_error(error):
    logger.error(error)
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
