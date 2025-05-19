import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, 'instance')
os.makedirs(INSTANCE_DIR, exist_ok=True)

class Config:
    SECRET_KEY = os.environ.get('JWTLAB_SECRET_KEY', 'supersecret')  # Weak key for lab
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(INSTANCE_DIR, 'users.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ALGORITHM = 'HS256'
    JWT_ISSUER = 'jwt-lab-app' 