# CapStone
## Distinctiveness and Complexity
The goal of this project was to create a comprehensive cryptocurrency trading platform using real-time data from the coinmarketcap.com API. Unlike other trading platforms, this project allows users to make deposits, withdrawals, and trades using a variety of cryptocurrencies, providing a seamless and user-friendly experience.

To accomplish this, I used a combination of technologies, including Django, CSS, Bootstrap, HTML, and JavaScript. I also integrated multiple APIs to gather real-time data on cryptocurrency prices, ensuring that users have the most up-to-date information when making trades.

One of the most complex aspects of this project was designing and implementing the portfolio and wallet system. Each user has a unique portfolio where they can store their deposited funds and track their trading history. When a user buys a particular cryptocurrency, the project automatically creates a new wallet for that currency, allowing the user to store and trade it independently from other currencies.

Overall, this project represents a significant achievement in the field of cryptocurrency trading platforms, and I am proud to have been able to create such a comprehensive and innovative tool using my skills in web development and API integration.

## Files:

### urls.py

This file contains all the url patterns that is going to be used in the website.

### views.py 

This file is responsible for all the backend work it consist with many functions which is going to be used to run the website routes, The functions are:

#### register

This will render the register page for registering a new user and adding the user to the database

#### login_view 

This method will render the login html template page for loging a user stored in the data base in.

#### logout_view 

This will render the logout html template file for loging the user out the user after been signed in.

#### portfolio

This method will render the portfolio page. using this method the user will be able to add new balance and it will show all wallets the user has.
