"""
Workspace model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, List, Dict, Any, Literal
from uuid import UUID

from pydantic import Field, EmailStr, field_serializer

from .base import InstantlyModel

class Workspace(InstantlyModel):
    """Model representing a workspace in Instantly.ai."""
    
    id: UUID = Field(..., description="The unique identifier of the workspace")
    name: str = Field(..., description="The name of the workspace")
    description: Optional[str] = Field(None, description="Optional description of the workspace")
    status: Literal["active", "suspended", "archived"] = Field(
        ..., 
        description="Current status of the workspace"
    )
    plan: str = Field(..., description="The subscription plan of the workspace")
    owner_id: UUID = Field(..., description="ID of the workspace owner")
    settings: Dict[str, Any] = Field(default_factory=dict, description="Workspace settings")
    features: List[str] = Field(default_factory=list, description="List of enabled features")
    created_at: datetime = Field(..., description="When the workspace was created")
    updated_at: datetime = Field(..., description="When the workspace was last updated")
    trial_ends_at: Optional[datetime] = Field(None, description="When the trial period ends")
    billing_email: Optional[EmailStr] = Field(None, description="Email address for billing notifications")
    timezone: str = Field(default="UTC", description="Timezone of the workspace")
    language: str = Field(default="en", description="Language preference of the workspace")
    custom_domain: Optional[str] = Field(None, description="Custom domain for the workspace")
    logo_url: Optional[str] = Field(None, description="URL of the workspace logo")

    @field_serializer("id", "owner_id", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v) 