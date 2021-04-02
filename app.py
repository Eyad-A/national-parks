from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Park, UserPark 
import requests 
from secret import API_KEY, SECRET_KEY 
# from natlparks import NatlParks

# parks = NatlParks(API_KEY_CODE)
CURR_USER_KEY = "curr_user"

API_BASE_URL = "https://developer.nps.gov/api/v1"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///national-parks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

app.config['SECRET_KEY'] = SECRET_KEY 
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

url = f"{API_BASE_URL}/parks?parkCode=yose&api_key={API_KEY}" 
response = requests.get(url)
r = response.json() 

park_name = r['data'][0]['fullName']

@app.route("/")
def show_index():
    return render_template("base.html", park_name=park_name) 