"""
Audit log model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, Dict, Any, Literal
from uuid import UUID

from pydantic import Field, field_serializer

from .base import InstantlyModel

class AuditLog(InstantlyModel):
    """Model representing an audit log entry in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this audit log belongs to")
    user_id: UUID = Field(..., description="The ID of the user who performed the action")
    action: str = Field(..., description="The action that was performed")
    resource_type: str = Field(..., description="The type of resource that was affected")
    resource_id: UUID = Field(..., description="The ID of the resource that was affected")
    changes: Optional[Dict[str, Any]] = Field(None, description="Details of the changes made")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata about the action")
    ip_address: Optional[str] = Field(None, description="IP address from which the action was performed")
    user_agent: Optional[str] = Field(None, description="User agent of the client that performed the action")
    created_at: datetime = Field(..., description="When the audit log entry was created")
    status: Literal["success", "failure"] = Field(..., description="Status of the action")
    error_message: Optional[str] = Field(None, description="Error message if the action failed")

    @field_serializer("workspace_id", "user_id", "resource_id", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v) 