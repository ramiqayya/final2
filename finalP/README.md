# CapStone
## Distinctiveness and Complexity
The goal of this project was to create a comprehensive cryptocurrency trading platform using real-time data from the coinmarketcap.com API. Unlike other trading platforms, this project allows users to make deposits, withdrawals, and trades using a variety of cryptocurrencies, providing a seamless and user-friendly experience.

To accomplish this, I used a combination of technologies, including Django, CSS, Bootstrap, HTML, and JavaScript. I also integrated multiple APIs to gather real-time data on cryptocurrency prices, ensuring that users have the most up-to-date information when making trades.

One of the most complex aspects of this project was designing and implementing the portfolio and wallet system. Each user has a unique portfolio where they can store their deposited funds and track their trading history. When a user buys a particular cryptocurrency, the project automatically creates a new wallet for that currency, allowing the user to store and trade it independently from other currencies.

Overall, this project represents a significant achievement in the field of cryptocurrency trading platforms, and I am proud to have been able to create such a comprehensive and innovative tool using my skills in web development and API integration.

## Files:

*in myapp folder I modified the following files:*
### urls.py

This file contains all the url patterns that is going to be used in the website.

### views.py 

This file is responsible for all the backend work it consist with many functions which is going to be used to run the website routes, The functions are:

* register

This will render the register page for registering a new user and adding the user to the database

* login_view 

This method will render the login html template page for loging a user stored in the data base in.

* logout_view 

This will render the logout html template file for loging the user out the user after been signed in.

* portfolio

This method will render the portfolio page. using this method the user will be able to deposit and withdraw money, also it shows all wallets that the user has.

* sell

This mehtod will render the sell page. After you insert the amount this route will check the amount of coins you have in this wallet and check the current price of that coin and sell. after sell it the money will be added to the main balance in the portfolio.

* trade 

This method will render the trade page template where you can enter the symbol of a cryptpcurrency then press check price. this method will check if that symbol exists and will show the current price of this coin. Under the shown price you can press the buy coin button that will transfer you to the buy page.

* buy 

After checking the price in the trade page you can proceed and press buy button, this method will check the available balance in your portfolio and let you buy a new coins with new wallet or add to coins to the existing wallets.

* lookup

This function will take the coin symbol , then send a request to the API and return the data for that coin symbol.

### models.py

This file has 3 models:

* User

This model for creating new user.

* Wallet

This model is for creating new wallet.

* CoinsAmout

This model is for adding coins amounts for each wallet.

*inside templates/myapp I added the following files:*

### register.html

This file contains the form for registering a new user.

### login.html

This contains the login form 

### index.html

This template file contains the main page which has the top 10 coins table.

### portfolio.html

This template file contains the user portfolio which shows the balance and a table wallets with each amount of coins and it's current value.

### trade.html

This template file contains a  form for entering the symbol that you would like to enquire about it's current price. As soon as you click check price button the current price will appear with a buy botton.

### sell.html

After clicking at the sell button next to each coin you will be directed to the sell page. This file template is for sell page which contains a form for entering the amount of coins you will like to sell.

### error.html

This template file for showing error codes and error messages.

### layout.html

This template file is for the layout of all pages which can be included in all other templates it contains the navbar and any other view that is going to be shown in all pages.

*inside static/myapp I added the following files:*

### styles.css

This file is responsible for some of the styles in the website.

### app.js

This javascript file is for adding some dynamic styles to the website.

## How to run the website

To use this application you need to register a new user choose Register at the top right, then enter a Unique Username, E-mail, password and confirm password. Now you have a new account and you can enter and use the application anytime by choosing login for entering the website.
The Index or homepage has a table of the top 10 cryptocurrencies by cap.
To buy a new cryptocurrency first you have to choose trade button at the navbar, a new page will open you with a title of price query and text field asking for coin symbol that you would like to enquire about. After entering a correct symbol for a coin and pressing check a price the name of that coin with its symbol and price will appear at the bottom also a button will appear asking you if you would like to buy that coin. Whereas if you enter a wrong symbol the error page will appear with an error message.
After entering a correct symbol then pressing buy that coin you will be redirected to the buy page this page will show you the current price and a field from entering the amount of that coin you would like to buy. But you can't anything without having a balance first.
To add money to your balance you need to go to the portfolio page first. you can find the portfolio at the navbar, a new page will open showing the name of the user and the balance he have. Two fields one for entering the amount of money you would like to deposit or withdraw the other is a drop field for choosing the transaction type, wether you would like to depoit or withraw money. To deposit money to your account enter the amount you would like to deposit then choose deposit then press the "Deposit/Withdraw" button, now you can use that balance to buy cryptocurrencies.
Again go to trade page and enter a valid symbol then press buy, enter the amount of that currency you would like to buy to total price of the amount will appear at the bottom of the field, press buy if you have enough credit, again you will be redirected to the portfolio page and a new wallet will appear at the table in the bottom of the page with coin symbol, amount and value in usd. 
Please keep in mind that if you enter an amount of a coin with a total price more than what you have in the portfolio. An error page will appear telling you that you don't have enough balance.
Try to buy several coins with the money you've deposited before. You will see if you buy a new coin it will be appear in the portfolio with a new wallet with the coin symbol, in the other hand if you buy an amount of you coin that you already have that amount will be added to the amount you have previously in the same wallet.
To sell coins that you already have go to the portfolio then beside each coin you will find a sell button, press that button you will be sent to the sell page. Choose the amount that you would like to sell not more than what you have and not less than 0, otherwise an error message will appear, then press the sell button. the current price of the amount of coins you sold will added to balance.
