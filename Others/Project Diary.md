
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

- added the code for URL patterns for functions in views.py file

<br>

**Changes made in views.py file in mainapp :**

- added the code for home function

<br>

**changes made in urls.py file inside sleepwell:**

- added the code to include the URL patterns of mainapp

<br><br>


## 📅 2 FEB 2024

- Created a static folder, inside this folder created another folder named as mainapp
- Created a templates folder, inside this folder created another folder named as mainapp

<br>

- downloaded a template from [www.free-css.com](http://www.free-css.com/) and extracted
- Copied the below mentioned folders and files to the mainapp/static/mainapp directory

    1. CSS

    2. Fonts

    3. img

    4. js

    5. mail

<br>

- created a base.html in mainapp/templates/mainapp directory
- created below mentioned html files in mainapp/templates/mainapp directory and extended using 
base.html

    1. home.html
    2. about.html

<br>

**Changes made in views.py file in mainapp :**

- changes made for home function
- created below mentioned functions

    1. about

<br>

**created urls.py file inside mainapp :**

- added the URL pattern for below mentioned functions from views.py

    1. about

<br><br>


## 📅 6 & 7 FEB 2024

- created a new app named 'healthrecord'
- created a urls.py inside healthrecord folder
- Created a templates folder, inside this folder created another folder named as healthrecord 
- created a forms.py file inside healthrecord folder.

<br>

**Changes made in settings.py file :**
- added healthrecord to app section.

<br>

**Changes made in urls.py file in sleepwell folder :**
- added the code to include the URL patterns of healthrecord app.

<br>

**Changes made in Models.py**

- created a model for
    1. Occupations
    2. HealthProfile

**Changes made in Admins.py**
- created admin class and register for the following model
    1. Occupations
    2. HealthProfile

**Changes made in forms.py**
- created forms for following model
    1. OccupationForm
    2. HealthProfileForm


**Templates**

- created below mentioned html files in /healthrecord/templates/healthrecord directory

    1. signup.html
    2. signin.html

<br>

**Changes made in views.py file in healthrecord :**


- created below mentioned functions

    1. signup
    2. signin

<br>

**created urls.py file inside mainapp :**

- added the URL pattern for below mentioned functions from views.py

    1. signup
    2. signin



<br><br>



## 📅 9 FEB 2024

- submitted a Absract of the Project to Project Guide

    1. Research Area
    2. Objectives
    3. Requirements
    4. Modules with small Descriptions.
    5. Problem statement.


- uploaded the abstract file to the Documentation folder in project git repository.

<br> <br>

## 📅 12 FEB 2024

- Uploaded the the Abstract to **Documentation** Folder
- Renamed the 'HealthProfile' to 'HealthProfileSignUPForm' in forms.py
- Renamed the healthrecord app to healthprofile

<br>

**Templates**
- dashboard.html

<br>

**urls.py in healthprofile**
- added the URL pattern for the following
    1. Dashboard
    2. signout

<br>

**views.py in healthprofile**
- added the functions for the following
    1. Dashboard
    2. signout
<br>

**forms.py in healthprofile**
- added the following forms
    1. HealthProfileSignINForm
    2. HealthProfileSignUPForm

<br><br>

## 📅 13 FEB 2024

- added the code for a successfull login and logout with a user session

<br>

**views.py in healthprofile**

- added below mentioned views

    1. getUser()
    2. removeUser()

- changes made for below mentioned views

    1. signin()
    2. signout()
    3. dashboard()

<br>

**templates.py in healthprofile**

- changes made for below mentioned templates

    1. dashboard.html


<br><br>

