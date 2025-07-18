# Finance Tracker 💸

A simple and clean personal finance dashboard built with Django, allowing users to track income and expenses with ease.

## ✨ Features

- Add financial transactions (income or expense)
- Specify amount, description, category, and date
- Summary of total income, expenses, and balance
- View recent transactions in a styled table
- Responsive UI with Bootstrap (RTL support)
- Modal form for smooth transaction input

## 🖼️ UI Preview

> `![Dashboard](static/images/dashboard.png)`

---

## ⚙️ Getting Started

1. Clone the repository:
```bash
git clone https://github.com/mhsangestani/finance_tracker.git
cd finance_tracker
Create a virtual environment and install dependencies:

bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Apply database migrations:

bash
Copy
Edit
python manage.py migrate
Run the development server:

bash
Copy
Edit
python manage.py runserver
Visit http://127.0.0.1:8000 to use the application.

📁 Project Structure
finance_tracker/
├── core/                 # Django project settings
├── transactions/         # Main app: models, views, forms
│   ├── migrations/
│   ├── templatetags/
├── templates/            # HTML templates
├── static/css/           # Custom styles
├── requirements.txt
└── manage.py
🧰 Tech Stack
Tool / Library	Purpose
Django	Backend framework
Bootstrap 5	Frontend styling
SQLite	Database (default)
HTML + Jinja2	Templating (Django)

🛣️ Main Routes
/ → Main dashboard (list + summary)

add_transaction → POST route to save transaction from modal

🔧 Future Improvements
Add real delete/edit functionality for transactions

Filter and search capabilities by category/date

Multi-user support with login system

Deploy to Render, Railway, or Heroku

📄 License
This project is licensed under the MIT License. See LICENSE for details.

👤 Author
Name: mhsangestani

GitHub Profile
