from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/ideas')
def ideas():
    return render_template('ideas.html')

@views.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)