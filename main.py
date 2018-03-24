from pymodm import connect
import models
import datetime
import numpy as np

def add_heart_rate(email, heart_rate, time):
    user = models.User.objects.raw({"_id": email}).first() # Get the first user where _id=email
    user.heart_rate.append(heart_rate) # Append the heart_rate to the user's list of heart rates
    user.heart_rate_times.append(time) # append the current time to the user's list of heart rate times
    user.save() # save the user to the database

def create_user(email, age, heart_rate):
    u = models.User(email, age, [], []) # create a new User instance
    u.heart_rate.append(heart_rate) # add initial heart rate
    u.heart_rate_times.append(datetime.datetime.now()) # add initial heart rate time
    u.save() # save the user to the database

def print_user(email):
    user = models.User.objects.raw({"_id": email}).first() # Get the first user where _id=email
    info = {
        "user_email": user.email,
        "heart_rate": user.heart_rate,
        "heart_rate_times": user.heart_rate_times
    }
    return info
    #print(user.email)
    #print(user.heart_rate)
    #print(user.heart_rate_times)

def hr_ave(email):
    user = models.User.objects.raw({"_id": email}).first()
    average = np.mean(user.heart_rate)
    return average

def hr_int_ave(email,ref_time):
    user = models.User.objects.raw({"_id": email}).first()
    time = user.heart_rate_times
    given_time = datetime.datetime.strptime(ref_time, "%Y-%m-%d %H:%M:%S.%f")
    hr_report = []
    for idx, val in enumerate(time):
        if time[idx] >= given_time:
            hr_report.append(user.heart_rate[idx])
    ave_report = np.mean(hr_report)
    return ave_report

if __name__ == "__main__":
    connect("mongodb://vcm-3574.vm.duke.edu:27017/heart_rate_databases_introduction") # open up connection to db
    create_user(email="suyash@suyashkumar.com", age=24, heart_rate=60) # we should only do this once, otherwise will overwrite existing user
    add_heart_rate("suyash@suyashkumar.com", 60, datetime.datetime.now())
    print_user("suyash@suyashkumar.com")
