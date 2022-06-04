# Alpha Genbank

This repository is designed to store the backend project of a cannabis traceability system, the API REST is implemented using Django Rest Framework and a relational DB in the MySQL DB engine
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file in the genbank main directory.

### Database

`DATABASE_NAME`

`DATABASE_USER`

`DATABASE_PASSWORD`

`DATABASE_HOST`

`DATABASE_PORT`

### Django

`DJANGO_ALLOWED_HOSTS`

`SECRET_KEY`

## Installation

Install the project with django in a python 3.0 virtual environment

Use the file requirements.txt to install all required libraries for the project in the alpha-genbank directory with pip:

### Linux install:
```bash
pip3 install -r requirements.txt
````

Run the django server with:
```bash
python3 manage.py makemigrations && python3 manage.py migrate
python3 manage.py runserver
```