"""
Custom tag model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import Field, field_serializer

from .base import InstantlyModel

class CustomTag(InstantlyModel):
    """Model representing a custom tag in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this tag belongs to")
    name: str = Field(..., description="The name of the tag")
    color: str = Field(..., description="The color of the tag in hex format")
    description: Optional[str] = Field(None, description="Optional description of the tag")
    resource_ids: List[UUID] = Field(default_factory=list, description="List of resource IDs this tag is applied to")

    @field_serializer("workspace_id", "resource_ids", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v) 