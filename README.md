# 💰 Finance Tracker

A minimal yet effective personal finance dashboard built with Django. Track your income and expenses, view summaries, and manage your transactions in a clean, responsive UI.

## 🚀 Features

- Add income and expense transactions
- View summary: total income, expenses, and balance
- Responsive Bootstrap 5 UI with RTL (Persian) support
- Modal form for quick transaction input

## 🛠 Tech Stack

- **Backend**: Django + SQLite
- **Frontend**: HTML, Bootstrap 5, Jinja2
- **Other**: Custom Django template tags

## 📦 Installation

```bash
git clone https://github.com/mhsangestani/finance_tracker.git
cd finance_tracker
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
Then open http://127.0.0.1:8000 in your browser.

🧭 Project Structure

├── core/              # Project settings
├── transactions/      # App logic: models, views, forms
├── templates/         # HTML templates
├── static/            # CSS assets
├── manage.py


📈 Roadmap Ideas
Edit/delete transactions

Filter/search by date or category

User authentication (multi-user support)

Deployment to Render or Railway
