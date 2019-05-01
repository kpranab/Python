# Python
Install virtualenv 

verify easy_install --version
Check the script path is set or not in path -> C:\Users\Muna\AppData\Local\Programs\Python\Python36\Scripts\
install virtualenv -> pip3 install virtualenv
Verify virtualenv installed ->easy_install virtualenv

Create virtualenv -> virtualenv renv (Name of virtualenv)
Then go to the cd renv/Scripts folder and type activate to activate virtualenv

Go back to project folder and install Django over there
	pip install django
Install Django for rest framework
	pip install djangorestframework

Create Django project
	django-admin startproject rest
Create Django app
	django-admin startapp restapp
Check the app is set correctly from the project folder i.e. rest
	python manage.py runserver
	
Do the coding on required file and then do migration

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

#Adding Image field on RestAPI
Go to root directory i.e restenv
pip install pillow

#Upgrade pip version
python -m pip install --upgrade pip

#Install Django filter
pip install django-filter

#Test end points
http://127.0.0.1:8000/task/?completed=True

#Search functionality for rest-API
http://127.0.0.1:8000/task/?search=before
