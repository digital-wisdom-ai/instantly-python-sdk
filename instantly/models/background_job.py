"""
Background job model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, Dict, Any, Literal
from uuid import UUID

from pydantic import Field, field_serializer

from .base import InstantlyModel

class BackgroundJob(InstantlyModel):
    """Model representing a background job in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this job belongs to")
    user_id: Optional[UUID] = Field(None, description="The user ID that triggered this job")
    type: Literal["move-leads", "import-leads", "export-leads"] = Field(
        ..., 
        description="The type of background job"
    )
    entity_id: Optional[UUID] = Field(None, description="The ID of the entity this job is related to")
    entity_type: Optional[Literal["list", "campaign"]] = Field(
        None, 
        description="The type of entity this job is related to"
    )
    data: Dict[str, Any] = Field(default_factory=dict, description="Additional data about the job")
    progress: int = Field(..., ge=0, le=100, description="Progress of the job as a percentage")
    status: Literal["pending", "in-progress", "success", "failed"] = Field(
        ..., 
        description="Current status of the job"
    )

    @field_serializer("workspace_id", "user_id", "entity_id", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v) 