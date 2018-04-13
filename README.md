# heart_rate_databases_starter

## Description
A database compiling user e-mail, user age, heart rate values, and time reported is created using MongoDB framework. The server (specific endpoints are included in the Components section) updates and reads information to the database. A sample client request is also included in the repository which walks through all possible requests the user can make to the database.

## Setup Instructions
The following instructions are written if the user chooses to set up the server using a vcm. Insure that pip and Docker are installed. 

After cloning the repo, change into the folder. Set up a Python virtual environment and install the packages listed in requirements.txt:
``` 
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

Set up a screen (for example `screen -S mongo`) to establish the database by typing `sudo docker run -v $PWD/db:/data/db -p 27017:27017 mongo`. 

Set up another screen to run the server by typing `gunicorn --bind 0.0.0.0:5000 server:app`.

Run client.py to see the requests in action.

## Components
Website: http://vcm-3574.vm.duke.edu:5000/

server.py is RESTful API
* /api/heart_rate is a POST request to add a new heart rate measurement for the user
* /api/heart_rate/<user_email> is a GET request that will return all heart rate measurements associated with the e-mail
* /api/heart_rate/average/<user_email> is a GET request that will return the user's average heart rate over all measurements
* /api/heart_rate/interval_average is a POST request that calculates and returns the average heart rate for the user since the time given. In addition, an indication if the reading is tachycardic based on the user's age is given. 

main.py is compilation of helper functions

models.py establish a MongoModel class

client.py is the example of client requests

test_client.py contains unit tests of functions, such as validating inputs (and is slight misnomer)

