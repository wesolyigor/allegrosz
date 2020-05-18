from flask import Flask, g


def create_app():
    allegrosz = Flask(__name__)

    allegrosz.config["SECRET_KEY"] = 'tajne'

    from allegrosz.views.main_views import main_bp
    from allegrosz.views.item_views import items_bp

    allegrosz.register_blueprint(main_bp)
    allegrosz.register_blueprint(items_bp)

    return allegrosz


app = create_app()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "__database", None)
    if db is not None:
        db.close()
