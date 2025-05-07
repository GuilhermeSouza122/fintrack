from flask import render_template, redirect, url_for, request, flash
from app import app
import os

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard', methods=['POST', 'GET'])
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and file.filename.endswith('.csv'):
            filepath = os.path.join('uploads', file.filename)
            file.save(filepath)
            flash('File uploaded successfully!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Please upload a valid CSV file.', 'danger')
    return render_template('upload.html')
