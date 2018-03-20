from flask import Flask, jsonify, request
import main

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi!"

@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    pass

@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def heart_meas():
    pass

@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def heart_ave():
    pass

@app.route("/api/heart_rate/interval_average", methods=["POST"])
def heart_int_ave():
    pass
