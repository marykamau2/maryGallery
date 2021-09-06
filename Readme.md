### Author
 Mary Kamau
### Description
This is an application that will allow users to read news basically from bitcoin, apple and tesla news. As a user of the web application you will be able to:

- See the available news on the homepage
- User can click on read more to get more news on the source website
- See the image of the article he/she wants to read
### Setup and installations
- Clone Project to your machine
- Activate a virtual environment on terminal: source virtual/bin/activate
- Install all the requirements found in requirements file.
- On your terminal run python3.8 manage.py runserver
- Access the live site using the local host provided
### Getting started
### Prerequisites
- python3.8
- virtual environment
- pip
- Clone the Repo and rename it to suit your needs.
- git clone https://github.com/marykamau2/maryGallery
- Initialize git and add the remote repository
- git init
- git remote add origin <your-repository-url>
- Create and activate the virtual environment
- python3.8 -m venv virtual
- source virtual/bin/activate
- Install dependancies
- Install dependancies that will create an environment for the app to run pip install -r requirements.txt

## Make and run migrations
- python3.8 manage.py check
- python manage.py makemigrations news
- python3.8 manage.py sqlmigrate news 0001
- python3.8 manage.py migrate
- Run the app
- python3.8 manage.py runserver
- Open localhost:8000

### Testing the Application
- python3.8 manager.py tests

### Built With
- Python3.6
- Django
- Boostrap
- HTML
- CSS
### Licence
- This project is under the MIT licence