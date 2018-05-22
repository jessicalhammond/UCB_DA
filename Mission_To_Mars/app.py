import pandas as pd
import requests
from selenium import webdriver
import mission

from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo

app = Flask(__name__, static_url_path='/static')

mongo = PyMongo(app)

@app.route("/")
def index():
    mars_data = mongo.db.mars_data.find_one()
    return render_template("index.html", mars_data=mars_data)

@app.route("/team")
def team():
    return render_template("team.html")

@app.route("/stories")
def stories():
    return render_template("stories.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/scrape")
def scraper():
    data = mongo.db.mars_data
    scrape_data = mission.scrape()
    data.update(
        {},
        scrape_data,
        upsert=True
    )
    return redirect("http://localhost:5000/", code=302)

if __name__ == "__main__":
    app.run(debug=True)