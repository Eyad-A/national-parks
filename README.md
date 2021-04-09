# National Parks
## An app that allows you to search for US national parks and view information such as location and ongoing events. 

### API used: 
[National Park Service](https://www.nps.gov/subjects/developer/index.htm) 

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
