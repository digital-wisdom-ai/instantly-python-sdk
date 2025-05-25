"""
Lead List models for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict

from instantly.models.base import InstantlyModel

class LeadList(InstantlyModel):
    """Lead List model representing a list used to store leads."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "0196eed7-b516-7082-bd55-11a1e14138ca",
                "timestamp_created": "2025-05-20T17:57:16.182Z",
                "timestamp_updated": "2025-05-20T17:57:16.182Z",
                "name": "My Lead List",
                "description": "A list of leads for my campaign",
                "organization_id": "0196eed7-b516-7082-bd55-11a2cf42ba3f",
                "lead_count": 100,
                "is_archived": False,
                "is_deleted": False,
                "created_by": "0196eed7-b516-7082-bd55-11a3e14138ca",
                "updated_by": "0196eed7-b516-7082-bd55-11a3e14138ca"
            }
        }
    )

    name: str = Field(..., description="The name of the lead list")
    description: Optional[str] = Field(None, description="A description of the lead list")
    lead_count: int = Field(..., description="The number of leads in the list")
    is_archived: bool = Field(..., description="Whether the list is archived")
    is_deleted: bool = Field(..., description="Whether the list is deleted")
    created_by: str = Field(..., description="The ID of the user who created the list")
    updated_by: str = Field(..., description="The ID of the user who last updated the list")

class LeadListCreate(BaseModel):
    """Model for creating a new lead list."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "My Lead List",
                "description": "A list of leads for my campaign"
            }
        }
    )

    name: str = Field(..., description="The name of the lead list")
    description: Optional[str] = Field(None, description="A description of the lead list")

class LeadListUpdate(BaseModel):
    """Model for updating an existing lead list."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Updated Lead List Name",
                "description": "Updated description"
            }
        }
    )

    name: Optional[str] = Field(None, description="The name of the lead list")
    description: Optional[str] = Field(None, description="A description of the lead list") 