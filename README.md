# Scorpion Kings Website

## Description 
This web application is used to book tickets to live music events of the 
Scorpion Kings. It includes an online store to purchasing merchandise,
as well as a blog app for keeping up with the latest news and trends
pertaining to the band.

## Table of contents
1. Create and activate a virtual environment.
2. Running Docker.
3. Other system requirements.
4. Credits.

## 1. Create and activate a virtual environment.
1. Ensure you have python installed on your machine.
2. To check if you have python installed open the command prompt and type
*python --version*.
3. Go to the root directory and type 
*python -m venv "name of your virtual environment"*
4. Activate the virtual environment using the following command,
*name of your virtual environment"\Scripts\activate.bat*.
5. To run the development server type
*python manage.py runserver*
You should see a message that the server is running at http://127.0.0.1:8000/. 
Open your browser and go to this URL.

## 2. Running Docker.
1. Dockerfile has already been created on your behalf in ****.
2. Create docker image by typing the following in the command prompt,
*docker build -t "name of your image" ./*.
Please ensure Docker desktop is open before running this command.
4. Run the image with this command, 
*docker run -d -p 8080:8000 "name of your image"*
5. Go to http://localhost:8080 to confirm that the image is running.
6. To deploy the image go to Docker Hub (https://hub.docker.com), click
a create repository and name it.
7. Rename the image on your local repository to match the image on Docker
Hub by running *docker tag "local image name" username/remote repo name*.
8. Login to Docker and push the local image using the two commands:
*docker login*
*docker push username/remote repo name *.
9. Test the website on a virtual machine. Visit  https://labs.play-with-docker.com/.

## 3. Other system requirements
1. To install dependencies listed in the requirements.txt file, type
the following in the command prompt *pip install -r requirements.txt*.

## 4. Credits
This file was created by only Tshepo Maubane.
