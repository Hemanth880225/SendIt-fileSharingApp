# SendIt — Secure File Sharing & File Management System

**SendIt** is a **secure file sharing and file management web application** built using **Flask**.
It enables users to upload, organize, rename, and manage files securely through a structured dashboard.

This project demonstrates **real-world backend engineering concepts** including authentication, file handling, folder management, and clean architecture.

---

# 🚀 Project Overview

SendIt allows users to:

* Upload files securely
* Organize files into folders
* Rename files and folders
* Manage uploads
* View dashboard
* Manage profile

This project is designed using **modular Flask architecture** and **production-style project structure**.

---

# 🏗️ High-Level Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                         Client Layer                         │
│--------------------------------------------------------------│
│ Browser / Web UI                                             │
│ HTML | CSS | JavaScript | Bootstrap                          │
└───────────────────────────────┬──────────────────────────────┘
                                │ HTTP Requests
                                ▼
┌──────────────────────────────────────────────────────────────┐
│                      Flask Application                       │
│--------------------------------------------------------------│
│ Routes Layer                                                 │
│                                                              │
│ • Authentication Routes                                      │
│ • File Upload Routes                                         │
│ • Folder Management Routes                                   │
│ • Profile Routes                                             │
└───────────────────────────────┬──────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────┐
│                     Business Logic Layer                      │
│--------------------------------------------------------------│
│ Application Logic                                            │
│                                                              │
│ • File Upload Logic                                          │
│ • Folder Organization                                        │
│ • File Rename Logic                                          │
│ • User Management                                            │
└───────────────────────────────┬──────────────────────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────────────────┐
│                         Data Layer                           │
│--------------------------------------------------------------│
│ SQLAlchemy Models                                            │
│ SQLite Database                                              │
└──────────────────────────────────────────────────────────────┘
```

---

# 📂 Project Structure

```
sendit
│
├── static
│   ├── css
│   │   └── style.css
│   ├── js
│   │   └── main.js
│   ├── profile_pics
│   └── uploads
│
├── templates
│   ├── account.html
│   ├── base.html
│   ├── folders.html
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── rename_file.html
│   ├── rename_folder.html
│   ├── update.html
│   ├── upload.html
│   ├── uploads.html
│   └── uploads_by_folder.html
│
├── __init__.py
├── config.py
├── forms.py
├── models.py
├── routes.py
│
└── README.md
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

# Authentication

* User Registration
* User Login
* User Profile

---

# File Management

* Upload files
* Rename files
* Delete files
* Organize files

---

# Folder Management

* Create folders
* Rename folders
* Organize uploads

---

# Dashboard

* View uploaded files
* View folders
* Manage files

---

# 🧠 Application Flow

```
User Login/Register
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

| Field      | Type    |
| ---------- | ------- |
| id         | Integer |
| username   | String  |
| email      | String  |
| password   | String  |
| image_file | String  |

---

## File Table

| Field     | Type       |
| --------- | ---------- |
| id        | Integer    |
| filename  | String     |
| filepath  | String     |
| user_id   | ForeignKey |
| folder_id | ForeignKey |

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
* Secure uploads
* Folder isolation

---

# 🚀 Installation

Clone repository

```
git clone https://github.com/Hemanth880225/SendIt.git
```

Navigate

```
cd SendIt
```

Create virtual environment

```
python -m venv venv
```

Activate

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
python run.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🧪 Learning Outcomes

This project demonstrates:

* Flask architecture
* File handling
* User authentication
* Database relationships
* Dashboard design
* Full-stack Flask development

---

# 🔮 Future Improvements

* Expiring file links
* File sharing links
* Drag and drop uploads
* Cloud storage integration
* File preview support
* Download analytics

---

# ⭐ Resume Description

**SendIt — Secure File Sharing System**
Built a secure file sharing system using Flask with authentication, file upload system, folder organization, and dashboard interface. Designed modular architecture and implemented SQLAlchemy database relationships.

---

# 👨‍💻 Author

Hemanth
Backend Developer
Python | Flask | System Design

---

# 📄 License

MIT License

---
