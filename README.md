# Tennis Reservations

This is a small django project where it is possible to create tennis clubs, different types of courts and then reserve them at
 desired hours. The main task for me in this project was to learn to work with different types of time data.

## Getting Started

Below you will find the instructions and requirements on how to install and run this project on your local machine.

### Installing

The first step is to clone the repository.
After that you can create a virtual environment, activate it and install the requirements.txt file:

```
python -m venv env
source env/Scripts/activate.bat
python -m pip install -r requirements.txt
```

After successful installation you can migrate:

```
python manage.py migrate
```
And then start the server:

```
python manage.py runserver
```

## Usage

Login credentials to try the project with existing demo database:

Username: admin  
Password: admin
