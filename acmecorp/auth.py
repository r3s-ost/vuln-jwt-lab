from flask import Blueprint, request, jsonify, render_template, redirect, url_for, make_response
from .models import db, User
import jwt
import datetime
from .config import Config
import re

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return render_template('register.html', error='Username and password required')
        if not re.match(r'^[A-Za-z0-9]{8,}$', password):
            return render_template('register.html', error='Password must be at least 8 alphanumeric characters')
        if User.query.filter_by(username=username).first():
            return render_template('register.html', error='Username already exists')
        user = User(username=username, role='user')
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            token = generate_token(user)
            resp = make_response(redirect(url_for('user.dashboard')))
            resp.set_cookie('token', token, httponly=False, samesite='Lax')
            return resp
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

def generate_token(user):
    payload = {
        'user_id': user.id,
        'username': user.username,
        'role': user.role,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'iss': Config.JWT_ISSUER
    }
    # Intentionally weak secret and vulnerable algorithm handling
    return jwt.encode(payload, Config.SECRET_KEY, algorithm=Config.JWT_ALGORITHM) 