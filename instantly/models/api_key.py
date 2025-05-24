"""
API key model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import Field

from .base import InstantlyModel

class APIKey(InstantlyModel):
    """Model representing an API key in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this API key belongs to")
    name: str = Field(..., description="The name of the API key")
    key: str = Field(..., description="The actual API key value")
    scopes: List[str] = Field(..., description="List of scopes this API key has access to")
    expires_at: Optional[datetime] = Field(None, description="Optional expiration date for the API key")
    last_used_at: Optional[datetime] = Field(None, description="When the API key was last used") 