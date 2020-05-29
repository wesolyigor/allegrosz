import os

from flask import Flask, g


def create_app():
    alegrosz = Flask(__name__)
    alegrosz.config['SECRET_KEY'] = b'tajne'
    alegrosz.config['ALLOWED_IMAGE_EXTENSIONS'] = ["jpg", "jpeg", "png"]
    alegrosz.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    alegrosz.config['IMAGE_UPLOADS'] = os.path.join(os.path.realpath(__file__), "uploads")

    from alegrosz.views.main_views import main_bp
    from alegrosz.views.items_views import item_bp
    from alegrosz.views.comments_views import comment_bp

    alegrosz.register_blueprint(main_bp)
    alegrosz.register_blueprint(item_bp)
    alegrosz.register_blueprint(comment_bp)

    return alegrosz


app = create_app()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
