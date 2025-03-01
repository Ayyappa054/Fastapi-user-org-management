FastAPI User Organization Management API
Overview
This is a FastAPI-based API that allows users to manage:

Users (Create, Retrieve)
Organizations (Create, Retrieve)
Websites (Create, Retrieve)
User-Organization Relationships (Many-to-Many)
Features
✅ RESTful API with CRUD operations
✅ SQLAlchemy ORM for database interactions
✅ Pydantic models for request validation
✅ Dependency injection for database session management

Technologies Used
FastAPI (Web framework)
SQLAlchemy (ORM for database interactions)
Pydantic (Data validation)
SQLite / PostgreSQL / MySQL (Database support)

Installation
1. Clone the Repository
git clone https://github.com/your-username/fastapi-user-org-management.git
cd fastapi-user-org-management
2. Set Up a Virtual Environment
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
3. Install Dependencies
pip install -r requirements.txt
4. Set Up the Database
Modify database.py to configure your database connection.
5. Run the FastAPI Application
uvicorn main:app --reload
It will start the server at http://127.0.0.1:8000.

API Endpoints
User Endpoints
POST /users/ - Create a new user
GET /users/{user_id} - Get a user by ID
Organization Endpoints
POST /organizations/ - Create an organization
GET /organizations/{org_id} - Get an organization by ID
Website Endpoints
POST /websites/ - Create a website
GET /websites/organization/{org_id} - Get websites by organization
User-Organization Relationship
POST /userorg/ - Create a user-organization relationship
Testing the API
After running the application, open Swagger UI at:
🔗 http://127.0.0.1:8000/docs

Contributing
Feel free to fork this repository, create a branch, and submit pull requests!

License
MIT License
