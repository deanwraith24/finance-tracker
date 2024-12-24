# Finance Tracker App

[Link to live project](https://finance-tracker-6cb04c9dae67.herokuapp.com/login/?next=/)

This is a simple income and expenses tracker that allows a user to start a private account and have multiple budgets stored.

### <u>Table of Contents</u>

* [Planning](#planning)
  * [External User Goals](#external-user-goals)
  * [Site Owner Goals](#site-owner-goals)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [Log-in Page](#log-in-page)
  * [Sign-up Page](#sign-up-page)
  * [Dashboard](#dashboard)
  * [Budget Detail Page](#budget-detail-page)
  * [Add Income Page](#add-income-page)
  * [Add Expense Page](#add-expense-page)

* [Future Enhancements](#future-enhancements)

* [Testing](#testing)
  * [Manual Testing](#manual-testing)
  * [Validation](#validation)
  * [Issues](#issues)

* [Deployement](#deployement)

* [Credits](#credits)

### <u>Planning</u>

#### <u>External User Goals</u>
The external user will be able to set up various budgets with different end goals whether that be a monthly tracker, a vacation budget or a savings term. The user can add expenses and incomes and have a numerical representation of the totals as well as a graphical representation.

#### <u>Site Owner Goals</u>
The site owner wanted a space where users could start a unique account where they could have multiple budgets stored and used.

#### <u>Wireframes</u>

![Dashboard Wireframe](https:)

![Budget Detail Wireframe](https:)

### <u>Features</u>

#### <u>Log-In Page</u>

The landing page has the game title at the top and then the rules of the game listed below.

Below the rules is a button that allows the player to start the game when they have read the rules and are ready to start.

![Log-In Page]()

#### <u>Sign-Up Page</u>

When the player clicks the start game button on the landing page they are directed to the game page. On the game page the title at the top of the page is a link that will redirect to the landing page if the user wants to read the rules again. 

Below that is the question the user needs to answer. The questions are randomly selected from a collection of 50 questions and are not repeated in a single game.

There is then a section for the user to input a guess. It reminds the player the number needs to be between 0 and 100. 

Then there is the submit guess button. If the button is clicked and the input field is empty an error messgae will appear prompting the player to input a guess. When the guess is input and the submit button is clicked the answer to the question is displayed, the score is updated and the submit button is disabled so it can't be clicked more than once. There is also a next question button that appears so the user can move forward in the game. 

There is a score counter that updates depending on the players answer. It is updated by adding the difference between the users guess and the correct answer. There is also a question counter to show the player their progress. 

When the player answers the final question the next question button changes to end game. When clicked the screen changes to show the players final score and gives them the option to play again.

![Sign-Up Page](https://github.com/deanwraith24/triviagame/blob/main/assets/images/game_page.jpg)

#### <u>Dashboard</u>

The landing page has the game title at the top and then the rules of the game listed below.

Below the rules is a button that allows the player to start the game when they have read the rules and are ready to start.

![Dashboard]()

#### <u>Budget Detail Page</u>

The landing page has the game title at the top and then the rules of the game listed below.

Below the rules is a button that allows the player to start the game when they have read the rules and are ready to start.

![Budget Detail Page]()

#### <u>Add Income Page</u>

The landing page has the game title at the top and then the rules of the game listed below.

Below the rules is a button that allows the player to start the game when they have read the rules and are ready to start.

![Add Income Page]()

#### <u>Add Expense Page</u>

The landing page has the game title at the top and then the rules of the game listed below.

Below the rules is a button that allows the player to start the game when they have read the rules and are ready to start.

![Add Expense Page]()

### <u>Future Enhancements</u>

The list below is some features that could be added in the future to enhance the user experience.

* Score Board
A score board could be added so that players can keep track of their top 5 scores and track their progress.

* Question Timer
A timer could be added that could either be used for the whole game or each question that could make the game more difficult.

* Categories and Difficulty
Questions could be seperated into specific categories and players could have a selection menu where they can select different categories and difficulty levels to challenge themselves.

### <u>Testing</u>

#### <u>Manual Testing</u>

I tested the game myself and also sent it to famliy and friends to play on various devices and to send feedback.

#### <u>Validation</u>
 * HTML
 For the HTML I used W3C Markup Validation Service.

 * CSS
 For the validation of the CSS I used Jigsaw CSS validatior.

 * JS
 For the validation of the CSS I used Code Beautyify JS validatior.

#### <u>Issues</u>

Some of the issues that were encountered and then corrected during the testing are listed below, 

* Initially there was no way to return to the landing page, so the heading was turned into a link to allow this if users wanted to read the rules again.

* The submit button could be clicked more than once which would lead to the score being updated on each click, so the code was updated to disable the submit button after it has been clicked once and then be reset when the new question is loaded.

* The submit button was being displayed in the final score screen which was corrected by hiding it.

### <u>Deployement</u>

The project was deployed using GitHub Pages. The steps to deploy are as follows:

 1. Open the repository and click on the settings tab.
 2. Navigate to the Pages tab in the menu on the left.
 3. Choose deploy from a branch and select main branch.
 4. Click save and you can access the deployed website from the Pages tab.

### <u>Credits</u>

The idea for the game from a card game I have played before. The questions and answers came from the game and I selected the more general questions to be used. 

The course work and W3 Schools were helpful in developing the functions that allow the game to work.