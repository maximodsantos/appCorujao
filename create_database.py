# create_database.py
from app.database import Base, get_db_params, Session
from app.models.user import Admin
from app.tools.utils import generate_password

# Import all your models here
from app.models.user import User, Admin, Professor
from app.models.group import Group
from app.models.student import Student

clear_db, engine = get_db_params()

# If clear_db is true, drop all tables
if clear_db:
    Base.metadata.drop_all(engine)

# Create all tables
Base.metadata.create_all(engine)

# Create a Session
session = Session()

# Check if any user exists
if session.query(User).count() == 0:
    # If not, create an admin user
    admin_password = generate_password()
    print(f"Generated admin password: {admin_password}")
    admin = Admin(name='Admin User', email='admin@admin.com.br', status='Active')
    admin.password = admin_password  # Assuming you have a password field and a way to hash the password
    session.add(admin)
    session.commit()




# >^<\|Fj1=P