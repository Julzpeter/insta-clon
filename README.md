# Instaclone

## Description
Instagram is a website that allows users to share photos and videos from their lives, add captions and engage with others.

## Author
Juliet Koech


## Date made
25/07/2019

## User Stories
As a user of the application you will be able to:

* Sign in to the application to start using
* Upload pictures to the application 
* View different photos that interest you
* See my profile with all my pictures
* Follow other users and see their pictures on my timeline
* Like a picture and leave a comment on it


## Behavior Driven Development
| Behavior              | Input                                                                  | Output                         |
|-----------------------|------------------------------------------------------------------------|--------------------------------|
| Post an image         | Click on add button                                                    | Adds the post of the user      |
| Comment on the image  | Comment on the comment form.Add your comment. Click on the post button | Comment is added and displayed |  
| Follow other users    | Click on the follow button                                             | User is added to your timeline | 


##  Installing
* You require a minimum python version 3.6 to run the application
* Clone this repo: git clone https://github.com/Julzpeter/insta-clon.git
* The repo comes in a zipped or compressed format. Extract to your prefered location and open it.
* To run the app, you'll have to run the following commands in your terminal pip install -r requirements.txt
*On your terminal,Create database gallery using the command below. CREATE DATABASE instagram;
*Migrate the database using the command below
 python3.7 manage.py migrate
* Then serve the app, so that the app will be available on localhost:8000, to do this run the command below
 python manage.py runserver
* Use the navigation bar/navbar/navigation pane/menu to navigate and explore the app.

## Running the tests
Use the command given below to run automated tests. 
python3.7 manage.py test instagram
python3.7 manage.py test user


## creating a virtual environment
* python3.7 -m venv --without-pip virtual
* source virtual/bin/activate

## downloading the latest version of pip
Myinstagram heavily relies on pip to install Django and any other packages that we will need.

(virtual)$ curl https://bootstrap.pypa.io/get-pip.py | python

## Install Django
We need to install the latst django release of version 1.11
(virtual)$ pip install django==1.11


## Technologies used
* Django - web framework used
* HTML-For building Markup pages and user interface
* CSS and MDB Bootstrap-for styling user interface

## Bugs
If you encounter any bags feel free to email me at chepngetichjuliet@gmail.com

## Support and contact details
Contact me on chepngetichjuliet@gmail.com for any comments,reviews or advice

## MIT LICENSE
[MIT]()