from flask import Flask, jsonify, request
import main



app = Flask(__name__)


@app.route("/")
def hello():
    return "Hi!"


@app.route("/api/heart_rate", methods=["POST"])
def heart_rate():
    """ Store inputted measurement for user w/ email

    """
    r = request.get_json()
    create_user(r.user_email, r.user_age, r.heart_rate)
    add_heart_rate(r.user_email, r.heart_rate, datetime.datetime.now())


@app.route("/api/heart_rate/<user_email>", methods=["GET"])
def heart_meas(user_email):
    """ Return all heart rate measurements for user

    :param user_email:
    """
    info = print_user(user_email)
    return jsonify(info)


@app.route("/api/heart_rate/average/<user_email>", methods=["GET"])
def heart_ave():
    """ Return user's average heart rate over all measurements

    """
    pass


@app.route("/api/heart_rate/interval_average", methods=["POST"])
def heart_int_ave():
    """ Calculate and return average heart rate for user since the time given

    """
    pass
