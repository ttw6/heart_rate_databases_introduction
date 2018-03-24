from flask import Flask, jsonify, request
from pymodm import connect
from main import *

connect("mongodb://vcm-3574.vm.duke.edu:27017/heart_rate_app")

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hi!"


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    """ Store inputted measurement for user w/ email

    """
    r = request.get_json()
    try:
        add_heart_rate(r["user_email"], r["heart_rate"], datetime.datetime.now())
        return jsonify("Updated {} Info".format(r["user_email"]))
    except:
        create_user(r["user_email"], r["user_age"], r["heart_rate"])
        return jsonify("Created new user")


@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def heart_meas(user_email):
    """ Return all heart rate measurements for user

    """
    try:
        info = print_user(user_email)
        return jsonify(info)
    except:
        return jsonify("Unknown User")


@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def heart_ave(user_email):
    """ Return user's average heart rate over all measurements

    """
    try:
        ave = hr_ave(user_email)
        return jsonify(ave)
    except:
        return jsonify("Unknown User")


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def heart_int_ave():
    """ Calculate and return average heart rate for user since the time given

    """
    try:
        r = request.get_json()
        ave = hr_int_ave(r["user_email"],r["heart_rate_average_since"])
        return jsonify(ave)
    except:
        return jsonify("Unknown User")
