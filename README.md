# Django Application Setup Guide

This guide provides step-by-step instructions to set up and run the Django application in a virtual environment.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-project-directory>
```

---

## 🐍 Set Up Virtual Environment

### Linux/macOS

```bash
python3 -m venv myvenv
source myvenv/bin/activate
```

### Windows

```bash
python -m venv myvenv
myvenv\Scripts\activate
```

---

## 📆 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 💠 Run Migrations (if needed)

```bash
python manage.py migrate
```

---

## ▶️ Run the Application

```bash
python manage.py runserver 0.0.0.0:8000
```

The app will be available at: [http://localhost:8000](http://localhost:8000)

---

## ✅ Deactivate the Environment (after use)

```bash
deactivate
```

---

## 📝 Notes

- Make sure Python 3 is installed.
- If you use `.env` for secrets, create one before running the server.

