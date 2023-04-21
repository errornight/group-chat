# Django Group Chat website
A very simple chatting app. With no **web-sockets**(yet) and no **JS** :|<br>
**Why?** because I don't know JavaScript. But I'm planning to learn it.(I will update this repo.)
<br>

I created this website only to improve my base skill.

### Front-end
As I don't know anything about front-end development, The UI has been generated using **[Chat-gpt](https://chat.openai.com/)**.
<br>

# Installing
To start it locally, just follow the steps:
## 1. Create a virtual environment.
```
pip install virtualenv
```
```
virtualenv env
```
##### *Activate the virtual environment*.
```
env/Scripts/activate
```
## 2. Install requirements
```
pip install -r requirements.txt
```
## 3. Configure Django
+ #### Install database.
```
python manage.py makemigrations
```
```
python manage.py migrate
```

+ #### Add a superuser to manage the website.
```
python manage.py createsuperuser
```
##### Then enter username and password.

## 4. Run it locally
```
python manage.py runserver
```
<br>

Now open your browser and go to [127.0.0.1:8000](http://127.0.0.1:8000)

<br>


# Overview
