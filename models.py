from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Employer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)  # In real app, use hashing
    jobs = db.relationship('Job', backref='employer', lazy=True)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.String(50))
    category = db.Column(db.String(50))
    posted_date = db.Column(db.DateTime, default=datetime.utcnow)
    employer_id = db.Column(db.Integer, db.ForeignKey('employer.id'))
    applications = db.relationship('Application', backref='job', lazy=True)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)  # In real app, use hashing
    resume_filename = db.Column(db.String(200))
    applications = db.relationship('Application', backref='candidate', lazy=True)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'))
    status = db.Column(db.String(20), default="Pending")  # Pending, Shortlisted, Rejected
    applied_date = db.Column(db.DateTime, default=datetime.utcnow)
    cover_letter = db.Column(db.Text)