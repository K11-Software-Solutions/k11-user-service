from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="User Service",
    description="Manages user accounts and profiles for the K11 platform",
    version="1.0.0",
)


class User(BaseModel):
    id: str
    email: str
    name: str
    avatar_url: Optional[str] = None


class CreateUser(BaseModel):
    email: str
    name: str


class ContactInfo(BaseModel):
    email: str
    phone: Optional[str] = None


@app.get("/api/v2/users", response_model=list[User], tags=["users"])
async def list_users(page: int = 1, page_size: int = 20):
    """List all users with pagination."""
    return []


@app.get("/api/v2/users/{id}", response_model=User, tags=["users"])
async def get_user(id: str):
    """Get a user by ID."""
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/api/v2/users", response_model=User, status_code=201, tags=["users"])
async def create_user(body: CreateUser):
    """Create a new user account."""
    return User(id="generated-id", email=body.email, name=body.name)


@app.get("/api/v2/users/{id}/contact", response_model=ContactInfo, tags=["users"])
async def get_user_contact(id: str):
    """Get a user's contact information."""
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/health")
async def health():
    return {"status": "ok", "service": "user-service", "version": "1.0.0"}
