from flask import Flask


def create_app():
    allegrosz = Flask(__name__)

    from allegrosz.views.main_views import main_bp

    allegrosz.register_blueprint(main_bp)

    return allegrosz


app = create_app()
