# HASHMATIC
A social media automation tool focused on integrating Threads for uploading posts and scheduling content.

## Features
- Upload and schedule video/image posts.
- Integrates with Threads API.
- Built using Python, Flask, and Bootstrap.

## Getting Started
1. Clone this repository.
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv hashmatic_env
   source hashmatic_env/bin/activate
   pip install -r requirements.txt

## Database Schema
### Tables
1. **User**
   - `id`: Primary key.
   - `username`: Unique username.
   - `email`: Unique email.

2. **MediaPost**
   - `id`: Primary key.
   - `filename`: Name of the uploaded file.
   - `file_type`: Type of the file (image/video).
   - `upload_date`: Timestamp of upload.

3. **Schedule**
   - `id`: Primary key.
   - `post_id`: Foreign key linking to MediaPost.
   - `scheduled_time`: Time for scheduled post.

