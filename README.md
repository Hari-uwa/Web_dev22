# Agile Web Development - CITS3403 - Project 1 

![Numberloo Screen](https://i.imgur.com/hgu68tL.png)

## Students
- Jennifer Nguyen 22757325
- Carmen Leong 22789943
- Dongwoo Noh 22999339
- Hari Vignesh 22874425

## 1. Purpose
- The purpose of this project is to demonstrate fundamental skills of building a web page, from the front end, to back end
- This web application provides users with a daily mini puzzle game where they can play and enjoy during their break time

## 2. Architecture of the Web Application
The Architecture of this Web Application is represented below
```zsh
Numberloo Project
├── README.md
├── app.db
├── config.py
├── numberloo.py
├── requirements.txt
├── app
│   ├── __init__.py
│   ├── controllers.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
│   ├── static
│   │   ├── images
│   │   │   ├── images ...
│   │   ├── interactive.js
│   │   ├── script.js
│   │   └── style.css
│   └── templates
│       ├── login.html
│       ├── register.html
│       └── skeleton.html
├── notebooks
│   ├── Quiz_view_insert.ipynb
│   └── sql_queries_test.ipynb
└── test
    ├── Untitled.ipynb
    └── db_tests.ipynb
```

## 3. Assessment and Context mechanism

## 4. How to launch the application
- Open your terminal and run the following commands:
- Use pip or pip3 to install all the required packages
`pip3 install -r requirements.txt`
- Run the application
`flask run`

- If the Web Application cannot run, check the environmental variable
`FLASK_APP=start.py`
and store it as environmental variable

## 5. About the database
The Web Application comes with an existing database named 'app.db, it contains several user accounts.

However, if you want to delete the existing database, and create it on your own, please apply the following commands:
1. `delete the file 'app.db'`
2. `flask db init`
3. `flask db migrate -m "users table"`
4. `flask db upgrade`
5. `flask db migrate -m "posts table"`
6. `flask db upgrade`
