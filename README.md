# CarZone

This is a fullstack web application with full CRUD implementation. Users can register for an account and shop for cars. When they find a car, they can contact the seller and the seller will receive a notification via mail. CarZone is an online shop for buying used and new cars. Users can filter the available car listings using different parameters. More advanced features like token authentication and filter by price will be implemented in future updates to the application.



![Screenshot](carzoneweb.png?raw=true "carzone website")

## Technologies 

The following technologies were used in this project:

- [HTML](https://html.com/)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps)
- [Bootstrap](https://getbootstrap.com/)
- [JavaScript](https://www.javascript.com/)
- [jQuery](https://jquery.com/)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [PostgreSQL](https://www.postgresql.org/)

## Requirements

Before starting, you need to have [Git](https://git-scm.com), [PostgreSQL](https://www.postgresql.org/) and [Python](https://www.python.org/) installed. Alternatively, you can download the code as a zip file. Also setup your database in the settings.py module located in carzone directory.

## Clone this project

    git clone https://github.com/benidevo/carzone-website.git

## Create virtual environment

    python3 -m venv env

## Activate virtual environment

    . env/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Create an admin user profile

    python manage.py createsuperuser

## Collect Static files

    python manage.py collectstatic

## Start server

    python manage.py runserver
