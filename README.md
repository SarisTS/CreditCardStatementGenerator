# Public Bank Credit Card Statement Generator
This project is a full-stack web application that generates PDF credit card statements for customers using Django (backend) and React (frontend).

## Features
  - Generate PDF statements for customers
  - Multi-language support (10 popular languages)
  - Real-time data fetch from database
  - Styled, bank-like PDF format
  - Responsive frontend using React


## Tech Stack

 - **Frontend:** React, Bootstrap
 - **Backend:** Django REST Framework, WeasyPrint
 - **Database:** SQLite (for submission)


## How to Run
### Backend:
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 
```
---

### Frontend:
```bash
cd frontend
npm install
npm start
```
---

### Sample API
Visit http://localhost:8000/api/generate-statement/?customer_id=1001&language=en

---

### Sample Credentials (for demo)
Customer ID: 1
Supported Languages: English, Tamil, Hindi, Arabic, French, Malay, Chinese, German, Japanese, Spanish

---


### Developer

**Name:** Sarish T. S  
**Email:** mohamedsaris17@gmail.com