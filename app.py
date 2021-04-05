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

@app.route("/")
def show_index():
    return render_template("index.html") 

@app.route("/search", methods=['POST']) 
def handle_search():
    """handle park search and show search results"""

    search_query = request.form['search_query']
    search_url = f"{API_BASE_URL}/parks?q={search_query}&limit=30&api_key={API_KEY}" 
    search_response = requests.get(search_url) 
    search_r = search_response.json()
    
    search_list = []
    for item in search_r['data']:
        search_list.append(item) 
    
    return render_template("search.html", search_list=search_list)


@app.route("/search-by-state", methods=['POST']) 
def handle_search_by_state():
    """handle park search and show search results"""

    state_query = request.form['state_query']
    search_url = f"{API_BASE_URL}/parks?stateCode={state_query}&limit=30&api_key={API_KEY}" 
    search_response = requests.get(search_url) 
    search_r = search_response.json()
    
    search_list = []
    for item in search_r['data']:
        search_list.append(item) 
    
    return render_template("search.html", search_list=search_list)


@app.route("/park-details", methods=['POST']) 
def show_park():
    """Show park details"""

    # Fetch park details 
    park_code = request.form['park_code'] 
    park_url = f"{API_BASE_URL}/parks?parkCode={park_code}&api_key={API_KEY}"
    park_response = requests.get(park_url)
    park_r = park_response.json() 
    park = park_r['data'][0]

    # Fetch places associated with this park 
    places_url = f"{API_BASE_URL}/places?parkCode={park_code}&limit=3&api_key={API_KEY}"
    places_response = requests.get(places_url)
    places_r = places_response.json() 
    places_list = []
    for place in places_r['data']:
        places_list.append(place)  


    return render_template("park-details.html", park=park, places_list=places_list)   

    
    