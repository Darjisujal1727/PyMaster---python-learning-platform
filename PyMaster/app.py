from flask import Flask

from config import Config
from models import db
from routes.main import main_bp


def create_app(config_class=Config):
    """Create and configure the PyMaster Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
