# Agile Web Development - CITS3403 - Project 1 

![Numberloo Screen](https://i.imgur.com/hgu68tL.png)

## Students
- Jennifer Nguyen 22757325
- Carmen Leong 22789943
- Dongwoo Noh 22999339
- Hari Vignesh 22874425


## 1. Purpose of the Web Application
- Numberloo is a daily puzzle game which aims to test users mathematic skills, as well as provide them with a source of entertainment 
- The game is short enough to keep users entertained, but also fairly challenging to give users a sense of achievement after every game
- Numberloo reward system includes a collection of plants. Based on the time taken to solve the puzzle, users are rewarded with a plant which they can add to their mini garden/collection. We designed with the environment in mind. 
    - We want to constantly remind users of the beautiful nature around them.
    - This reward system aims to encourage users to play the game daily and grow their collection

## 2. Design of Numberloo

### Registration Page
- First time Numberloo users have the option to register their account on our game
- There is no requirements on the length of password or username, as we want the process of logging in and registering to be as smooth and easy as possible
- Once the user set up a unique username and a password, this data will be sent to our server database. The user will be redirected to the sign in page

![Numberloo Registration Screen](https://i.imgur.com/Huwfikx.png)

### Sign In Page
- The sign in form is short and easy to fill in. Plus users can use remember me option so that they do not have to sign in everytime they play the game, which is usually the main reason deterring users from playing games
- Our game has validators in place to make sure that only the correct and registered account is allowed access

![Numberloo Sign In Screen](https://i.imgur.com/b4ZOoEk.png)

### Game Page
The design, colour scheme and layout of this game follows [Google Material Design's design guideline](https://material.io/design/color/dark-theme.html) to ensure that our webpage is visually appealing to users, which is an important aspect of web development. 

We also try to keep the design *clean and minimal* for a seamless user experience. The chosen font is Arial and Helvetical, which has the highest compatibility on both Windows and Mac system.

1. **Left Hand Menu**
    - How To Play Modal: This modal **provide instructions** on how to play the game, with visual demonstration in place
    - Log out Button: This option provides users the **flexibility of using different accounts**, e.g. when their friends want to log in and play on their phones. Compared to Wordle, this option means that users do not have to keep playing Numberloo in the same device, saving the hassle.

2. **Right Hand Menu**
    - Settings Modal: This modal allows users to change their **preference of light settings**: light mode or dark mode. The game uses local storage to remember users preference. This lighting mode was added because dark mode has been so popular nowadays
    - Statistics Modal: This modal displays the **global statistics, as well as users personal statistics**, using data fetched from the server. This ensures the data cannot be tampered (compared with the option of using local storage). The modal also includes users' **personal plant collection** which they can show off to their friends via our sharing mechanism (clipboard API). There is also a countdown to inform users when the next game starts

3. **Main Game**
    - There is a **START** button in the middle of the page to prompt users to start. Once they click start, the timer will start counting. The game uses drag and drop mechanism.
    - Once the game finishes, or the time limit exceeds, the statistics will be automatically sent to the server and updated on the front end.

4. **Assessment Mechanism**
    - Users have to find the right combination of numbers for an equation that makes up to given target
    - The time taken to play the puzzle will be recorded and users will be rewarded accordingly. Their winning percentage, current streak and best streaks will also be calculated.
    - If users skip a day, their current streak will not be reset, since we believe this may deter users from coming back.
    - Once the game is played, the system will have users' record and prevent them from refreshing the page/playing again. They can only play again the next day.


## 3. Architecture of the Web Application
The Architecture of this Web Application is represented below
```zsh
Numberloo Project
├── README.md
├── app.db
├── config.py
├── numberloo.py
├── requirements.txt
├── addQuiz.py
├── vetQuiz.py
├── tests-backend.py
├── tests-frontend.txt
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
└── migrations
    ├── alembic.ini
    ├── env.py
    └── script.py.mako

```

## 4. Prerequisite
This application requires python3, venv, and sqlite

1. **Install venv**
    - Use pip or another package manager to install virtualenv package `pip install venv`
2. **Install sqlite**
    - For Windows: [Windows instructions](http://www.sqlitetutorial.net/download-install-sqlite/)
    - For Linux: `sudo apt-get install sqlite`

## 5. How to launch the application

1. **Virtual environment**
    - Activate python virtual environment `$ python -m venv venv` followed by `$ source venv/bin/activate` 

2. **Run the app**
    - Use pip or pip3 to install all the required packages
    `pip install -r requirements.txt`
    - Run the application
    `flask run`

    You will see the following:
    ```
    * Serving Flask app 'numberloo.py' (lazy loading)
    * Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
    ```

    **This starts the apps running on local host at port 5000 http://127.0.0.1:5000 or http://localhost:5000**

    - If the web application cannot run, check the environment variable
    `FLASK_APP=numberloo.py` and store it
    - If you want to turn on debug mode, you can install python-dotenv package
    `pip install python-dotenv` and put `$ export FLASK_ENV=development`

## 6. About the database

The Web Application comes with an existing database named 'app.db, it contains several user accounts and around 200 quizes.

However, if you want to delete the existing database, and create it on your own, please apply the following commands:
1. delete the file 'app.db'
2. `flask db init`
3. `flask db migrate -m "users table"`
4. `flask db upgrade`

## 7. Testing

Application of both unit and selenium tests have been conducted to ensure our app is in bug free environment.
Running method of two tests are desccribed as below:

###### Unit test - Back end

Mainly testing updates of user's personal statistical attirubute such as streak count and achviement collections from database in a daily basis.

To run the test:
1. **Flask run in your terminal within desired local server**

```
flask run
```
2. **Open seperate terminal to run tests-backend.py**

```
python3 tests.py  ## type suitable python version installed in your device

```
3. **Check the outcome of the test as shown below**

```
test_hashig_pwd (__main__.UserModelCase) ... ok
test_update_streak (__main__.UserModelCase) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.737s

OK
```


###### Selenium test
Selenium test covers updates of user's account registration in the frontend.
Running Selenium test is similar to method mentioned above.

1. **Flask run in your terminal within desired local server**

```
flask run
```
2. **Open seperate terminal to run tests-frontend.py**

```
python3 tests-frontend.py  ## type suitable python version installed in your device

```


## 8. Adding & Vetting puzzles

To add puzzles, run the following command , this will automatically add new quiz(es) to the quiz table in the databse. Replace <quizNum> with the number of quiz to add, if unspecified, default to 1.
```
python3 addQuiz.py <quizNum>
```
    
To vet quizes, run the following command, it will print all the quizes stored in the database
```
pyhton3 vetQuiz.py
```
    
## 9. Commit Log
    
As in the attached git.log.txt 


## 10. Acknowledgement

Following teaching references and instructions were used for Agiles project :

* Application of lecture slides and Workshop from Dr.Tim French and Thomas Smoker - https://teaching.csse.uwa.edu.au/units/CITS3403/
* Flask Application Mega-Tutorial by Miguel Grinberg  -  https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
