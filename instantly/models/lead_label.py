"""
Lead label model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field, field_serializer

from .base import InstantlyModel

class LeadLabel(InstantlyModel):
    """Model representing a lead label in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this label belongs to")
    name: str = Field(..., description="The name of the label")
    color: str = Field(..., description="The color of the label in hex format")
    description: Optional[str] = Field(None, description="Optional description of the label")

    @field_serializer("workspace_id", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v) 