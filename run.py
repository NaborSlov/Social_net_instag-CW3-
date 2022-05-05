from flask import Flask, render_template, send_from_directory

from app.main.views import main_blueprint
app = Flask(__name__)

app.register_blueprint(main_blueprint)


@app.route('/')
def home():
    pass


if __name__ == '__main__':
    app.run(debug=True)
