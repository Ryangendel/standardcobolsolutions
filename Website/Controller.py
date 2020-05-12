from flask import Flask, render_template, request
from Website.Model import connectionInstantiator, ContactForm, contactFormModel

# from Models import IceCreamStore,Sharks, connectionInstatiator
# from sqlalchemy.orm import sessionmaker, scoped_session
# import psycopg2
# from sqlalchemy import create_engine

app = Flask(__name__)
connectionString ='sqlite:///C:\\Users\\NT_WIN10\\Desktop\\Coball\\Website\\testDatabase.db'
viewDirectory = "Views/"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Services")
def services():
    return render_template("services.html")

@app.route("/Contact", methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        
        db = connectionInstantiator(connectionString)
        # contactTable = ContactFormTable(db.scopedSession)
        contactTable = ContactForm()

        newContact: contactFormModel = contactFormModel(
            firstName = request.form["firstName"],
            lastName = request.form["lastName"],
            email = request.form["email"],
            organization = request.form["organization"],
            phoneNumber = request.form["phoneNumber"],
            message = request.form["message"]
        )
        if contactTable.insert(newContact):
            return render_template("contactResponse.html")
        else:
            return "DB ERROR"
    else:
        return render_template("contact.html")