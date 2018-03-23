import requests
from server import *

# Post inputs
input1 = {
    "user_email": "suyash@suyashkumar.com",
    "user_age": 50,
    "heart_rate": 100
}

input2 = {
    "user_email": "suyash@suyashkumar.com",
    "heart_rate_average_since": "2018-03-09 11:00:36.372339"
}

link = "http://vcm-3574.vm.duke.edu:5000"
# link = "http://127.0.0.1:5000/"

# Request
r1 = requests.post(link+"/api/heart_rate", json=input1)
print(r1.json())

#r2 = requests.get(link+"/api/heart_rate/suyash@suyashkumar.com")
#print(r2.json())

#r3 = requests.get(link+"/api/heart_rate/average/suyash@suyashkumar.com")
#print(r3.json())

#r4 = requests.post(link+"/api/heart_rate/interval_average")
#print(r4.json())
