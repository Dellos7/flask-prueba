from flask import Flask, render_template, request, url_for
from markupsafe import escape
import mysql.connector

# Python MySQL: https://www.w3schools.com/python/python_mysql_getstarted.asp

app = Flask(__name__)

@app.route('/')
def hello():
    mydb = mysql.connector.connect(
        host="localhost",
        user="david",
        password="12345678",
        database="ejercicios_html_php"
    )
    print(mydb)

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM ejercicio3")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

    return '<p><b>Hello</b>, <u>World! (bbdd)</u></p>'
