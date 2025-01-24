from flask import Blueprint
from app.routes.media_routes import media_bp
from app.routes.schedule_routes import schedule_bp

def register_routes(app):
    app.register_blueprint(media_bp, url_prefix="/media")
    app.register_blueprint(schedule_bp, url_prefix="/schedule")
