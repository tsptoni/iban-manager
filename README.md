## IBAN Manager QuickStart

Operating System requirements
=============================

* docker ce
* docker-compose


Libraries and Components used
=============================

* Django 2.1
* Django REST Framework 3.8
* Python 3.6
* django-rest-framework-social-oauth2 for Google Auth
* python-stdnum for values validations (In our case for IBAN accounts)
* django-querycount Debug queries


Installation
============

#### IMPORTANT!
**Make a copy of the file env.example and renamed it to .env**


You should make the list of Google Emails you want to login in the app, since the app uses
Google Authentication, it requires at least one ADMIN user matches the google email.

Example:

`FIRST_ADMIN_USERS=example@mail.com,bob@mail.com`

This will create the ADMIN users at startup, so this list can be expanded at any time to add new
ADMIN users (or just use the Django Admin Panel http://localhost:8000/admin/ ).

To build the project in development mode:

Move to the base directory (you should see the dev.yml file).

* 1 `docker-compose -f dev.yml build`

This will take a while until all the dependencies are installed (Python requirements, React packages and OS binaries).

Once done, start the project with:

* 2 `docker-compose -f dev.yml up`

* 3 Open your browser and go to http://localhost:3000

* 3.1 If you want to explore the Django Admin Panel, go to http://localhost:8000


Tests
=====

To execute Django tests just type:

`docker-compose -f test.yml up`

**Note:**

After the tests, PostgreSQL doesn't shutdown. This can cause malfunction with other docker projects if they use
the same port.

To avoid this, just execute:

`docker-compose -f dev.yml stop`


Usage
=====

1 Login with you Google Account using the top button "Login with Google".
2 In the user list you will see only the ADMIN accounts.
3 You can create new users in the tab "New User".
4 To see and update an user, you can click the row of the user in "Users List".
    4.1 If you are the creator of the user, then you will be able to add new accounts and modify user details.
