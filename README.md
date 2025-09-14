# Flask-Based Student Registration Web Application

## **Project Overview**
This project is a **Flask-based web application** designed to register students and store their details in a MySQL database.  
It provides an intuitive web form for entering student data and a tabular interface for viewing, editing, and deleting records.  
The project is perfect for learning **Flask**, **MySQL integration**, **form handling**, and **deployment workflows**.

The application was later enhanced with optional CI/CD integration using **Jenkins** and **GitHub**, and it can also be deployed on **AWS EC2**.

---

## **Features**
- 📝 **Student Registration Form**  
  Collects:
  - Name
  - Email
  - Phone Number
  - Course
  - Address

- 🔒 **Validation**
  - Client-side validation (HTML5)
  - Server-side validation (Flask)

- 💾 **Database Integration**
  - MySQL for persistent data storage
  - SQLAlchemy ORM for database management

- 📊 **View Registered Students**
  - View all registered students in a table
  - Shows time of registration

- ✏️ **Edit & Delete Students** *(optional enhancement)*

- 🎨 **Responsive UI**
  - Styled with Bootstrap 5

---

## **Technology Stack**
| Component      | Technology |
|----------------|------------|
| **Frontend**   | HTML, CSS, Bootstrap 5 |
| **Backend**    | Python (Flask Framework) |
| **Database**   | MySQL |
| **Version Control** | Git & GitHub |
| **Optional Deployment** | AWS EC2 |
| **CI/CD (Optional)** | Jenkins |

---

## **Project Structure**

stud-reg-flask-app/
├── app.py # Main Flask application
├── config.py # Configuration file (DB, secrets, etc.)
├── requirements.txt # Python dependencies
├── schema.sql # MySQL schema for creating database & table
├── .env.example # Environment variable template
├── templates/ # HTML templates
│ ├── base.html
│ ├── register.html
│ └── students.html
├── static/
│ └── css/
│ └── styles.css # Custom styling
│ 
└── README.md # Project documentation


## **Setup Instructions**

### **1. Clone the Repository**
git clone https://github.com/Aniket2699/Student-Registeration_flask-app.git
cd Student-Registeration_flask-app

### **2. Create and Activate a Virtual Environment**

python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

### **3. Install Dependencies**

pip install -r requirements.txt

### **4. Configure Environment Variables**
Create a .env file by copying .env.example:

cp .env.example .env
Update the .env file with your MySQL credentials:


FLASK_ENV=development
SECRET_KEY=your_secret_key_here
DATABASE_USER=root
DATABASE_PASSWORD=your_mysql_password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306
DATABASE_NAME=student_db
⚠️ Note: Never commit .env to GitHub. It contains sensitive information.

### **5. Set Up the Database**
Login to MySQL:


mysql -u root -p
Run the schema file to create the database and table:

SOURCE schema.sql;
Verify:


SHOW DATABASES;
USE student_db;
SHOW TABLES;

### **6. Run Flask Application**

flask run
By default, the app will run at:


http://127.0.0.1:5000/
Usage
Register a Student
Navigate to /register

Fill in the student details

Submit the form

View Registered Students
Go to /students

See all registered students displayed in a table.

Sample SQL Output
When a student is registered successfully:

mysql> SELECT * FROM students;
+----+----------------+---------------------------+------------+--------+------------------------+---------------------+
| id | name           | email                     | phone      | course | address                | created_at          |
+----+----------------+---------------------------+------------+--------+------------------------+---------------------+
|  1 | Aniket Dauskar | aniketdauskar@gmail.com   |            | DevOps | 46, MARDI ROAD, RAJURA | 2025-09-14 10:02:47 |
+----+----------------+---------------------------+------------+--------+------------------------+---------------------+

Screenshots
1. Registration Page
Resgisteration page.png

3. View Students Page
   Registered students.png

Explanation of Major Components
Component	Description
app.py	Main Flask app containing routes for registration, data handling, and viewing students
config.py	Centralized configuration for DB connection, Flask secret key, etc.
templates/	Contains HTML pages for registration, viewing, editing students
static/css/styles.css	Custom styling for better UI
requirements.txt	List of all Python dependencies required to run the app
schema.sql	MySQL commands to create the required database and table
.env	Stores sensitive environment variables such as DB credentials

Optional Deployment
Deploy on AWS EC2
Launch an EC2 instance with Ubuntu.

Install Python, MySQL, and required dependencies.

Clone your repository:

bash
Copy code
git clone https://github.com/swati-zampal/stud-reg-flask-app.git
Configure .env with production credentials.

Run the app with Gunicorn:

bash
Copy code
gunicorn --bind 0.0.0.0:8000 app:app
Configure Nginx as a reverse proxy for production deployment.

Optional Jenkins CI/CD Integration
You can integrate this project with Jenkins to automate deployment:

Jenkins pipeline pulls the latest code from GitHub.

Builds and deploys the Flask app automatically to your EC2 instance.

Ensures continuous updates without manual steps.

GitHub Repository
https://github.com/Aniket2699/Student-Registeration_flask-app.git

Future Enhancements
Add authentication (Admin login)

Export student data to CSV/Excel

Advanced search and filtering

REST API integration for mobile apps

Author
Aniket Dauskar

📧 Email: aniketdauskar99@gmail.com

🌐 LinkedIn: linkedin.com/in/aniketdauskar

📍 Pune, Maharashtra, India

