from flask import Flask, request, redirect, render_template, url_for
from models import db, Employer, Job, Candidate, Application
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create uploads folder if not exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db.init_app(app)

with app.app_context():
    db.create_all()
    # Add sample data if empty
    if Employer.query.count() == 0:
        emp = Employer(company_name="Google", email="hr@google.com", password="pass123")
        db.session.add(emp)
        db.session.commit()
        
        jobs = [
            Job(title="Software Engineer", description="Build amazing products", location="Remote", salary="$100k", category="Engineering", employer_id=1),
            Job(title="Data Analyst", description="Analyze data and create insights", location="New York", salary="$80k", category="Data", employer_id=1),
        ]
        for job in jobs:
            db.session.add(job)
        db.session.commit()

@app.route('/')
def index():
    jobs = Job.query.order_by(Job.posted_date.desc()).limit(6).all()
    return render_template('index.html', jobs=jobs)

# ========== JOB ROUTES ==========
@app.route('/jobs')
def jobs():
    category = request.args.get('category')
    location = request.args.get('location')
    query = Job.query
    
    if category:
        query = query.filter_by(category=category)
    if location:
        query = query.filter(Job.location.contains(location))
    
    jobs = query.all()
    return render_template('jobs.html', jobs=jobs, category=category, location=location)

@app.route('/job/<int:id>')
def job_detail(id):
    job = Job.query.get_or_404(id)
    return render_template('job_detail.html', job=job)

@app.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        location = request.form['location']
        salary = request.form['salary']
        category = request.form['category']
        employer_id = 1  # For demo, assuming employer with id=1
        
        job = Job(title=title, description=description, location=location, salary=salary, category=category, employer_id=employer_id)
        db.session.add(job)
        db.session.commit()
        return redirect('/jobs')
    
    return render_template('post_job.html')

@app.route('/search')
def search():
    keyword = request.args.get('q')
    jobs = Job.query.filter(Job.title.contains(keyword) | Job.description.contains(keyword)).all()
    return render_template('jobs.html', jobs=jobs)

# ========== APPLICATION ROUTES ==========
@app.route('/apply/<int:job_id>', methods=['GET', 'POST'])
def apply_job(job_id):
    job = Job.query.get_or_404(job_id)
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cover_letter = request.form['cover_letter']
        
        # Check if candidate exists
        candidate = Candidate.query.filter_by(email=email).first()
        if not candidate:
            candidate = Candidate(name=name, email=email, password="temp123")
            db.session.add(candidate)
            db.session.commit()
        
        # Save resume
        resume = request.files['resume']
        if resume:
            filename = f"{email}_{resume.filename}"
            resume.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            candidate.resume_filename = filename
            db.session.commit()
        
        # Create application
        application = Application(job_id=job.id, candidate_id=candidate.id, cover_letter=cover_letter, status="Pending")
        db.session.add(application)
        db.session.commit()
        
        return redirect(url_for('application_status', app_id=application.id))
    
    return render_template('apply_job.html', job=job)

@app.route('/application/<int:app_id>')
def application_status(app_id):
    app_obj = Application.query.get_or_404(app_id)
    return render_template('application_status.html', app=app_obj)

@app.route('/applications')
def applications():
    all_apps = Application.query.all()
    return render_template('applications.html', applications=all_apps)

@app.route('/update_status/<int:app_id>', methods=['POST'])
def update_status(app_id):
    app_obj = Application.query.get_or_404(app_id)
    new_status = request.form['status']
    app_obj.status = new_status
    db.session.commit()
    return redirect('/applications')

# ========== DASHBOARD ==========
@app.route('/dashboard')
def dashboard():
    total_jobs = Job.query.count()
    total_apps = Application.query.count()
    pending_apps = Application.query.filter_by(status="Pending").count()
    shortlisted_apps = Application.query.filter_by(status="Shortlisted").count()
    
    return render_template('dashboard.html', total_jobs=total_jobs, total_apps=total_apps, pending_apps=pending_apps, shortlisted_apps=shortlisted_apps)

if __name__ == '__main__':
    app.run(debug=True)