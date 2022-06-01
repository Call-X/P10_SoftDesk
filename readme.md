
# OpenclassroomProjets - "SoftDesk API"


## Custommer asking:

Softdesk is an API that allows users to create and track technical issues.

This API is designed to operate in the backend of an iOS, Android or web application. The application shall allow users to create projects, add collaborators, create issues and comments, assign priorities or tags etc.

The application shall use the termination points of the API to request and write data.

The documentation of the API is available at the following location: Insomnia-documentater

The API is developped in python using Django Rest Framework.


## Installation guide :
1. Clone the repository 
```
$ git clone https://github.com/Call-X/LITReview.git
```
2. Navigate to the root folder of the repository

3. Create a virtual environnement with :
``` 
python -m venv projectenv
```
3. Activate the virtual environment with
``` 
projectenv/Srcipts/activate
``` 
4. install the project with its dependencies with :
``` 
pip install -r requirements.txt
``` 
5. Finally, run the server with :
``` 
python manage.py runserver
``` 

## How to use ?

1. Install Node.js which automaticaly will install the package manager JavaScript NPM

2. Install all dependencies to your project :
```
nmp install
```

4. Get your Insomnia Documentation file in your browser:
```
npx insomnia-documenter --config <Name_of_your_file>.json --output insomnia-final
```
 * * * Done! * * *
Your documentation has been created and it's ready to be deployed!

5. Go to your project.file with the command :
```
cd insomnia-final
```

6. launch with command : 
```
npx serve
``` 

7. Open the following adress on your web browser
```
http://localhost:3000
```
8. Follow the instruction on the Insomnia-Documenter


## Contributeur :

-Emile MIATH -

# Licence & Copyright :

Aucun copyrights



