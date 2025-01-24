from app import create_app, db
from app.models import User, MediaPost, Schedule
from datetime import datetime

app = create_app()

with app.app_context():
    # Add a test user
    user = User(username="test_user", email="test@example.com")
    db.session.add(user)

    # Add a test media post
    post = MediaPost(filename="sample_image.jpg", file_type="image")
    db.session.add(post)

    # Add a test schedule with a valid datetime object
    schedule = Schedule(post_id=1, scheduled_time=datetime(2025, 1, 24, 10, 0, 0))  # Replace with your desired time
    db.session.add(schedule)

    # Commit changes
    db.session.commit()

    print("Database setup complete with sample data!")
