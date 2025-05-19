from flask import Flask, render_template, redirect, url_for, request, make_response
from .config import Config
from .models import db
from .auth import bp as auth_bp
from .user import bp as user_bp
from .admin import bp as admin_bp
import os
import jwt

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# Ensure instance directory exists
os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance'), exist_ok=True)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)

@app.context_processor
def inject_current_role():
    token = request.cookies.get('token')
    role = None
    is_authenticated = False
    if token:
        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM], options={"verify_signature": False})
            role = payload.get('role')
            if payload.get('user_id') and payload.get('username'):
                is_authenticated = True
        except Exception:
            pass
    return dict(current_role=role, is_authenticated=is_authenticated)

@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.delete_cookie('token')
    return resp

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/robots.txt')
def robots():
    return 'User-agent: *\nDisallow: /admin-backup-2023/', 200, {'Content-Type': 'text/plain'}

@app.route('/admin-backup-2023/flag.txt')
def admin_backup_flag():
    return '...or maybe not', 200, {'Content-Type': 'text/plain'}

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0') 