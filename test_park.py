""" Test file"""
from unittest import TestCase 
from models import db, User, Park, UserPark 
from app import app 

db.create_all() 

class UserModelTestCase(TestCase):
    """Test the user model"""

    def setUp(self):
        """Create test client, add sample data"""

        db.drop_all()
        db.create_all()

        u1 = User.signup("test1", "password")
        uid1 = 1111
        u1.id = uid1         

        db.session.commit()

        u1 = User.query.get(uid1)          

        self.u1 = u1 
        self.uid1 = uid1       

        self.client = app.test_client()     

    def tearDown(self):
        res = super().tearDown() 
        db.session.rollback() 
        return res 

    def test_user_model(self):
        """Does basic model work?"""

        u = User.signup("yetanothertest", "password")
        uid = 888
        u.id = uid        

        p = Park(
            park_code="yose",
            full_name="Yosemite National Park"
        )

        db.session.add_all([u, p]) 
        db.session.commit()

        u.parks.append(p) 
        db.session.commit() 

        # User should have one favorite park
        self.assertEqual(len(u.parks), 1)