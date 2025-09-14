# 📚 Flask-Based Student Registration Web Application

---

## **📖 Project Overview**
This project is a **Flask-based web application** designed to register students and store their details in a **MySQL database**.  
It provides an intuitive **web form** for entering student data and a **tabular interface** for viewing, editing, and deleting records.

The project is ideal for learning:
- Flask fundamentals
- MySQL database integration
- Form handling and validation
- Deployment workflows with optional CI/CD via Jenkins

---

## **✨ Features**

- 📝 **Student Registration Form**
  - Name, Email, Phone Number, Course, Address

- 🔒 **Validation**
  - Client-side validation using HTML5
  - Server-side validation using Flask

- 💾 **Database Integration**
  - Persistent storage using MySQL
  - SQLAlchemy ORM for seamless interaction

- 📊 **View Registered Students**
  - Displays all registered students in a responsive table
  - Shows time of registration

- ✏️ **Edit & Delete Records** *(optional enhancement)*

- 🎨 **Responsive UI**
  - Built with **Bootstrap 5** for mobile-friendly design

---

## **🛠️ Technology Stack**

| Layer              | Technology Used |
|--------------------|----------------|
| **Frontend**       | HTML, CSS, Bootstrap 5 |
| **Backend**        | Python (Flask Framework) |
| **Database**       | MySQL |
| **Version Control**| Git & GitHub |
| **Deployment (Optional)** | AWS EC2 |
| **CI/CD (Optional)** | Jenkins |


## **⚙️ Setup Instructions**

### **1️⃣ Clone the Repository**

git clone https://github.com/Aniket2699/Student-Registeration_flask-app.git
cd stud-reg-flask-app
### **2️⃣ Create and Activate Virtual Environment**

python3 -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

### **3️⃣ Install Dependencies**

pip install -r requirements.txt

### **4️⃣ Configure Environment Variables**
Create a .env file by copying the provided template:

cp .env.example .env
Edit the .env file and set your MySQL credentials:

env
Copy code
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
DATABASE_USER=root
DATABASE_PASSWORD=your_mysql_password
DATABASE_HOST=127.0.0.1
DATABASE_PORT=3306
DATABASE_NAME=student_db
⚠️ Important: Never commit your .env file to GitHub.

### **5️⃣ Set Up the Database**
Login to MySQL:

mysql -u root -p
Run the schema file to create the database and table:


SOURCE schema.sql;
Verify:


SHOW DATABASES;
USE student_db;
SHOW TABLES;

### **6️⃣ Run the Flask Application**

flask run
By default, the app will run at:
🌐 http://127.0.0.1:5000/

🚀 Usage
Register a Student
Navigate to /register

Fill in the required details

Submit the form to register a student

View Registered Students
Go to /students

See all registered students displayed in a table with options to edit or delete.

### **🗄️ Sample Database Output**
After registering a student, the database will show:


mysql> SELECT * FROM students;
+----+----------------+---------------------------+------------+--------+------------------------+---------------------+
| id | name           | email                     | phone      | course | address                | created_at          |
+----+----------------+---------------------------+------------+--------+------------------------+---------------------+
|  5 | Aniket Dauskar | aniketdauskar99@gmail.com | 7620162625 | DevOps | 46, MARDI ROAD, RAJURA | 2025-09-14 10:02:47 |
+----+----------------+---------------------------+------------+--------+------------------------+---------------------+
🖼️ Screenshots
1. Registration Page
<img width="1917" height="972" alt="Registeration page" src="https://github.com/user-attachments/assets/e558d9e2-d71f-4954-937b-4f3df3034e3f" />


2. View Students Page
<img width="1916" height="967" alt="Registered students" src="https://github.com/user-attachments/assets/cba9bce7-d53b-47bf-b27c-8636ce43e731" />


### **🔍 Explanation of Major Components**
File / Folder	Description
app.py	Core Flask app with routes for registration, data handling, and viewing students
config.py	Centralized configuration for DB connection and Flask secret key
templates/	Contains HTML templates (register, list view, edit form)
static/css/	Custom CSS for styling
requirements.txt	Python dependencies list
schema.sql	SQL commands to create database and table
.env	Stores sensitive environment variables like DB credentials

### **☁️ Optional Deployment on AWS EC2**
Launch an Ubuntu EC2 instance.

Install Python, MySQL, and dependencies:


sudo apt update
sudo apt install python3-pip mysql-server
Clone your GitHub repository:


git clone https://github.com/Aniket2699/Student-Registeration_flask-app.git
Set up .env with production credentials.

Run the app using Gunicorn:


gunicorn --bind 0.0.0.0:8000 app:app
Configure Nginx as a reverse proxy.

### **⚡ Optional Jenkins CI/CD Integration**
You can integrate this project with Jenkins for continuous deployment:

Jenkins pulls the latest code from GitHub.

Builds and deploys the Flask app to AWS EC2 automatically.

Ensures smooth and automated deployment cycles.

### **🔗 GitHub Repository**
GitHub Repo Link
https://github.com/Aniket2699/Student-Registeration_flask-app.git

### **💡 Future Enhancements**
Add admin authentication

Export student data to CSV/Excel

Implement search and filtering

Build a REST API for mobile app integration

### **👨‍💻 Author**
Aniket Dauskar
📧 Email: aniketdauskar99@gmail.com
🔗 LinkedIn: linkedin.com/in/aniketdauskar
📍 Pune, Maharashtra, India

📜 License
This project is open-source and available under the MIT License.

🌟 Support
If you found this project helpful, please star ⭐ the repository to show your support!
