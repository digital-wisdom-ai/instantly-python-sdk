"""
Workspace member model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, List, Literal
from uuid import UUID

from pydantic import Field, EmailStr

from .base import InstantlyModel

class WorkspaceMember(InstantlyModel):
    """Model representing a workspace member in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this member belongs to")
    user_id: UUID = Field(..., description="The ID of the user")
    role: Literal["owner", "admin", "member", "viewer"] = Field(
        ..., 
        description="Role of the user in the workspace"
    )
    email: EmailStr = Field(..., description="Email address of the user")
    first_name: Optional[str] = Field(None, description="First name of the user")
    last_name: Optional[str] = Field(None, description="Last name of the user")
    status: Literal["active", "invited", "suspended"] = Field(
        ..., 
        description="Current status of the workspace membership"
    )
    permissions: List[str] = Field(default_factory=list, description="List of specific permissions")
    created_at: datetime = Field(..., description="When the workspace membership was created")
    updated_at: datetime = Field(..., description="When the workspace membership was last updated")
    invited_at: Optional[datetime] = Field(None, description="When the user was invited to the workspace")
    joined_at: Optional[datetime] = Field(None, description="When the user joined the workspace")
    invited_by: Optional[UUID] = Field(None, description="ID of the user who invited this member")
    last_active_at: Optional[datetime] = Field(None, description="When the user was last active")
    two_factor_enabled: bool = Field(default=False, description="Whether two-factor authentication is enabled")
    groups: List[UUID] = Field(default_factory=list, description="List of group IDs the user belongs to") 