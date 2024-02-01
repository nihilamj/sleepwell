
# PROJECT DIARY

<br>
<br>

> Dates and Details of the work done for the project '**SleepWell**'.

<br>

## 📅 29 JAN 2024
I submitted three project ideas to the guide for approval, and the guide approved the project idea titled ‘Sleep, Health & Lifestyle predictor using Machine Learning in Python Django’.

<br><br>


## 📅 30 JAN 2024
Following packages and software were installed :
- Python
- PIP
- Postgresql
- Virtualenvwrapper-win
- Django
- python-decouple
- psycopg-binary 

<br><br>

## 📅 1 FEB 2024
- created a GitHub repository ‘sleepwell’ to build,commit my project and to store other related files.
- updated the git ignore
- created a django project named ‘sleepwell’
- created a database named 'sleepwell' in postgres using pgAdmin
- created .env file in root directory to store Postgresql credentials
- created a superuser for the project named as 'mj'
- created an app named 'mainapp' in the project
- changes were migrated & tables were automatically build by Django

<br>

**Changes made in settings.py file :**

- changed time zone to 'Asia/Kolkata'
- Imported config module from decouple to use the database credentials from the .env file
- added 'mainapp' to installed app section

<br>

**created urls.py file inside mainapp :**

- added the code for URL patterns for functions in views

<br>

**Changes made in views.py file in mainapp :**

- added the code for home function<br>

<br>

**changes made in urls.py file inside sleepwell:**

- added the code to include the URL patterns of mainapp

<br>
