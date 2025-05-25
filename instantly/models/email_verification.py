"""
Email Verification models for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict, EmailStr

from instantly.models.base import InstantlyModel

class EmailVerification(InstantlyModel):
    """Email Verification model representing a single email verification."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "0196eed7-b516-7082-bd55-11a1e14138ca",
                "timestamp_created": "2025-05-20T17:57:16.182Z",
                "timestamp_updated": "2025-05-20T17:57:16.182Z",
                "email": "test@example.com",
                "status": "valid",
                "organization_id": "0196eed7-b516-7082-bd55-11a2cf42ba3f"
            }
        }
    )

    email: EmailStr = Field(..., description="The email address to verify")
    status: str = Field(..., description="The verification status of the email")

class EmailVerificationCreate(BaseModel):
    """Model for creating a new email verification."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "email": "test@example.com"
            }
        }
    )

    email: EmailStr = Field(..., description="The email address to verify") 