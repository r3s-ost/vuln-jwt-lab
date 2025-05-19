from flask import Blueprint, request, render_template, redirect, url_for
import jwt
from .config import Config
from .user import get_jwt_payload

bp = Blueprint('admin', __name__)

@bp.route('/admin')
def admin():
    payload = get_jwt_payload()
    if not payload:
        return redirect(url_for('auth.login'))
    if payload.get('role') == 'admin':
        return render_template('admin.html', user=payload)
    return render_template('403.html'), 403 