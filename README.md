# Acme Corp Portal - Realistic Vulnerable Web Application

This is a deliberately vulnerable web application designed to demonstrate real-world JWT (JSON Web Token) security issues. This lab is intended for educational purposes only.

## 🚀 Features

- Stateless JWT authentication (no Flask-Login)
- User registration and login
- Role-based access control (user/admin)
- Modern web interface
- Multiple JWT vulnerabilities (weak secret, alg:none, role escalation)
- Docker support for easy setup

## 🗂️ Project Structure

```
acmecorp/
    app.py
    config.py
    models.py
    auth.py
    user.py
    admin.py
    __init__.py
static/
templates/
requirements.txt
Dockerfile
README.md
```

## 🛠️ Setup Instructions

### Using Docker (Recommended)

1. Build the Docker image:
   ```bash
   docker build -t jwt-lab .
   ```
2. Run the container:
   ```bash
   docker run -p 5000:5000 jwt-lab
   ```

### Manual Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python -m acmecorp.app
   ```

The application will be available at `http://localhost:5000`

## 🔍 Learning Objectives

- Understand JWT authentication in stateless web apps
- Identify and exploit real-world JWT vulnerabilities
- Practice role escalation, algorithm confusion, and weak secret attacks

## ⚠️ Security Notice

This application is intentionally vulnerable and should only be used for educational purposes in a controlled environment. Do not deploy in production. 