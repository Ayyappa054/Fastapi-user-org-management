from enum import Enum
from pydantic import BaseModel
from typing import Optional

class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"

class UserCreate(BaseModel):
    firstname: str
    lastname: str
    Email: str
    Password: str
    Role: RoleEnum

class UserResponse(BaseModel):
    User_id : int
    firstname: str
    lastname: str
    Email: str
    Password: str
    Role: str
    created_by: int

class User(UserCreate):
    User_id: Optional[int] = None


    class Config:
        from_attributes = True

class OrganizationBase(BaseModel):
    orgname: str
    orgaddress: str

class OrganizationCreate(OrganizationBase):
    pass

class Organization(OrganizationBase):
    Org_id: int
    Created_by: int

    class Config:
        from_attributes = True

class WebsiteBase(BaseModel):
    Url: str
    Description: str

class WebsiteCreate(WebsiteBase):
    pass

class Website(WebsiteBase):
    id: int
    Created_By: int
    Org_id: int

    class Config:
        from_attributes = True

class UserOrgBase(BaseModel):
    User_id: int
    Org_id: int

class UserOrgCreate(UserOrgBase):  
    pass

class UserOrg(UserOrgBase):      
    id: int

    class Config:
        from_attributes = True
