"""
Workspace group member model for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, List, Literal
from uuid import UUID

from pydantic import Field, EmailStr

from .base import InstantlyModel

class WorkspaceGroupMember(InstantlyModel):
    """Model representing a workspace group member in Instantly.ai."""
    
    workspace_id: UUID = Field(..., description="The workspace ID this group member belongs to")
    group_id: UUID = Field(..., description="The ID of the group")
    user_id: UUID = Field(..., description="The ID of the user")
    role: Literal["admin", "member", "viewer"] = Field(
        ..., 
        description="Role of the user in the group"
    )
    email: EmailStr = Field(..., description="Email address of the user")
    first_name: Optional[str] = Field(None, description="First name of the user")
    last_name: Optional[str] = Field(None, description="Last name of the user")
    status: Literal["active", "invited", "suspended"] = Field(
        ..., 
        description="Current status of the group membership"
    )
    permissions: List[str] = Field(default_factory=list, description="List of specific permissions")
    created_at: datetime = Field(..., description="When the group membership was created")
    updated_at: datetime = Field(..., description="When the group membership was last updated")
    invited_at: Optional[datetime] = Field(None, description="When the user was invited to the group")
    joined_at: Optional[datetime] = Field(None, description="When the user joined the group")
    invited_by: Optional[UUID] = Field(None, description="ID of the user who invited this member") 