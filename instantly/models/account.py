"""
Account models for the Instantly.ai API
"""

from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from instantly.models.base import InstantlyModel

class Account(InstantlyModel):
    """Account model representing an email account that can be used to send campaigns."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "0196eed7-b516-7082-bd55-11a1e14138ca",
                "timestamp_created": "2025-05-20T17:57:16.182Z",
                "timestamp_updated": "2025-05-20T17:57:16.182Z",
                "email": "account@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "status": 1,
                "plan": "pro",
                "timezone": "UTC",
                "organization_id": "0196eed7-b516-7082-bd55-11a2cf42ba3f"
            }
        }
    )

    email: str = Field(..., description="The email address of the account")
    first_name: str = Field(..., description="The first name of the account owner")
    last_name: str = Field(..., description="The last name of the account owner")
    status: int = Field(..., description="The status of the account (e.g., 1 for 'active')")
    plan: str = Field(default="pro", description="The plan type of the account")
    timezone: str = Field(default="UTC", description="The timezone of the account")

class AccountCreate(BaseModel):
    """Model for creating a new account."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "account@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "timezone": "UTC"
            }
        }
    )

    email: str = Field(..., description="The email address of the account")
    first_name: str = Field(..., description="The first name of the account owner")
    last_name: str = Field(..., description="The last name of the account owner")
    timezone: str = Field(default="UTC", description="The timezone of the account")

class AccountUpdate(BaseModel):
    """Model for updating an existing account."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "timezone": "UTC"
            }
        }
    )

    first_name: Optional[str] = Field(None, description="The first name of the account owner")
    last_name: Optional[str] = Field(None, description="The last name of the account owner")
    timezone: Optional[str] = Field(None, description="The timezone of the account") 