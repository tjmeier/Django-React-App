# Starting the App
## Setting up the Repo
* Clone Repo
* `$ cd backend`
  
## Python Environment
* `$ python -m venv env`
* `$ env/Scripts/activate.bat`
* `$ pip install -r requirements.txt`

## Deployment
* Pull Changes
* Go to Backend Directory
* `$ python manage.py makemigrations`
* `$ python manage.py migrate`
* `$ python manage.py runserver`
* Go to Frontend Directory
* `$ npm run dev`
* Use the outputted URL in browser.

# Manual Backup
`$ python manage.py dumpdata -a -o data.json`

# Committing
* Encusre no sensitive or data files will be committed
* `$ pip freeze > requirements.txt`

# Features
* See `FEATURES.md`

# Configuration
## Creating React Frontend
* Install Node.js
* `$ npm create vite@latest frontend -- --template react`
* `$ cd frontend`
* `$ npm install axios react-router-dom jwt-decode`

## Creating Django Backend
* `$ django-admin startproject backend`
