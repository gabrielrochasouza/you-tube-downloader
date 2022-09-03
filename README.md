# What this project is about:

## <a href="https://yt-downloader-application.herokuapp.com/" target="_blanck">Link of project deployed</a>

This project was created to download videos from youtube, in video format and mp3 format. I used django and its libraries to do this task, and deployed in heroku. 

It was used django templates to render pages, and pytube to open a new window in the browser, where you can download the video without having to using the heroku server, since it would increase a lot the time to download.

In this application you can see the size of the file you will download, and choose the resolution of the video you want to download.




## Image overview

<img src="./overview.png" alt="Overview Image"/>

<img src="./download-screen.png" alt="Download screen"/>



<br>

## Main technologies
- HTML
- CSS
- JAVASCRIPT
- BOOTSTRAP
- PYTHON
- DJANGO


## Main Libraries of Django used:
- Pytube
- ipdb (to debug the code)
- Jninja


## Commands to start the project locally

First you need to add a .env file in root, take a look at .env.example to see the variables you should set, it is a SECRET_KEY, you can define its value, since you are using in your local repository.

After this step is done, follow the commands bellow.

```
python -m venv venv 
## (To create a venv a virtual environment so you can install the dependencies of this project)

source venv/bin/activate 
## (To activate the virtual environment)

pip install -r requirements.txt --upgrade pip
## (To install all dependencies of this project)

python manage.py runserver
## (To start server at port 8000)

## After that access this url in your browser: http://localhost:8000/
```

One line command:
```
python -m venv venv && source venv/bin/activate && pip install -r requirements.txt --upgrade pip && python manage.py runserver
```
