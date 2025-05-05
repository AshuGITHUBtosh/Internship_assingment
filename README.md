
# 📝 Task Manager

## Overview

The Task Manager is a web-based application built using Django. It allows users to create, update, delete, and view tasks. Each task includes a title, description, status, due date, remarks, and timestamps. The platform also supports user authentication to ensure that tasks are user-specific and secure.

---

## Database Design

### ER Diagram

```mermaid
erDiagram
    USER ||--o{ TASK : has
    TASK {
        int id
        varchar title
        text description
        date due_date
        varchar status
        text remarks
        datetime created_on
        datetime updated_on
    }
```

### Data Dictionary

| Field        | Type          | Description                        |
|--------------|---------------|------------------------------------|
| id           | AutoField     | Primary key                        |
| title        | CharField(200)| Title of the task                  |
| description  | TextField     | Detailed description of the task   |
| due_date     | DateField     | Deadline of the task               |
| status       | CharField(20) | Status: Pending, In Progress, Completed |
| remarks      | TextField     | Optional remarks                   |
| created_on   | DateTimeField | Auto timestamp on creation         |
| updated_on   | DateTimeField | Auto timestamp on update           |
| created_by   | ForeignKey(User) | Creator of the task             |
| updated_by   | ForeignKey(User) | Last editor of the task         |

### Indexes Used

By default, Django creates indexes for:
- Primary keys (`id`)
- Foreign keys (`created_by`, `updated_by`)
- Any field used in filtering or lookup (e.g., `status`, `title`)

### 2.1.3.2.4. Code First vs DB First

**Code First** approach is used with Django's ORM.

**Why?**  
It allows us to manage models using Python code, easily migrate schema changes using Django's built-in migration tools, and version control model changes effectively.

---

## Application Structure

### Project Folder Structure

```
taskmanager/
│
├── taskmanager/             # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── tasks/                   # App for task management
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── static/
│   │   └── tasks/
│   │       ├── form.css
│   │       └── styles.css
│   └── templates/
│       ├── base.html
│       ├── registration/
│       │   └── login.html
│       └── tasks/
│           ├── task_confirm_delete.html
│           ├── task_form.html
│           └── task_list.html
│
├── db.sqlite3
└── manage.py
```

### Rendering Strategy

**Standard MVC server-side rendering (MPA)** has been used.

**Reason:**  
Django's templating engine is powerful and integrates seamlessly with its ORM and views. For this project’s scale, MPA provides simplicity and rapid development.

---

## Frontend Structure

### Frontend Type Used

**Web-based frontend** using **HTML + CSS** (via Django Templates).

### Justification

A web frontend is easier to implement and deploy for MVPs. It allows easier access across platforms (desktop, mobile browsers) without the need for separate Android/iOS builds.

---

## Build and Install Instructions

### Environment & Dependencies

#### 🔧 Requirements:
- Python 3.10+
- Django 4.x
- SQLite (default)
- `pip` for managing Python packages

### Build / Compile Instructions

```bash
# Clone the repository
git clone https://github.com/AshuGITHUBtosh/Internship_assingment.git
cd taskmanager

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### Run / Install Instructions

```bash
# Create a superuser (optional but recommended)
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Open in browser:
# http://127.0.0.1:8000/
```
