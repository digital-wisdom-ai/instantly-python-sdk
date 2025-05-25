"""
Inbox placement test model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, List, Dict, Any, Literal
from uuid import UUID

from pydantic import Field, EmailStr

from .base import InstantlyModel

class InboxPlacementTest(InstantlyModel):
    """Model representing an inbox placement test in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this test belongs to")
    name: str = Field(..., description="The name of the test")
    description: Optional[str] = Field(None, description="Optional description of the test")
    from_email: EmailStr = Field(..., description="The sender email address")
    subject: str = Field(..., description="The subject line of the test email")
    body: Dict[str, Any] = Field(..., description="The email body content")
    test_emails: List[EmailStr] = Field(..., description="List of email addresses to test with")
    status: Literal["pending", "in_progress", "completed", "failed"] = Field(
        ..., 
        description="Current status of the test"
    )
    results: Optional[Dict[str, Any]] = Field(None, description="Test results data")
    created_at: datetime = Field(..., description="When the test was created")
    updated_at: datetime = Field(..., description="When the test was last updated")
    completed_at: Optional[datetime] = Field(None, description="When the test was completed")
    error_message: Optional[str] = Field(None, description="Error message if the test failed") 