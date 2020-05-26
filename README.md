# Food Vendor API (FVA) V1.
# Getting Started
### These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
* Clone the repo to your local machine.
* Navigate to the cloned file.
* Open the cloned file using any of your desire IDE tool.
* Cd to root directory of the cloned file and create a virtual environment.
* Pip install requirements.txt.
* Create a postgres database and navigate to settings.py to change to the database created.
* Run python manage.py migrate to migrate the Model Tables to the database and ./manage.py runserver to run the program.
# Deployment
This project is deployed using Heroku server. Visit https://devcenter.heroku.com/articles/deploying-python for Heroku Django deployment flow. 
Navigate to http://foodvendorapi.herokuapp.com/admin to login to admin panel using
__testing@gmail.com__ and __password__ as username and password respectively in order to see the API endpoints of the deployed application.
# Built With
* Python
* Django 
* Rest Framework
* Postgres (Database)
