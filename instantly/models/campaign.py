"""
Campaign models for the Instantly.ai API
"""

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class CampaignSchedule(BaseModel):
    """Schedule settings for a campaign."""
    timezone: str
    start_time: str = Field(..., pattern=r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$")
    end_time: str = Field(..., pattern=r"^([01]?[0-9]|2[0-3]):[0-5][0-9]$")
    days: List[int] = Field(..., min_length=1, max_length=7)
    max_emails_per_day: Optional[int] = None

class CampaignCreate(BaseModel):
    """Data required to create a new campaign."""
    name: str
    schedule: CampaignSchedule
    email_list_id: str
    sequence_id: str
    daily_limit: Optional[int] = None
    stop_on_reply: bool = True
    stop_on_auto_reply: bool = True
    link_tracking: bool = True
    open_tracking: bool = True

class CampaignUpdate(BaseModel):
    """Data that can be updated for a campaign."""
    name: Optional[str] = None
    schedule: Optional[CampaignSchedule] = None
    daily_limit: Optional[int] = None
    stop_on_reply: Optional[bool] = None
    stop_on_auto_reply: Optional[bool] = None
    link_tracking: Optional[bool] = None
    open_tracking: Optional[bool] = None

class Campaign(BaseModel):
    """Campaign data returned by the API."""
    id: str
    name: str
    status: str
    schedule: CampaignSchedule
    email_list_id: str
    sequence_id: str
    daily_limit: Optional[int]
    stop_on_reply: bool
    stop_on_auto_reply: bool
    link_tracking: bool
    open_tracking: bool
    created_at: datetime
    updated_at: datetime 