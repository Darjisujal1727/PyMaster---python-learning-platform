from flask import Flask

from config import Config
from models import Course, db
from routes.main import main_bp


def create_app(config_class=Config):
    """Create and configure the PyMaster Flask application."""
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()
        from seed.curriculum import seed_curriculum
        from services.lesson_content import add_resources

        seed_curriculum()
        add_resources()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
