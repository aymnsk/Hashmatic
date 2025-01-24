from flask import Blueprint, request, jsonify
from datetime import datetime
from app import db
from app.models import Schedule

schedule_bp = Blueprint("schedule", __name__)

@schedule_bp.route("/add", methods=["POST"])
def add_schedule():
    data = request.get_json()
    post_id = data.get("post_id")
    scheduled_time = data.get("scheduled_time")

    if not post_id or not scheduled_time:
        return jsonify({"error": "Missing post_id or scheduled_time"}), 400

    try:
        scheduled_time = datetime.strptime(scheduled_time, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return jsonify({"error": "Invalid datetime format. Use YYYY-MM-DD HH:MM:SS"}), 400

    # Add the schedule to the database
    schedule = Schedule(post_id=post_id, scheduled_time=scheduled_time)
    db.session.add(schedule)
    db.session.commit()

    return jsonify({"message": "Schedule added successfully", "schedule_id": schedule.id}), 201
