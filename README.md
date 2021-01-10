# InsightlyCountry
A simple Django project which fetch data from a [Country API](https://restcountries.eu/rest/v2/all), format them, make them available by creating simple rest APIs and display the information in a simple secured web page. 

## Installation
- [Python 3python](https://www.python.org/downloads/)
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

- Make Migrations
	`python manage.py migrate`
- Run the application at http://127.0.0.1:8000/
	`python manage.py runserver`
