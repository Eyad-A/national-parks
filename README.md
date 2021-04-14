# National Parks
## An app that allows you to search for US national parks and view information such as location and ongoing events.

### Website link: 
Deployed on Heroku here: 
https://national-parks-finder.herokuapp.com/

### API used: 
[National Park Service](https://www.nps.gov/subjects/developer/index.htm) 

### Description:
Users can search for a park or select a state to see all the available parks in that state. 
From the search results, users can click on any park to view more details about that park. 
Content includes images, climate information, park activities, and places within the park 
to visit. Logged in users can save parks to their favorite lists to view them later. 

### Tech used: 
- Python
- Flask
- SQLAlchemy
- Bootstrap 


### Change log: 

**April 1, 2020**
- Create database schema 
- Install dependencies 
- Create repo
  
**April 2, 2020**
- Update models.py
- Add base.html, seed.py, and app.py
- Successfully test API calls to display park's information 

**April 4, 2020**
- Add search form to search by park name
- Add search form to search by state
- Add /search route to handle search by park name
- Add /search-by-state route to handle search by state
- Add search.html page to display results of search

**April 5, 2020**
- Add park-details route 
- Add park-details.html to display park information
- Add navigation bar
- Add index.html

**April 6, 2020**
- Implement user registeration and authentication functionality
- Install Flask-WTForms and add login and sign up forms 
- Add login.html to be used for login and signup forms 
- Add favorite-parks route and favorite-parks.html
- Add signup route
- Add login route
- Add logout route 

**April 9, 2020**
- Add 'add to favorites' functionality. Parks can now be favorited by users and be added 
  correctly in the DB.
- Update '/<username>/add-favorite/<park_code>' route
- Update '/<username>/favorite-parks' route
- 'Add to favorites' button now only shows if user is logged in

**April 10, 2020**
- Add user model test cases
- Update Park model to include park's name 
  
**April 11, 2020**
- Add hero image and styling
- Add styling for homepage
- Add footer.html
- Add about.html 

**April 12, 2020**
- Add styling to search results, favorite parks, login, and signup pages 
- Update nav bar to include favorite parks 
- Add conditionals to handle parks that have missing data 
- Bug fixes 

**April 13, 2020**
- Add styling to flash messages
- Add test cases for parks 
- bug fixes 
- Add Procfile and runtime
- Add environmental variables 
- Deploy 