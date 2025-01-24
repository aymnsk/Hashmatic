from flask import Blueprint, request, jsonify
from app import db
from app.models import MediaPost

media_bp = Blueprint("media", __name__)

@media_bp.route("/upload", methods=["POST"])
def upload_media():
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Save the file to the database (filename only for simplicity)
    media = MediaPost(filename=file.filename, file_type="image")  # Adjust file_type dynamically if needed
    db.session.add(media)
    db.session.commit()

    return jsonify({"message": "File uploaded successfully", "media_id": media.id}), 201
