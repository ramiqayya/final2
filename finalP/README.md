# CapStone
## Distinctiveness and Complexity

The goal of this project was to create a comprehensive cryptocurrency trading platform using real-time data from the coinmarketcap.com API. Unlike other trading platforms, this project allows users to make deposits, withdrawals, and trades using a variety of cryptocurrencies, providing a seamless and user-friendly experience.

To accomplish this, I used a combination of technologies, including Django, CSS, Bootstrap, HTML, and JavaScript. I also integrated multiple APIs to gather real-time data on cryptocurrency prices, ensuring that users have the most up-to-date information when making trades.

One of the most complex aspects of this project was designing and implementing the portfolio and wallet system. Each user has a unique portfolio where they can store their deposited funds and track their trading history. When a user buys a particular cryptocurrency, the project automatically creates a new wallet for that currency, allowing the user to store and trade it independently from other currencies.

Overall, this project represents a significant achievement in the field of cryptocurrency trading platforms, and I am proud to have been able to create such a comprehensive and innovative tool using my skills in web development and API integration.



## Files:


*in myapp folder I modified the following files:*
### urls.py

This file contains the URL patterns for your website. These patterns define how your website's views are mapped to specific URLs.

### views.py 

This file contains the backend logic for your website. It includes several functions, such as:

* register(): Renders the register page where a new user can be added to the database.
* login_view(): Renders the login page where an existing user can log in.
* logout_view(): Renders the logout page where a user can log out after being signed in.
* portfolio(): Renders the user's portfolio page, where they can deposit or withdraw money and view all their wallets.
* sell(): Renders the sell page where the user can enter the amount of coins they want to sell, checks the current price of the coin, and sells it, adding the money to their main balance in the portfolio.
* trade(): Renders the trade page where the user can enter the symbol of a cryptocurrency, check its current price, and proceed to the buy page.
* buy(): Checks the user's available balance and lets them buy a new coin with a new wallet or add coins to an existing wallet.
* lookup(): Sends a request to an API with a coin symbol and returns the data for that coin.


### models.py

This file includes three models:

* User: Creates a new user.
* Wallet: Creates a new wallet.
* CoinsAmount: Adds the amount of coins to each wallet.

## Templates
*You have several templates in your templates/myapp folder. Here is a brief description of each:*

### register.html: Contains the form for registering a new user.
### login.html: Contains the login form.
### index.html: The main page, displaying a table of the top 10 coins.
### portfolio.html: Displays the user's portfolio, including their balance and a table of their wallets with each coin's current value.
### trade.html: Contains a form for entering the symbol of a cryptocurrency, displaying its current price, and allowing the user to proceed to the buy page.
### sell.html: Displays a form for entering the amount of coins the user wants to sell.
### error.html: Displays error codes and messages.
### layout.html: A template for the layout of all pages, including the navbar and any other views that appear on all pages.

## Static files
*Your static/myapp folder includes the following files:*

* styles.css: Defines some of the styles used on the website.
* app.js: Contains JavaScript code that adds dynamic styles to the website.

## How to Run the Application
To use this application, you need to follow these steps:

1. Register a new user by choosing "Register" at the top right corner of the homepage. Enter a unique username, email, password, and confirm password. Once you have registered, you can log in to the website anytime by choosing "Login."
2. The homepage displays a table of the top 10 cryptocurrencies by market capitalization.
3. To buy a new cryptocurrency, click on the "Trade" button in the navigation bar. This will open a new page with a title of "Price Query" and a text field asking for the coin symbol you want to enquire about. After entering the correct symbol for a coin and pressing "Check Price," the name of the coin, symbol, and price will appear at the bottom, along with a button asking if you would like to buy that coin. If you enter an incorrect symbol, the error page will appear with an error message.
4. If you choose to buy the coin, you will be redirected to the buy page. This page displays the current price of the coin and a field where you can enter the amount of that coin you would like to buy. However, you can't do anything without having a balance first.
5. To add money to your balance, go to the portfolio page by clicking on "Portfolio" in the navigation bar. This will open a new page showing your name and current balance. There are two fields: one for entering the amount of money you would like to deposit or withdraw and the other for choosing the transaction type (deposit or withdraw). To deposit money, enter the amount you would like to deposit, choose "Deposit," and then press the "Deposit/Withdraw" button. Now, you can use that balance to buy cryptocurrencies.
6. Once you have enough balance, go to the trade page and enter a valid symbol, then press "Buy." Enter the amount of that currency you would like to buy, and the total price of the amount will appear at the bottom of the field. If you have enough credit, press "Buy," and you will be redirected to the portfolio page, where a new wallet will appear at the table in the bottom of the page with the coin symbol, amount, and value in USD.
7. Please keep in mind that if you enter an amount of a coin with a total price greater than what you have in your portfolio, an error page will appear telling you that you do not have enough balance.
8. Try to buy several coins with the money you've deposited before. If you buy a new coin, it will appear in the portfolio with a new wallet with the coin symbol. On the other hand, if you buy an amount of a coin that you already have, that amount will be added to the amount you previously had in the same wallet.
9. To sell coins that you already have, go to the portfolio, and click on the "Sell" button next to the coin you want to sell. You will be sent to the sell page, where you can choose the amount that you would like to sell (not more than what you have and not less than 0). Otherwise, an error message will appear. Press the "Sell" button, and the current price of the amount of coins you sold will be added to your balance.