from flask import Flask, request, render_template, redirect, url_for, flash, session


app = Flask(__name__)
app.secret_key = "f$0jg0sdis498yfoskjdf7g9aouhf48"  # Replace with a secure key in production

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')




