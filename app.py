from flask import Flask, render_template, request, flash
import logging as logger
logger.basicConfig(level="DEBUG")


app = Flask(__name__)

@app.route("/")
def home():
    flash("Hey there! what's your name?")
    return render_template("home.html")

@app.route("/hello", methods=["POST", "GET"])
def hello():
    flash("HEY " + str(request.form['name_input']) + ", NICE TO MEET YOU!")
    return render_template("home.html")


app.secret_key = 'super secret key'

if __name__ == '__main__':
    logger.debug("Starting Flask App")
    app.run(debug=True, host='0.0.0.0')