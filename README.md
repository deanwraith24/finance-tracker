# Finance Tracker App

[Link to live project](https://finance-tracker-6cb04c9dae67.herokuapp.com/login/?next=/)

This is a simple income and expenses tracker that allows a user to start a private account and have multiple budgets stored.

### <u>Table of Contents</u>

* [Planning](#planning)
  * [External User Goals](#external-user-goals)
  * [Site Owner Goals](#site-owner-goals)
  * [User Stories](#user-stories)
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

#### <u>User Stories</u>
| User Story | Acceptance Criteria | Tasks |
|:-----------|:--------------------|-------|
| As a user, I can log an income entry so that I can track my earnings. | The user can enter the income amount, source, and date. The system saves the income entry to the database. The income appears in the income list and affects totals. | Create an income entry form. Implement form validation. Store income data in the database. Update totals after new income is logged. |
| As a user, I can log an expense entry so that I can monitor my spending. | The user can enter the expense amount, category, and date. The system saves the expense entry to the database. The expense appears in the expense list and affects totals. | Create an expense entry form. Implement form validation. Store expense data in the database. Update totals after new expense is logged. | 
| As a user, I can edit or delete income and expense entries so that I can correct mistakes or update my records. | The user can update an existing entry. The user can delete an entry, and the totals update accordingly. The system confirms before deleting an entry. | Implement edit functionality in the transaction list. Implement delete functionality with a confirmation prompt. Ensure total calculations update after edits or deletions. |
| As a user, I can see my total income and total expenses so that I can quickly assess my financial health. | The system calculates and displays total income and expenses. Totals update dynamically when entries are added, edited, or deleted. | Implement a function to calculate total income and expenses. Display totals on the dashboard. Ensure real-time updates when transactions change. |
| As a user, I can see my net balance so that I can understand my financial position. | The system calculates net balance (income minus expenses). The net balance updates dynamically with transactions. | Implement a function to calculate net balance. Display net balance on the dashboard. Ensure real-time updates when transactions change. |
| As a user, I can view a financial summary on a dashboard so that I can access key insights in one place. | The dashboard displays total income, total expenses, net balance, and visualizations. The data updates in real time when transactions change. | Design and implement the dashboard layout. Fetch and display key financial metrics. Integrate charts and totals into the dashboard. |
| As a user, I can access my finance tracker from desktop and mobile devices so that I can log transactions conveniently. | The system is responsive and works well on different screen sizes. All features are accessible on mobile devices. | Implement a responsive design. Test the interface on multiple devices. Optimize touch interactions for mobile users. |

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

| Feature | Expected | Testing | Result |
|:--------|:---------|:--------|:------:|
| Login button | When correct username and password entered, the user is redirected to the dashboard | Entered correct details for a registered user and clicked login button | Passed |
| Login button | When incorrect or non-registered username and password entered the user is not granted access and an error message is displayed | Entered incorrect details and tried logging in | Passed |
| Sign up | When the user clicks this they are redirected to a sign up page where they can register an account. | Clicked the link and registered a new account | Passed |
| Add new budget | When clicked the user is redirected to a page where they can create a new budget with its own individual name | Clicked button and created a new budget several times. | Passed |
| Back to dashboard button | This allows the user to return to the dashboard without creating a new budget. | Went to create new budget and clicked return to dashboard button | Passed |
| Delete selected budget button | This allows the user to select several budgets to delete if they no longer require them. If no budgets are selected an error message pops up | Tried deleting with nothing selected and message popped up. Selected several budgets and deleted them. | Passed |
| Log out button | Will log user out of dashboard if clicked. | Clicked and was returned to landing page. | Passed |
| Add Income / Add Expense | Both these when clicked will allow the user to add an expense or income. The user can give the input a label and an amount. When added it will update the pie chart. | Added several incomes and expenses. | Passed |
| Responsive elements | The app should adjust to all size screens and devices. | Tested across multiple phones, tablets and laptops. | Passed |

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

1. On the Heroku dashboard, select create app.
2. In the settings select Config Vars and add key. Add the Disable collect static key and designate it a value of 1.
3. In Visual Code Studio install the webserver using the pip3 install gunicorn~=20.1 command and freeze the to requirements.
4. Create a Procfile and include gunicorn project_name.wsgi in it.
5. Add herokuapp.com to the allowed hosts in the settings.py.
6. On the Heroku dashboard select deploy tab
7. Select connect to Github as the deployement method. Search for the repo and select the project repo.
8. Select deploy branch
9. Open app

### <u>Credits</u>

The walkthrough projects, W3Schools, Code Institute course work, Slack and Django documentation were used at different stages to work through problems.