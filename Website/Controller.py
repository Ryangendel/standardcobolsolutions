from flask import Flask, render_template
# from Models import IceCreamStore,Sharks, connectionInstatiator
# from sqlalchemy.orm import sessionmaker, scoped_session
# import psycopg2
# from sqlalchemy import create_engine

app = Flask(__name__)

viewDirectory = "./Views/"

@app.route("/")
def home():
    return render_template(f"{viewDirectory}index.html")

@app.route("/Services")
def services():
    return render_template(f"{viewDirectory}services.html")