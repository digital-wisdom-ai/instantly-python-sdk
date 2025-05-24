"""
Block list entry model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, Literal
from uuid import UUID

from pydantic import Field

from .base import InstantlyModel

class BlockListEntry(InstantlyModel):
    """Model representing a block list entry in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this entry belongs to")
    type: Literal["email", "domain"] = Field(..., description="The type of block list entry")
    value: str = Field(..., description="The email or domain to block")
    reason: Optional[str] = Field(None, description="Optional reason for blocking")
    expires_at: Optional[datetime] = Field(None, description="Optional expiration date for the block") 