# 🎓 Student Study Portal

A full-stack web application built using **HTML**, **CSS**, **Python**, **Django**, and **SQL** that enables students to manage and track their study resources efficiently. The portal includes features like user authentication, CRUD operations, and external data fetching using APIs.

---

## 🔍 About the Project

The **Student Study Portal** is designed to help students manage their study materials, explore additional learning resources via integrated APIs, and stay organized. With a simple and clean interface, users can register, log in, add/update/delete their study content, and access related YouTube videos and Wikipedia content — all within a unified platform.

---

## 🚀 Features

- ✅ **User Authentication**
  - Register / Signup
  - Login / Logout

- 📝 **CRUD Operations**
  - Create, Read, Update, Delete study resources

- 🔗 **API Integrations**
  - Fetch relevant Wikipedia content
  - Search YouTube videos using `youtube-search-python`

- 💡 **Responsive UI**
  - Built with HTML and CSS using Django templates and Crispy Forms

---

## 🛠️ Tech Stack

| Category            | Technologies / Packages Used                  |
|---------------------|-----------------------------------------------|
| 💻 Frontend         | HTML, CSS                                     |
| 🧠 Backend          | Python, Django                                |
| 🗃️ Database         | SQLite (Django default)                       |
| 🔐 Authentication   | Django Authentication System                  |
| 📦 Python Packages  | 
|                     | `virtualenv` – For isolated development env   |
|                     | `wikipedia` – For fetching content            |
|                     | `youtube-search-python` – YouTube video API   |
|                     | `crispy-forms` – To enhance form design       |

---

## 📂 Project Structure
student_study_portal/
├── manage.py
├── db.sqlite3
├── requirements.txt
├── templates/
│ ├── base.html
│ ├── home.html
│ ├── login.html
│ └── register.html
├── static/
│ ├── css/
│ └── js/
├── study/
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── forms.py
└── student_study_portal/
├── settings.py
├── urls.py
└── wsgi.py

## 🔧 Setup Instructions

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/student_study_portal.git
cd student_study_portal

2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies
pip install django wikipedia youtube-search-python django-crispy-forms

4. Run Migrations
python manage.py makemigrations
python manage.py migrate

5. Create Superuser (Optional)
python manage.py createsuperuser

6. Start the Development Server
python manage.py runserver
pip install -r requirements.txt

