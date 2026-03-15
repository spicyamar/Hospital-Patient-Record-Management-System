from flask import Flask, render_template
from flask_login import LoginManager
from config import Config
from database.db import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize DB client
    init_db(app.config['MONGO_URI'])

    # Login manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from utils.auth_utils import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_by_id(user_id)

    # Register blueprints
    from routes.auth_routes import auth_bp
    from routes.patient_routes import patient_bp
    from routes.record_routes import record_bp
    from routes.appointment_routes import appointment_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(record_bp)
    app.register_blueprint(appointment_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, use_reloader=False)
