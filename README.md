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

Now open your browser and go to [127.0.0.1:8000](http://127.0.0.1:8000)![signup]


<br>


# Overview
![sign-up](https://user-images.githubusercontent.com/122703595/233636664-c9292cba-8a50-49a6-a457-8d69f5ce1de9.png)
![profile](https://user-images.githubusercontent.com/122703595/233637211-44a93654-4bbe-4557-8428-03fcdc7caa5f.png)
![groups](https://user-images.githubusercontent.com/122703595/233637466-7d1da526-bf24-4c50-84cd-0c18de40aaae.png)
![Chat](https://user-images.githubusercontent.com/122703595/233637522-42bb1d9c-928f-4897-9b22-ed3f1f1f9ff0.png)
