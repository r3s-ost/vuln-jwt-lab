from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from .models import User
import jwt
from .config import Config
from functools import wraps

def get_jwt_payload():
    token = request.cookies.get('token')
    if not token:
        return None
    try:
        # Only accept tokens with a valid structure and required claims
        payload = jwt.decode(token, Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM], options={"verify_signature": False})
        if not payload or not payload.get('user_id') or not payload.get('username') or not payload.get('role'):
            return None
        return payload
    except Exception:
        return None

def jwt_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        payload = get_jwt_payload()
        if not payload:
            return redirect(url_for('auth.login'))
        return f(payload, *args, **kwargs)
    return decorated

bp = Blueprint('user', __name__)

@bp.route('/dashboard')
@jwt_required
def dashboard(payload):
    user = User.query.filter_by(id=payload.get('user_id')).first()
    if not user:
        return redirect(url_for('auth.login'))
    return render_template('dashboard.html', user=user, jwt_token=request.cookies.get('token'))

@bp.route('/api/user')
@jwt_required
def api_user(payload):
    return jsonify(payload) 