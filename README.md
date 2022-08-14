# Capstone1
Springboard Capstone Project 1 - Application Name: Mental Keep



## Background
Mental Keep is a privatized journal application that allows the user to express their thoughts and feelings in a comfortable environment. The journal is purposely built to look like a blank slate to simply inspire discussion without distraction. The user interaction with the app is simply that, just an interaction. As somone who struggled with mental health myself, all I ever needed was a platform to keep my thoughts. A platform to just listen and doesn't have to respond. 

## About
Mental Keep is broken down into 3 important sections. The first section being "Quick Jot" this application provides a quick write experience and is targeted to someone who may be trying to to document their thoughts for the first time and provides no pressure of sigining up. The second section is the journal home and journal page itself. The journal home is the users space. The user space provides two options, creation of a new journal entry, and a Patient Health Questionnaire (also known as PHQ9). It should be noted that the PHQ9 is by no way a method for the user of the application to self-evaluate their mental health. The journal page is a comfortable page with a title and text area allowing the individual to write. The final section is the PHQ9 questionnaire. This page is avaialble to only registered users of the application. This page is a way to serve as a self-review to identify unknown feelings or bring attention to areas that a user may not think about or know to identify.

## Expected Functionaliy
The following behaviors should be expected from the app.
1. A daily inspirational quote should appear daily.
2. The Mental Keep icon on the top left of the navbar should redirect home each time clicked.
3. Upon registration the user should be added to the user table and the password should be encrypted.
4. During registration if an image is not provided, a default image should apply.
5. When login occurs the button should then change to logout.
6. Once logged in the Mental Keep icon should now redirect to the homepage.
7. When a new journal is created the following should be saved:
    - The Jounal Title
    - The Journal Body
    - The created Journal date
8. A questionnaire button should be available on the homepage.
9. The questionnaire button should direct to the PHQ9 page for a simple dropdown questionnaire.
10. On the journal and quick jot bodies the text should be limited to 1500 characters.
11. Journal title should be limited to 120 characters.
12. Password should be a minimum of 8 characters and max of 32 characters.
13. Username should be a minimum of 4 characters and max of 15 characters.

## Future Functionality
- [x] Deploy to Heroku
- [x] PHQ9 score card and provide score form test.

# Preview
Here are some screen captures of the application.

## Home
![image](https://user-images.githubusercontent.com/83305789/183249611-da16b7c8-c905-44d2-b27d-af3b297f4621.png)

## QuickJot
![image](https://user-images.githubusercontent.com/83305789/183249640-15c9b818-91e3-4600-8357-21ede6567e87.png)

## PHQ9
![image](https://user-images.githubusercontent.com/83305789/183249667-68e36778-69c0-46b3-9e0a-adf1c31bb83c.png)

## Getting Started 
Here are the steps to get the application started.

### Windows
1. Start your **WSL** environment
```cmd
wsl
```
2. Creat your virtual environment
```terminal
python3 -m venv venv
```
3. Start the postgresql service
```terminal
sudo service postgresql start
```
4. Navigate to the virtual directory and run:
```terminal
python3 createdb mentalkeep_db
```
5. Run the **requirements.txt** file to install all needed requirements
```terminal
pip3 install -r requirments.txt
```
6. After the installation run **ipython**
```terminal
ipython
```
7. From **ipython** run the seed.py file to upload the PHQ9 questions.
```ipython
%run seed.py
```
8. After the seed file is complete you may exit ipython and run flask.
```terminal
flask run
```
9. Create a user to access the **Journal** and **PHQ9** portion of the site.

## OSX and Linux

2. Create your virtual environment
```terminal
python3 -m venv venv
```
3. Start the postgresql service
```terminal
sudo service postgresql start
```
4. Navigate to the virtual directory and run:
```terminal
python3 createdb mentalkeep_db
```
5. Run the **requirements.txt** file to install all needed requirements
```terminal
pip3 install -r requirments.txt
```
6. After the installation run **ipython**
```terminal
ipython
```
7. From **ipython** run the seed.py file to upload the PHQ9 questions.
```ipython
%run seed.py
```
8. After the seed file is complete you may exit ipython and run flask.
```terminal
flask run
```
9. Create a user to access the **Journal** and **PHQ9** portion of the site.
