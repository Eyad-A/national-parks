from app import app
from models import db, User 

db.drop_all()
db.create_all()

# u1 = User(
#     username="eyad",
#     password="eyad123",
# )

# u2 = User(
#     username="jay",
#     password="jay123", 
# )

# db.session.add_all([u1, u2])
# db.session.commit()