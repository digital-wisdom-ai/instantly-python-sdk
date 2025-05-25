"""
Inbox placement blacklist model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import Field, EmailStr, field_serializer

from .base import InstantlyModel

class InboxPlacementBlacklist(InstantlyModel):
    """Model representing an inbox placement blacklist in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this blacklist belongs to")
    email: EmailStr = Field(..., description="The blacklisted email address")
    reason: Optional[str] = Field(None, description="Optional reason for blacklisting")
    source: str = Field(..., description="Source of the blacklist entry (e.g., 'manual', 'system', 'test')")
    test_id: Optional[UUID] = Field(None, description="ID of the test that triggered the blacklist")
    created_at: datetime = Field(..., description="When the blacklist entry was created")
    updated_at: datetime = Field(..., description="When the blacklist entry was last updated")
    expires_at: Optional[datetime] = Field(None, description="Optional expiration date for the blacklist entry")

    @field_serializer("workspace_id", "test_id", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v) 