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

        u2 = User.signup("test2", "password")
        uid2 = 2222
        u2.id = uid2 

        db.session.commit()

        u1 = User.query.get(uid1) 
        u2 = User.query.get(uid2) 

        self.u1 = u1 
        self.uid1 = uid1 

        self.u2 = u2 
        self.uid2 = uid2 

        self.client = app.test_client() 

        self.client = app.test_client() 

    def tearDown(self):
        res = super().tearDown() 
        db.session.rollback() 
        return res 

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no favorite parks 
        self.assertEqual(len(u.parks), 0)
        
    def test_valid_signup(self):
        u_test = User.signup("testtesttest", "password")
        uid = 99999
        u_test.id = uid
        db.session.commit()

        u_test = User.query.get(uid)
        self.assertIsNotNone(u_test)
        self.assertEqual(u_test.username, "testtesttest")        
        self.assertNotEqual(u_test.password, "password")
        # Bcrypt strings should start with $2b$
        self.assertTrue(u_test.password.startswith("$2b$"))

    def test_valid_authentication(self):
        u = User.authenticate(self.u1.username, "password")
        self.assertIsNotNone(u)
        self.assertEqual(u.id, self.uid1)