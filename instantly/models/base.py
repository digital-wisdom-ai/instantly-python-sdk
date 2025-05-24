"""
Base models for the Instantly.ai API
"""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

class InstantlyModel(BaseModel):
    """Base model for all Instantly.ai API entities."""
    
    id: str = Field(..., description="The unique identifier for the entity")
    created_at: datetime = Field(..., description="When the entity was created")
    updated_at: Optional[datetime] = Field(None, description="When the entity was last updated")
    
    model_config = ConfigDict(from_attributes=True, populate_by_name=True) 