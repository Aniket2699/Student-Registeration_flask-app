Flask Student Registration Web Application
Project Overview

This project is a Flask-based Student Registration Web Application that allows users to register students by submitting their details through a web form. The submitted data is stored in a MySQL database, and users can view all registered students in a table format.

The project demonstrates:

Flask backend development

MySQL database integration

HTML/CSS for frontend

Deployment on AWS EC2 (optional)

GitHub version control

Features

Register students with the following details:

Name

Email

Phone Number

Course

Address

View all registered students in a table

Input validation on both client and server side

Modular and scalable code structure

Technology Stack
Layer	Technology
Frontend	HTML, CSS (Bootstrap optional)
Backend	Python (Flask)
Database	MySQL
Deployment	AWS EC2 (optional)
Version Control	Git, GitHub
Setup Instructions
1. Clone the Repository
git clone https://github.com/Aniket2699/Student-Registeration_flask-app.git
cd Student-Registeration_flask-app

2. Create and Activate a Virtual Environment
python3 -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Configure Database

Login to MySQL:

mysql -u root -p


Run these SQL commands:

CREATE DATABASE student_db;
CREATE USER 'flaskuser'@'%' IDENTIFIED BY 'StrongPassword123';
GRANT ALL PRIVILEGES ON student_db.* TO 'flaskuser'@'%';
FLUSH PRIVILEGES;


Update .env file with your credentials:

FLASK_ENV=development
SECRET_KEY=Aniket@26
DATABASE_USER=flaskuser
DATABASE_PASSWORD=StrongPassword123
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306
DATABASE_NAME=student_db

5. Initialize Database Tables
python


Then inside Python shell:

from app import app, db
with app.app_context():
    db.create_all()


Type exit() to quit.

6. Run the Application
flask run


App will run at:
🔗 http://127.0.0.1:5000

7. Deployment on AWS EC2 (Optional)

Launch an EC2 instance (Ubuntu)

Install required packages:

sudo apt update
sudo apt install python3-pip python3-venv mysql-client


Clone the repo and repeat steps 2–6

Use Gunicorn + Nginx for production deployment

Screenshots
1. Registration Page

2. Registered Students

Save screenshots in a folder named screenshots/ inside the project directory.

Major Components Explained
1. app.py

Main Flask application file

Contains routes for registration and displaying students

2. config.py

Loads database configuration from .env file using python-dotenv

3. templates/

HTML templates for frontend (register.html, students.html, base.html)

4. schema.sql

SQL commands for setting up initial database structure

5. requirements.txt

Python dependencies list for easy installation

6. static/

Contains CSS and static files for frontend styling

GitHub Repository

The complete source code is hosted here:
🔗 GitHub Repo Link

Contributors

Aniket Dauskar – Developer
