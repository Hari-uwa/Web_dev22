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
- First time Numberloo users have the option the register their account on our game
- There is no requirements on the length of password or username, as we want the process of logging in and registering to be as smooth and easy as possible
- Once the user set up a unique username and a password, this data will be sent to our server database. The user will be redirected to the sign in page

![Numberloo Registration Screen](https://i.imgur.com/Huwfikx.png)

### Sign In Page
- The sign in form is short and easy to fill in. Plus users can use remember me option so that they do not have to sign in everytime they play the game, which is usually the main reason deterring users from playing games
- Our game has validators in place to make sure that only the correct and registered account is allowed access

![Numberloo Sign In Screen](https://i.imgur.com/b4ZOoEk.png)

### Game Page
The design, colour scheme and layout of this game follows [Google Material Design's design guideline](https://material.io/design/color/dark-theme.html) to ensure that our webpage is visually appealing to users, which is an important aspect of web development. 

We also try to keep the design *clean and minimal* for a seamless user experience.

1. Left Hand Menu
    - How To Play Modal: This modal **provide instructions** on how to play the game, with visual demonstration in place
    - Log out Button: This option provides users the **flexibility of using different accounts**, e.g. when their friends want to log in and play on their phones. Compared to Wordle, this option means that users do not have to keep playing Numberloo in the same device, saving the hassle.

2. Right Hand Menu
    - Settings Modal: This modal allows users to change their **preference of light settings**: light mode or dark mode. The game uses local storage to remember users preference. This lighting mode was added because dark mode has been so popular nowadays
    - Statistics Modal: This modal displays the **global statistics, as well as users personal statistics**, using data fetched from the server. This ensures the data cannot be tampered (compared with the option of using local storage). The modal also includes users' **personal plant collection** which they can show off to their friends via our sharing mechanism (clipboard API). There is also a countdown to inform users when the next game starts

3. Main Game
    - There is a **START** button in the middle of the page to prompt users to start. Once they click start, the timer will start counting. The game uses drag and drop mechanism.
    - Once the game finishes, or the time limit exceeds, the statistics will be automatically sent to the server and updated on the front end.

4. Assessment Mechanism
    - Users have to find the right combination of numbers for an equation that makes up to given target
    - The time taken to play the puzzle will be recorded and users will be rewarded accordingly. Their win percentage, current streak and best streaks will also be calculated.
    - If users skip a day, their current streak will not be reset, since we believe this may deter users from coming back.
    - Once the game is played, the system will have users' record and prevent them from refreshing the page/playing again. They can only play again the next day.

## 3. Architecture of the Web Application


## 4. How to launch the application

1. Virtual environment

- Open your terminal and run the following commands:
- Use pip or pip3 to install all the required packages
`pip3 install -r requirements.txt`
- Run the application
`flask run`

- If the Web Application cannot run, check the environmental variable
`FLASK_APP=start.py`
and store it as environmental variable