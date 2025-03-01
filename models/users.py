from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.ext.declarative import declarative_base
from database import Base


# User Model
class User(Base):
    __tablename__ = 'users'
    
    User_id = Column(Integer, primary_key=True, autoincrement= True)
    Firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    Password = Column(String(100), nullable=False)
    Role = Column(String(255), nullable=False)

    # Relationships
    organizations = relationship('Organization', back_populates='created_by')
    websites = relationship('Website', back_populates='created_by')
    user_orgs = relationship('UserOrg', back_populates='users')

 # Organization Model
class Organization(Base):
     __tablename__ = 'organization'

     Org_id = Column(Integer, primary_key=True)
     orgname = Column(String(100), nullable=False)
     orgaddress = Column(String(255), nullable=False)
     Created_by = Column(Integer, ForeignKey('users.User_id'), nullable=False)

     # Relationships
     created_by = relationship('User', back_populates='organizations')
     websites = relationship('Website', back_populates='organization')
     user_orgs = relationship('UserOrg', back_populates='organization')

# # Website Model
class Website(Base):
     __tablename__ = 'websites'

     id = Column(Integer, primary_key=True)
     Url = Column(String(255), nullable=False)
     Description = Column(String(255), nullable=True)
     Created_By = Column(Integer, ForeignKey('users.User_id'), nullable=False)
     Org_id = Column(Integer, ForeignKey('organization.Org_id'), nullable=False)

     # Relationships
     created_by = relationship('User', back_populates='websites')
     organization = relationship('Organization', back_populates='websites')

# # UserOrg Model (Many-to-Many Relationship Table)
class UserOrgBase(Base):
     __tablename__ = 'userorg'

     id = Column(Integer, primary_key=True, index=True)
     User_id = Column(Integer, ForeignKey('users.User_id'), primary_key=True)
     Org_id = Column(Integer, ForeignKey('organization.Org_id'), primary_key=True)

#     # Relationships
     user = relationship('User', back_populates='user_orgs')
     organization = relationship('Organization', back_populates='user_orgs')

