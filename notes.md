#Django:
A high-level Python web framework that encourages rapid development and clean, pragmatic design.


Framework--collection of libraries and a pre defined Structure-Laravel,expressjs,django
Library--Set of pre-written, pre-defined, reusable codes-react,panda,numpy
URL--Path to visit any webpage, navigate to diff pages.
Package--Pre-written codes

Battery-included philosophy--means that Django comes with many built-in tools,packages and features(admin panel, auth, orm)
Django-bakend servers/applications

Why Django?
Build on top of python
Quick development of websites
Lots of pacakges
Provides Security
It's scalable

MVT Architecture
Model-View-Template

Model-Manages the data and business logic. INteracts with the database.--uses ORM Model--Layer which interacts with the database
View-Handles the request, processes the data from Model and sends it to Template for rendering.
Template-Defines the presentation layer. It receives data from the view and displays it to the user.

user--request-->django-->url-->view-->model-->database-->template---response-->user

Setting up the environment:
python -m venv myenv
 myenv\Scripts\Activate
pip install Django
django-admin --version

#To create a new project: 
python -m django startproject myProject
or:
django-admin startproject myProject

Outer myProject/  === project root directory
inner myProject/ == project package ---contains all configuration files
manage.py = command line tool to run and manage the project, run the server,creates the app and other Django management commands.

Command to run the server -- python manage.py runserver
default port number -- 8000

wsgi (Web Server Gateway Interface)
asgi (Asynchronous Server Gateway Interface)

#App
can create multiple apps-- inside a project

Command to create an app-- python manage.py startapp myapp
To register the app -- inside a project -- settings.py -- installed apps -- edit app name there

HTTP Methods:
(1)GET--Retrive the data without modifying
(2)POST--Uploading new data on the server
(3)PUT--Updating the entire data/resource on the server
(4)PATCH--Updating any particular data/entity
(5)DELETE--Deleting a resource from the server

How Django displays a web page:
Browser(requests a page)  ->url(sends request to the view)  ->view(prepares data(context))  ->template(creates HTML using the data)  ->browser(displays the final page)

user--> urls.py --> view.py <--> model--> database

Testing:- tests.py
To check and help build the software more efficiently.

import-- import django's testing tools.
testcase -- creates a testing class
Hometest -- organizes related tests
test_home-- a test function (must start with test)
assertEqual -- 


Diff --- python manage.py makemigrations
python manage.py migrate
