"""
Campaign subsequence model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, List, Dict, Any, Literal
from uuid import UUID

from pydantic import Field, field_serializer

from .base import InstantlyModel

class CampaignSubsequence(InstantlyModel):
    """Model representing a campaign subsequence in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this subsequence belongs to")
    campaign_id: UUID = Field(..., description="The ID of the parent campaign")
    name: str = Field(..., description="The name of the subsequence")
    description: Optional[str] = Field(None, description="Optional description of the subsequence")
    status: Literal["active", "paused", "completed", "archived"] = Field(
        ..., 
        description="Current status of the subsequence"
    )
    trigger_type: Literal["immediate", "delayed", "conditional"] = Field(
        ..., 
        description="Type of trigger for this subsequence"
    )
    trigger_delay: Optional[int] = Field(None, description="Delay in minutes before starting the subsequence")
    trigger_condition: Optional[Dict[str, Any]] = Field(None, description="Condition that must be met to trigger the subsequence")
    steps: List[Dict[str, Any]] = Field(..., description="List of steps in the subsequence")
    created_at: datetime = Field(..., description="When the subsequence was created")
    updated_at: datetime = Field(..., description="When the subsequence was last updated")
    started_at: Optional[datetime] = Field(None, description="When the subsequence was started")
    completed_at: Optional[datetime] = Field(None, description="When the subsequence was completed")
    created_by: UUID = Field(..., description="ID of the user who created the subsequence")
    last_modified_by: UUID = Field(..., description="ID of the user who last modified the subsequence")

    @field_serializer("workspace_id", "campaign_id", "created_by", "last_modified_by", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v) 