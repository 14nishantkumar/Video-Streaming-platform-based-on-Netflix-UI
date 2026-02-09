# 🎬 Netflix Clone (Django)

A Netflix-inspired video streaming web application built using **Django, SQLite, HTML, CSS, and JavaScript**.  
The project includes **user authentication, multiple profile management, and dynamic movie browsing** with a responsive dark-themed UI.

---

## 🚀 Features

- 🔐 User authentication (Login / Signup / Logout) using **Django Allauth**
- 👤 Multiple **profiles per user** (Kids & Adult support)
- 🎥 Movie listing and **movie detail page**
- 🖼 Dynamic posters, overview, and trailer integration
- 🌙 Netflix-style **dark responsive UI**
- 🧭 Secure routing using **profile UUID**
- 🗄 SQLite database integration
- 🔌 Ready for **TMDB API integration**

---

## 🛠 Tech Stack

**Backend**
- Django
- SQLite

**Frontend**
- HTML
- CSS
- JavaScript

**Libraries**
- django-allauth
- requests
- python-dotenv
- pillow

---

## ⚙️ Installation & Setup
### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/netflix-clone-django.git
cd netflix-clone-django
```

## 2️⃣ Create virtual environment
```bash
python -m venv myworld
```
##3️⃣ Activate virtual environment
**Windows**
```bash
myworld\Scripts\activate
```
**Mac/Linux**
``` bash
source myworld/bin/activate
```
##4️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
##5️⃣ Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
##6️⃣ Start development server
```bash
python manage.py runserver
```
## Open in browser:
```bash
http://127.0.0.1:8000
```
---
## 📸 Screenshots (Add Later)

### Signup Page
![Home](Screenshots/Signup_page.PNG)

### Login Page
![Login](Screenshots/Login_page.PNG)

### Profile Selection
![Profile](Screenshots/Profiles.PNG)

---
## 📈 Future Improvements

- ▶ Video streaming player

- ❤️ Watchlist feature

- ⏳ Continue watching section

- 🌐 Full TMDB API auto-sync

- ☁ Deployment (Render / AWS)
