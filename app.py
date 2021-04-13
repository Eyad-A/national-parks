from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Park, UserPark 
import requests 
from secret import API_KEY, SECRET_KEY 
from forms import SignupForm, LoginForm 
import os 

API_BASE_URL = "https://developer.nps.gov/api/v1"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///national-parks'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app) 
db.create_all()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'sekkkkkret1') 


@app.route("/")
def show_index():
    return render_template("index.html") 

@app.route("/search", methods=['POST']) 
def handle_search():
    """handle park search and show search results"""

    search_query = request.form['search_query']
    search_url = f"{API_BASE_URL}/parks?q={search_query}&api_key={API_KEY}" 
    search_response = requests.get(search_url) 
    search_r = search_response.json()   
    
    return render_template("search.html", search_r=search_r)  


@app.route("/search-by-state", methods=['POST']) 
def handle_search_by_state():
    """handle park search and show search results"""

    state_query = request.form['state_query']
    search_url = f"{API_BASE_URL}/parks?stateCode={state_query}&api_key={API_KEY}" 
    search_response = requests.get(search_url) 
    search_r = search_response.json()   
    
    return render_template("search.html", search_r=search_r) 


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
    
    return render_template("park-details.html", park=park, places_r=places_r)   

    
@app.route("/<username>/favorite-parks")
def show_favorites(username):
    """Display user's favorite parks"""

    if "username" not in session or username != session['username']:        
        return redirect("/login") 
    
    user = User.query.filter_by(username=username).first()
    return render_template("favorite-parks.html", user=user)    


@app.route("/<username>/add-favorite/<park_code>", methods=['POST'])
def add_favorites(username, park_code):
    """Add park to favorites"""
    if "username" not in session:       
        return redirect("/login")
    
    user = User.query.filter_by(username=username).first()     
    favorited_park = Park.query.filter_by(park_code=park_code).one_or_none()
    main_image_url = request.form['main_image_url']
    full_name = request.form['full_name']

    # if park already in the DB 
    if favorited_park:
        user.parks.append(favorited_park)
        db.session.commit() 
        flash("Park has been added to favorites")
        return redirect("/<username>/favorite-parks")
    # if the park is not already in the DB 
    else:
        park = Park(park_code=park_code, main_image_url=main_image_url, full_name=full_name) 
        user.parks.append(park)
        db.session.commit() 
        flash("Favorite park has been added") 
        return redirect("/<username>/favorite-parks")


@app.route('/signup', methods=['GET', 'POST']) 
def signup():
    """Show signup form or handle form submission"""

    if "username" in session:
        return redirect(f"/{session['username']}/favorite-parks")

    form = SignupForm()

    if form.validate_on_submit():
        username = form.username.data 
        password = form.password.data 
        user = User.signup(username, password)

        db.session.commit() 
        session['username'] = user.username 

        flash("You have successfully signed up") 
        return redirect("/") 
    
    else: 
        return render_template("signup.html", form=form) 


@app.route('/login', methods=['GET', 'POST']) 
def login():
    """Display login form or handle login"""

    if "username" in session: 
        return redirect(f"/{session['username']}/favorite-parks") 
    
    form = LoginForm() 

    if form.validate_on_submit():
        username = form.username.data 
        password = form.password.data 

        user = User.authenticate(username, password)
        if user:
            session['username'] = user.username 
            flash("You have successfully logged in")
            return redirect(f"/{user.username}/favorite-parks") 
        else: 
            form.username.errors = ["Invalid username/password"] 
            return render_template("/login.html", form=form) 

    return render_template("/login.html", form=form) 


@app.route("/logout")
def logout():
    """Logout route"""

    session.pop("username")
    flash("You have been logged out")
    return redirect("/login") 

@app.route("/about")
def show_about():
    return render_template("about.html") 