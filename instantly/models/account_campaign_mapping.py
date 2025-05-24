"""
Account campaign mapping model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import InstantlyModel

class AccountCampaignMapping(InstantlyModel):
    """Model representing an account campaign mapping in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this mapping belongs to")
    account_id: UUID = Field(..., description="The ID of the account")
    campaign_id: UUID = Field(..., description="The ID of the campaign")
    is_active: bool = Field(..., description="Whether this mapping is active")
    last_used_at: Optional[datetime] = Field(None, description="When this mapping was last used") 