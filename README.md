# Unleashed 2 back end

This project contains all files to setup the back end for the Unleashed app.

## Project setup

### virtualenv setup
To execute in a command prompt to setup the virtual environment ```virtualenv``` in the root of the project.

```
pip install virtualenv
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

## Google Spreadsheet access
Some of the data can be found within spreadsheets hosted on Google's Google Docs platform. To access those spreadsheets, a json needs to be loaded whoms location has to be set in the ```GOOGLE_APPLICATION_CREDENTIALS```-variable on the user's system as ```/path/to/the/json/client_secret.json```.

For demo purpose, this repository includes a ```client_secret.json``` at ```/unleashedapp/client_secret.json```. Therefor, the path can be set to ```c://path/to/the/github/project/root/unleashedapp/client_secret.json```.

### Windows
1. Search for "Edit the system environment variables" and open it
2. Choose "Environment Variables..."
3. Under "User variables for ```<name>```", click "New..."
4. Set ```GOOGLE_APPLICATION_CREDENTIALS``` as "Variable name" and ```c://path/to/the/github/project/root/unleashedapp/client_secret.json``` as "Variable path"
5. Click "OK", "OK" and again "OK"
6. Command Prompt or PowerShell needs to be restarted to load the new environment variables

## Run server
To be executed in a command prompt within the virtual environment ```env``` to run the server on ```http://localhost:8000/```.

```
python manage.py runserver
```