# Student Management System — Django

A full-stack Student Management System built with Python and Django as part of a 9-day Python Django Workshop conducted by **Nischal Lamichhane**.

This project covers the complete Django development cycle — models, views, URLs, templates, CRUD operations, security, and authentication.

> Built on top of concepts learned in:
> 👉 [django-learning](https://github.com/saurab997/django-learning)

---

## Features

- [x] View all students in a responsive table
- [x] Create a new student record
- [x] Update existing student details
- [x] Delete a student record
- [x] Student detail view
- [x] User login and logout (authentication)
- [x] CSRF protection on all forms
- [x] Cookie-based access control
- [x] Navbar with active link highlighting
- [x] Responsive UI using Bootstrap 5
- [x] Template inheritance with base layout

---

## Project Structure

```
sms-django/
├── sms/                        # main Django project folder
│   ├── settings.py             # project configuration
│   ├── urls.py                 # main URL routing
│   └── wsgi.py
├── home/                       # student management app
│   ├── models.py               # Student model
│   ├── views.py                # CRUD view functions
│   ├── admin.py                # admin panel configuration
│   └── urls.py
├── accounts/                   # authentication app
│   ├── views.py                # login and logout views
│   └── urls.py
├── templates/
│   ├── base.html               # base layout (navbar + footer)
│   ├── index.html              # student list page
│   ├── create.html             # create student form
│   ├── update.html             # update student form
│   ├── detail.html             # student detail view
│   ├── accounts/
│   │   └── login.html          # login page
│   └── includes/
│       ├── navbar.html         # reusable navbar component
│       └── footer.html         # reusable footer component
├── .gitignore
├── manage.py
└── requirements.txt
```

---

## Key Concepts Learned and Applied

### CRUD Operations
Full Create, Read, Update, Delete functionality implemented
through Django view functions and connected to templates
via URL routing.

### CSRF Protection
Every form in the project uses `{% csrf_token %}` to prevent
Cross-Site Request Forgery attacks. Django rejects any POST
request that does not include a valid CSRF token.

### POST vs GET Handling
View functions check `request.method` to distinguish between
a user visiting a page (GET) and a user submitting a form (POST).
Delete and create operations only execute on POST requests.

### Redirect After POST
After every successful create, update, or delete operation,
the view redirects to the homepage instead of re-rendering
the template. This prevents form resubmission on page refresh
— an important security and UX practice.

### Cookie-Based Access Control
The index view sets a cookie (visited = True) when a user
visits the homepage. The create view checks for this cookie
before allowing access — users who skip the homepage are
blocked from directly accessing the create form.

### Template Inheritance
All pages extend a single base.html layout using:

    {% extends "base.html" %}
    {% block content %}
        page specific content here
    {% endblock content %}

This keeps HTML consistent across all pages without
repeating the navbar, footer, and Bootstrap imports.

### Template Includes
Reusable components (navbar and footer) are separated into
their own files and included where needed:

    {% include "includes/navbar.html" %}
    {% include "includes/footer.html" %}

### Active Navbar Link
The navbar uses a small JavaScript snippet to automatically
highlight the currently active page link by comparing each
nav link href to the current browser URL.

### Authentication
A separate accounts app handles user login and logout.
The navbar conditionally shows Login or Logout depending
on whether the user is authenticated:

    {% if not user.is_authenticated %}
        show Login
    {% else %}
        show Logout
    {% endif %}

### get_object_or_404
Used in update and delete views to safely fetch a student
by ID. If the ID does not exist in the database, Django
automatically returns a 404 page instead of crashing.

---

## Models

### Student
| Field | Type | Description |
|---|---|---|
| name | CharField | Student full name |
| age | PositiveSmallIntegerField | Student age |
| Class | CharField | Class or grade |
| roll | IntegerField | Roll number |

---

## URL Routes

| URL | View | Name | Description |
|---|---|---|---|
| `/` | index | home | List all students |
| `/create/` | create | create | Create new student |
| `/update/<id>/` | update | update | Update a student |
| `/delete/<id>/` | delete | delete | Delete a student |
| `/accounts/login/` | login | login | User login |
| `/accounts/logout/` | logout | logout | User logout |

---

## How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/saurab997/sms-django.git
cd sms-django

# 2. Create and activate virtual environment
py -m venv .venv
.venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
py manage.py migrate

# 5. Create a superuser
py manage.py createsuperuser

# 6. Run the development server
py manage.py runserver
```

Then open your browser at http://127.0.0.1:8000/

---

## Tech Stack

- Python 3
- Django
- SQLite (development database)
- Bootstrap 5 (UI)
- HTML / CSS / JavaScript

---

## Workshop Info

| Detail | Info |
| Instructor | Nischal Lamichhane |
| Duration | 9 Days |
| Topics | Frontend · Backend · FullStack |
| Project Days | Days 5 → 9 |

---

## Related Repository

Foundational Django concepts and Day 4-5 workshop notes:

👉 **[github.com/saurab997/django-learning](https://github.com/saurab997/django-learning)**
