# heart_rate_databases_starter
Starter codebase for BME590 Databases Assignment (which can be found [here](https://github.com/mlp6/Medical-Software-Design/blob/master/Lectures/databases/main.md#mini-projectassignment)). 

To get started with this sample code, you first need to get the mongodb program running. To do this, simply run 
```
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```

either on your local machine (if you have docker installed there) or on a virtual machine you have access to where you can first install docker.

:eyes: if you are running your mongodb database on a virtual machine, you need to replace the `connect` URI string in `main.py`. Replace `localhost` with a VM address, like so:

```py
connect("mongodb://vcm-0000.vm.duke.edu:27017/heart_rate_app") # open up connection to db
```

once your database is running and your connection string is set, you can run the starter program by running `main.py` after activating your `virtualenv` and installing all the dependencies listed in `requirements.txt`.

```
python main.py
```
# Components
Website: http://vcm-3574.vm.duke.edu:5000/

server.py is RESTful API

main.py is compilation of helper functions

models.py establish a MongoModel class

client.py is the example of client requests

test_client.py contains unit tests of functions, such as validating inputs (and is slight misnomer)

