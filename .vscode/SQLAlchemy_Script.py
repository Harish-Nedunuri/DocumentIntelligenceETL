from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, Sequence, inspect
from sqlalchemy import create_engine, Column, Integer, String, Sequence, inspect
from sqlalchemy.orm import sessionmaker, declarative_base

# Replace the placeholders with your actual database credentials
DATABASE_URL = "postgresql://postgres:buddy2701@localhost:5432/DBdemo"

# Create an engine instance
engine = create_engine(DATABASE_URL)

# Create a base class for declarative models
Base = declarative_base()

# Define the User class
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)

    def __repr__(self):
        return f"<User(name='{self.name}', age={self.age})>"

# Check if the table already exists and create if it doesn't
if not inspect(engine).has_table(User.__tablename__):
    Base.metadata.create_all(engine)
else:
    print("Table already exists.")

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example of adding a new user
new_user = User(name='John Doe', age=30)
session.add(new_user)
session.commit()

# Close the session
session.close()
