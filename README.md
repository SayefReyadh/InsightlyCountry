# InsightlyCountry
A simple Django project which fetch data from a [Country API](https://restcountries.eu/rest/v2/all), format them, make them available by creating simple rest APIs and display the information in a simple secured web page. 

## Installation
- [Python3](https://www.python.org/downloads/)
- [Pycharm Professional](https://www.jetbrains.com/pycharm/download/)

## Requirements 
After cloning the project in your local directory you have to create a virtual environment in the project directory. Open up CMD in the InsightlyCountry project folder. 

- Create a virtual environment
	`python -m venv insightly`
- Activate virtual environment
	`insightly\Scripts\activate`
- Install all dependency requirements
	`pip install -r requirements.txt`

## Run 
Open up CMD in the InsightlyCountry project folder. 

- Activate virtual environment [Again if you closed the previous CMD]
	`insightly\Scripts\activate`
- Make Migrations
	`python manage.py migrate`
- Create a Super Admin
	`python manage.py createsuperuser`
- Run the application at http://127.0.0.1:8000/
	`python manage.py runserver`

#### Basic Instructions
Initially, the `Login page` will appear. You can login  using the superuser you have created  or you can sign up as a new user using the  `Registration Page`. At the initial phase the  database will be empty. `Load or Reset Database` will help you to Fetch all data from [Country API](https://restcountries.eu/rest/v2/all) and load them in the Sqlite Database. If the database is already populated, it will delete all delete all data and reload all the data again.

#### Disclaimer
The [login](https://jsfiddle.net/ivanov11/dghm5cu7/) and [registration](https://jsfiddle.net/ivanov11/hzf0jxLg/) page templetes are used under the term fair use.  
