# Django CMS Tutorials

[![Build Status](https://travis-ci.org/ConPanna/Caturra.svg?branch=master)](https://travis-ci.org/ConPanna/Caturra)

Django CMS tutorials on YouTube. [Watch on YouTube](https://youtube.com/ConPannaAgency)


## Installation

### Install Python 3

````
sudo apt-get install libsqlite3-dev sqlite3 bzip2 libbz2-dev
sudo apt-get install python3
````

Find the path to Python 3
````
which python3
````

````
sudo pip install --upgrade virtualenv

virtualenv -p /usr/local/bin/python3 env
# or
# virtualenv -p /usr/bin/python3 env
````

Activate virtual environment
````
source env/bin/activate
````

Install dependencies
````
sudo pip install -r requirements.txt
````

## Create A New Project
Use this option if you want to create a new project.
````
sudo pip install djangocms-installer
djangocms -s -p . caturra
````

## Start The App

Run migrations
````
python manage.py migrate
python manage.py makemigrations
python manage.py syncdb
````

Run the server
````
python manage.py runserver
````
Or use the Procfile
````
foreman start
````

--------------

## Develop Apps
In the videos we will create apps that will integrate with the website.

To start a blog run:

````
python manage.py startapp blog
````

Add the blog app in the `installed apps` section.
````
# caturra/settings.py

````

Then define the urls, model and run a migration.
````
python manage.py makemigrations blog
python manage.py syncdb
````

[ConPanna](http://conpanna.net)
