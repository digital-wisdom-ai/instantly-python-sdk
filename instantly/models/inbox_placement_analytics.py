"""
Inbox placement analytics model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, Dict, Any, List
from uuid import UUID

from pydantic import Field, field_serializer

from .base import InstantlyModel

class InboxPlacementAnalytics(InstantlyModel):
    """Model representing inbox placement analytics in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID these analytics belong to")
    test_id: UUID = Field(..., description="The ID of the associated inbox placement test")
    email_provider: str = Field(..., description="The email provider being tested")
    placement_status: str = Field(..., description="The placement status (inbox, spam, etc.)")
    delivery_time: Optional[datetime] = Field(None, description="When the test email was delivered")
    open_time: Optional[datetime] = Field(None, description="When the test email was opened")
    spam_score: Optional[float] = Field(None, description="Spam score assigned by the provider")
    headers: Optional[Dict[str, Any]] = Field(None, description="Email headers from the test")
    authentication_results: Optional[Dict[str, Any]] = Field(None, description="Authentication results (SPF, DKIM, DMARC)")
    created_at: datetime = Field(..., description="When the analytics were created")
    updated_at: datetime = Field(..., description="When the analytics were last updated")

    @field_serializer("workspace_id", "test_id", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v) 