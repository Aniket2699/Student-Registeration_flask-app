from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# models
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    phone = db.Column(db.String(20))
    course = db.Column(db.String(100))
    address = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f"<Student {self.name} - {self.email}>"

# helpers
def validate_student_form(form):
    errors = []
    name = form.get('name', '').strip()
    email = form.get('email', '').strip()
    phone = form.get('phone', '').strip()
    course = form.get('course', '').strip()
    address = form.get('address', '').strip()

    if not name:
        errors.append("Name is required.")
    if not email:
        errors.append("Email is required.")
    else:
        # simple email regex
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format.")
    if phone:
        # allow digits, +, -, spaces
        if not re.match(r'^[\d\+\-\s]{7,20}$', phone):
            errors.append("Invalid phone number.")
    # course optional but you can enforce presence:
    # if not course: errors.append("Course is required.")

    return errors

# routes
@app.route('/', methods=['GET'])
def index():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        errors = validate_student_form(request.form)
        if errors:
            for e in errors:
                flash(e, 'danger')
            # preserve entered fields by re-rendering form with existing values
            return render_template('register.html', form=request.form)
        # valid -> create student
        try:
            student = Student(
                name=request.form['name'].strip(),
                email=request.form['email'].strip(),
                phone=request.form.get('phone', '').strip(),
                course=request.form.get('course', '').strip(),
                address=request.form.get('address', '').strip()
            )
            db.session.add(student)
            db.session.commit()
            flash('Student registered successfully!', 'success')
            return redirect(url_for('students'))
        except Exception as e:
            db.session.rollback()
            # handle duplicate email or DB errors
            flash(f'Failed to register student: {str(e)}', 'danger')
            return render_template('register.html', form=request.form)

    return render_template('register.html', form={})

@app.route('/students', methods=['GET'])
def students():
    all_students = Student.query.order_by(Student.created_at.desc()).all()
    return render_template('students.html', students=all_students)

# optional: edit & delete
@app.route('/student/edit/<int:student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = Student.query.get_or_404(student_id)
    if request.method == 'POST':
        errors = validate_student_form(request.form)
        if errors:
            for e in errors: flash(e, 'danger')
            return render_template('register.html', form=request.form, edit=True, student=student)
        student.name = request.form['name'].strip()
        student.email = request.form['email'].strip()
        student.phone = request.form.get('phone', '').strip()
        student.course = request.form.get('course', '').strip()
        student.address = request.form.get('address', '').strip()
        try:
            db.session.commit()
            flash('Student record updated.', 'success')
            return redirect(url_for('students'))
        except Exception as e:
            db.session.rollback()
            flash(f'Update failed: {str(e)}', 'danger')
    # GET
    return render_template('register.html', form=student.__dict__, edit=True, student=student)

@app.route('/student/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    try:
        db.session.delete(student)
        db.session.commit()
        flash('Student deleted.', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Deletion failed: {str(e)}', 'danger')
    return redirect(url_for('students'))

if __name__ == '__main__':
    # ensure tables exist (for quick dev). For production use migrations (Flask-Migrate).
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)

