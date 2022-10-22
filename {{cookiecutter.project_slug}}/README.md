Quickstart
==========


Setup

    virtualenv .env -p {{cookiecutter.python}}
    source .env/bin/activate && pip install -r requirements.txt


Start application

    export DJANGO_SETTINGS_MODULE=mycoolproject.settings.dev
    python manage.py runserver_plus --nopin

You can now visit http://127.0.0.1:8000


Testing
=======

Run all tests

    pytest