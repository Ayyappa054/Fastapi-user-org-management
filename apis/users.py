from fastapi import FastAPI, APIRouter, Depends, HTTPException   
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from models.users import UserOrgBase 
from models.users import User, Organization, Website  
from schemas.users import UserCreate, User, OrganizationCreate, Organization, WebsiteCreate, Website, UserOrgBase,UserResponse


router = APIRouter() 

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new user
@router.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = UserCreate(firstname=user.firstname, lastname=user.lastname, Email=user.Email, Password=user.Password, Role=user.Role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Get a user by ID
@router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.User_id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Create an organization
@router.post("/organizations/", response_model=Organization)
def create_organization(organization: OrganizationCreate, db: Session = Depends(get_db)):
    db_org = Organization(
        orgname=organization.orgname,
        orgaddress=organization.orgaddress,
        Created_by=organization.Created_by,
    )
    db.add(db_org)
    db.commit()
    db.refresh(db_org)
    return db_org

# Get organization by ID
@router.get("/organizations/{org_id}", response_model=Organization)
def get_organization(org_id: int, db: Session = Depends(get_db)):
    db_org = db.query(Organization).filter(Organization.Org_id == org_id).first()
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_org

# Create a website
@router.post("/websites/", response_model=Website)
def create_website(website: WebsiteCreate, db: Session = Depends(get_db)):
    db_website = Website(
        Url=website.Url,
        Description=website.Description,
        Created_By=website.Created_By,
        Org_id=website.Org_id,
    )
    db.add(db_website)
    db.commit()
    db.refresh(db_website)
    return db_website

# Get websites by organization ID
@router.get("/websites/organization/{org_id}", response_model=List[Website])
def get_websites_by_org(org_id: int, db: Session = Depends(get_db)):
    db_websites = db.query(Website).filter(Website.Org_id == org_id).all()
    if not db_websites:
        raise HTTPException(status_code=404, detail="No websites found for this organization")
    return db_websites

# Create user-org relationship (Many-to-Many)
@router.post("/userorg/", response_model=UserOrgBase )
async def create_user_org(user_org: UserOrgBase, db: Session = Depends(get_db)):
    new_users = UserOrgBase (**user_org.dict())
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    return new_users
