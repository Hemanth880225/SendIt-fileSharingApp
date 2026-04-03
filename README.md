# SendIt — Secure File Sharing & Management System

**SendIt** is a **secure file sharing and file management web application** built using **Flask**.
It allows users to upload, organize, manage, and access files securely through a clean dashboard interface.

This project demonstrates **real-world backend development concepts** including authentication, file handling, folder organization, and structured application architecture.

---

# 🚀 Project Overview

SendIt enables users to:

* Upload files securely
* Organize files into folders
* Rename files and folders
* Manage uploaded content
* Access files through a dashboard

This project is designed as a **production-style file management backend** with clean architecture.

---

# 🏗️ High-Level Architecture

```
┌────────────────────────────────────────────────────┐
│                   Client Layer                     │
│----------------------------------------------------│
│ Browser / User Interface                           │
└───────────────────────────┬────────────────────────┘
                            │ HTTP Requests
                            ▼
┌────────────────────────────────────────────────────┐
│                 Flask Application                  │
│----------------------------------------------------│
│ Routes Layer                                       │
│                                                    │
│ • Authentication Routes                            │
│ • File Upload Routes                               │
│ • Folder Management Routes                         │
└───────────────────────────┬────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────┐
│                 Service Layer                      │
│----------------------------------------------------│
│ Business Logic                                     │
│                                                    │
│ • File Upload Logic                                │
│ • Folder Organization                              │
│ • File Rename                                      │
└───────────────────────────┬────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────┐
│                  Data Layer                        │
│----------------------------------------------------│
│ SQLAlchemy Models                                  │
│ SQLite Database                                    │
└────────────────────────────────────────────────────┘
```

---

# ⚙️ Tech Stack

## Backend

* Python
* Flask
* SQLAlchemy

## Frontend

* HTML
* CSS
* JavaScript
* Bootstrap

## Database

* SQLite

## Tools

* Git
* GitHub

---

# ✨ Features

## Authentication System

* User Registration
* User Login
* Session-based authentication
* Secure user access

---

## File Management

* Upload files
* Rename files
* Delete files
* Download files

---

## Folder Management

* Create folders
* Rename folders
* Organize files into folders

---

## Dashboard

* Organized file view
* Folder navigation
* User-specific files

---

# 📂 Project Structure

```
SendIt
│
├── static/           # CSS, JS, Images
├── templates/        # HTML templates
├── models.py         # Database models
├── routes.py         # Flask routes
├── app.py / run.py   # Entry point
└── uploads/          # Uploaded files
```

---

# 🧠 Application Flow

```
User Registers / Login
        ↓
Access Dashboard
        ↓
Upload Files
        ↓
Organize into Folders
        ↓
Manage Files
```

---

# 🗄️ Database Design

## User Table

| Field    | Type    |
| -------- | ------- |
| id       | Integer |
| username | String  |
| email    | String  |
| password | String  |

---

## File Table

| Field      | Type       |
| ---------- | ---------- |
| id         | Integer    |
| filename   | String     |
| filepath   | String     |
| user_id    | ForeignKey |
| created_at | DateTime   |

---

## Folder Table

| Field       | Type       |
| ----------- | ---------- |
| id          | Integer    |
| folder_name | String     |
| user_id     | ForeignKey |

---

# 🔐 Security Features

* User authentication
* User-specific file access
* Secure file upload handling

---

# 🚀 Installation

Clone repository

```
git clone https://github.com/Hemanth880225/SendIt.git
```

Navigate to project

```
cd SendIt
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run application

```
python app.py
```

Open in browser

```
http://127.0.0.1:5000
```

---

# 🧪 Learning Outcomes

This project demonstrates:

* File handling in Flask
* User authentication
* Database relationships
* Folder organization logic
* Dashboard UI design
* Full-stack Flask development

---

# 🔮 Future Improvements

* Expiring file links
* Shareable file URLs
* File download analytics
* Cloud storage integration
* Drag and drop uploads
* File preview support

---

# ⭐ Resume Description

**SendIt — Secure File Sharing System**
Built a secure file sharing application using Flask with authentication, file upload system, folder organization, and dashboard interface. Implemented database relationships using SQLAlchemy and designed clean project architecture.

---

# 👨‍💻 Author

Hemanth
Python | Flask | Backend Development

---

# 📄 License

MIT License

---
