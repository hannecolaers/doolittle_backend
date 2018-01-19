# Unleashed 2 backend

## Project setup

### virtualenv setup
To execute in a command prompt to setup the virtual environment ```virtualenv``` in the root of the project.

```
pip install virtual env
virtualenv env
```

To execute in a command prompt to activate the virtual environment ```env```.
```
env\Scripts\activate
```

### Django setup
To execute in a command prompt within the virtual environment ```env``` to install the requirements (Django, MySQL Driver, Django REST framework, etc.).

```
pip install -r requirements.txt
```

or

```
pip install -r requirements_test.txt
```

## Database configuration
Django expects a MySQL (or compatible, e.g. MariaDB) database with the name ```unleashed``` to be accessible with the username ```root``` without password as set in ```unleashedapp/unleashedapp/settings.py:76```.
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'unleashed',
        'USER': 'root'
    }
}
```

Update database:
```
python manage.py makemigrations
python manage.py migrate
```

## Run server
To be executed in a command prompt within the virtual environment ```env``` to run the server on ```http://localhost:8000/```.

```
python manage.py runserver
```

## Run coverage
```
coverage run manage.py test
coverage report
```

html report:
```
coverage html
```

## Configuration django-rest-framework-social-oauth2
Package for the authentication with google oatuh2.

The code for the support of Django 2 is available in github, but there is no release yet with this update. So for now you have to make these change in the package in your virtual enviornment folder:
Lib/site-packages/rest_framework_social_oauth2 

3 files need changes:
* authentication.py
* backends.py
* oauth2_grants.py
```
replace this line: 
from django.core.urlresolvers import reverse
with:
try:
    from django.urls import reverse
except ImportError:  # Will be removed in Django 2.0
    from django.core.urlresolvers import reverse
```

Now go to django admin and add a new Application.
* client_id and client_secret shouldn't be changed
* user should be your superuser
* redirect_uris should be left blank
* client_type should be set to confidential
* authorization_grant_type should be set to 'Resource owner password-based'
* name can be set to whatever you want

In the front end Xamarin project: go to Configuration.cs and change the client_id and client_secret.
