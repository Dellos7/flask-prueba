from flask import Flask, render_template, request, url_for
from markupsafe import escape
import mysql.connector

# Python MySQL: https://www.w3schools.com/python/python_mysql_getstarted.asp

app = Flask(__name__)

@app.route('/')
def hello():
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword"
    )
    print(mydb)
    return '<p><b>Hello</b>, <u>World!</u></p>'
