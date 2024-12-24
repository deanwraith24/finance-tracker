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

![Dashboard Wireframe](https://github.com/deanwraith24/finance-tracker/blob/main/assets/images/dashboard.jpg)

![Budget Detail Wireframe](https://github.com/deanwraith24/finance-tracker/blob/main/assets/images/budget_detail.jpg)

### <u>Features</u>

#### <u>Log-In Page</u>

The login page allows users who have already registered an account to login into their account with their selected username and password.

It also allows new users to access the sign-up page.

![Log-In Page](https://github.com/deanwraith24/finance-tracker/blob/main/assets/images/login_page.jpg)

#### <u>Sign-Up Page</u>

The sign-up page allows new users to register an account. Users need to add a username, email and password to register an account. There are also instructions that describe how to select usernames and passwords.

![Sign-Up Page](https://github.com/deanwraith24/finance-tracker/blob/main/assets/images/sign_up_page.jpg)

#### <u>Dashboard</u>

The dashboard is where users can see a list of their budgets they have created.

It also gives users the ability to add new budgets and delete old budgets they no longer need.

Users can also logout of the app from this page.

![Dashboard](https://github.com/deanwraith24/finance-tracker/blob/main/assets/images/dashboard_real.jpg)

#### <u>Budget Detail Page</u>

This page shows details of the selected budget.

It shows a seperate list for each incomes and expenses and shows a summary with totals for each.

There is the ability to add a new income and expense.

There is also a pie chart that shows the relationship between incomes and expenses.

There is also a link to return to the dashboard.

![Budget Detail Page](https://github.com/deanwraith24/finance-tracker/blob/main/assets/images/budget_detail_top.jpg)

![Budget Detail Page](https://github.com/deanwraith24/finance-tracker/blob/main/assets/images/budget_detail_bottom.jpg)

#### <u>Add Income Page</u>

This page allows users to add various incomes with a description.

![Add Income Page](https://github.com/deanwraith24/finance-tracker/blob/main/assets/images/add_income.jpg)

#### <u>Add Expense Page</u>

This page allows users to add various expenses with a description.

![Add Expense Page](https://github.com/deanwraith24/finance-tracker/blob/main/assets/images/add_expense.jpg)

### <u>Testing</u>

#### <u>Manual Testing</u>

In manual testing I created accounts myself and went through all of the available features.

#### <u>Validation</u>
 * HTML
 For the HTML I used W3C Markup Validation Service.

 * CSS
 For the validation of the CSS I used Jigsaw CSS validatior.

 * JS
 For the validation of the CSS I used Code Beautyify JS validatior.

#### <u>Issues</u>

Some of the issues that were encountered and then corrected during the testing are listed below, 

* I realised there was no way to return to the dashboard from the budget detail page so a link was added to the budget detail page.

* There was no way to exit the add income/expense pages if the user did not want to add either. A cancel button was added.

### <u>Deployement</u>

The project was deployed using Heroku. The process was started at the beginning of the project and updated regularly.

### <u>Credits</u>

The walkthrough projects, W3Schools, Code Institute course work, Slack and Django documentation were used at different stages to work through problems.