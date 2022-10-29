{{cookiecutter.project_name}}
=============================

Development
-----------

Setup

    virtualenv .env -p {{cookiecutter.python}}
    source .env/bin/activate && pip install -r requirements.txt


Migrate

    export DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.dev
    python manage.py makemigrations
    python manage.py migrate


Start application

    export DJANGO_SETTINGS_MODULE={{cookiecutter.project_slug}}.settings.dev
    python manage.py runserver_plus --nopin

You can now visit http://localhost:8000/api/


Testing
-------

Run all tests

    pytest