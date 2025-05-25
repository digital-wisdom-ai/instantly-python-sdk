"""
API key model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, List, Literal
from uuid import UUID

from pydantic import BaseModel, Field, ConfigDict, field_serializer

from .base import InstantlyModel

class APIKey(InstantlyModel):
    """Model representing an API key in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this API key belongs to")
    name: str = Field(..., description="The name of the API key")
    key: str = Field(..., description="The API key value")
    scopes: List[str] = Field(..., description="List of permission scopes for this key")
    status: Literal["active", "inactive", "revoked"] = Field(
        ..., 
        description="Current status of the API key"
    )
    last_used_at: Optional[datetime] = Field(None, description="When the key was last used")
    created_at: datetime = Field(..., description="When the key was created")
    updated_at: datetime = Field(..., description="When the key was last updated")
    expires_at: Optional[datetime] = Field(None, description="Optional expiration date for the key")
    created_by: UUID = Field(..., description="ID of the user who created the key")
    description: Optional[str] = Field(None, description="Optional description of the key's purpose")

    @field_serializer("workspace_id", "created_by", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

class APIKeyCreate(BaseModel):
    """Model for creating a new API key."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Test API Key",
                "scopes": ["read", "write"],
                "expires_at": "2024-12-31T00:00:00Z"
            }
        }
    )

    name: str = Field(..., description="The name of the API key")
    scopes: List[str] = Field(..., description="List of scopes this API key has access to")
    expires_at: Optional[datetime] = Field(None, description="Optional expiration date for the API key") 