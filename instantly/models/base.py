"""
Base models for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional, Any

from pydantic import BaseModel, Field, ConfigDict

class InstantlyModel(BaseModel):
    """Base model for all Instantly.ai API entities."""
    
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        extra="allow",
        json_schema_extra={
            "example": {
                "id": "0196eed7-b516-7082-bd55-11a1e14138ca",
                "timestamp_created": "2025-05-20T17:57:16.182Z",
                "timestamp_updated": "2025-05-20T17:57:16.182Z"
            }
        }
    )

    id: str = Field(..., description="The unique identifier for the entity")
    timestamp_created: datetime = Field(..., description="When the entity was created")
    timestamp_updated: Optional[datetime] = Field(None, description="When the entity was last updated")
    organization_id: Optional[str] = Field(None, description="The workspace ID") 