"""
Campaign models for the Instantly.ai API
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

from instantly.models.base import InstantlyModel

class AutoVariantSelect(BaseModel):
    """Auto variant selection settings."""
    trigger: str = Field(..., description="The trigger for auto variant selection (e.g., 'click_rate')")

class Campaign(InstantlyModel):
    """Campaign model representing a campaign that can be sent to a list of recipients."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "0196eed7-b516-7082-bd55-11a1e14138ca",
                "timestamp_created": "2025-05-20T17:57:16.182Z",
                "timestamp_updated": "2025-05-20T17:57:16.182Z",
                "name": "My Campaign",
                "email_gap": 10,
                "random_wait_max": 10,
                "text_only": False,
                "email_list": ["john@doe.com"],
                "daily_limit": 100,
                "stop_on_reply": False,
                "email_tag_list": ["0196eed7-b516-7082-bd55-11a1e14138ca"],
                "link_tracking": True,
                "open_tracking": True,
                "stop_on_auto_reply": False,
                "daily_max_leads": 100,
                "prioritize_new_leads": False,
                "auto_variant_select": {"trigger": "click_rate"},
                "match_lead_esp": False,
                "stop_for_company": False,
                "insert_unsubscribe_header": False,
                "allow_risky_contacts": False,
                "disable_bounce_protect": False,
                "cc_list": ["john@doe.com"],
                "bcc_list": ["john@doe.com"],
                "organization_id": "0196eed7-b516-7082-bd55-11a2cf42ba3f"
            }
        }
    )

    name: str = Field(..., description="The name of the campaign")
    email_gap: int = Field(..., description="The gap between emails in minutes")
    random_wait_max: int = Field(..., description="Maximum random wait time in minutes")
    text_only: bool = Field(..., description="Whether to send text-only emails")
    email_list: List[str] = Field(..., description="List of email addresses to send to")
    daily_limit: int = Field(..., description="Maximum number of emails to send per day")
    stop_on_reply: bool = Field(..., description="Whether to stop sending when a reply is received")
    email_tag_list: List[str] = Field(..., description="List of email tag IDs")
    link_tracking: bool = Field(..., description="Whether to track link clicks")
    open_tracking: bool = Field(..., description="Whether to track email opens")
    stop_on_auto_reply: bool = Field(..., description="Whether to stop on auto-replies")
    daily_max_leads: int = Field(..., description="Maximum number of leads to process per day")
    prioritize_new_leads: bool = Field(..., description="Whether to prioritize new leads")
    auto_variant_select: Optional[AutoVariantSelect] = Field(None, description="Auto variant selection settings")
    match_lead_esp: bool = Field(..., description="Whether to match lead ESP")
    stop_for_company: bool = Field(..., description="Whether to stop for company")
    insert_unsubscribe_header: bool = Field(..., description="Whether to insert unsubscribe header")
    allow_risky_contacts: bool = Field(..., description="Whether to allow risky contacts")
    disable_bounce_protect: bool = Field(..., description="Whether to disable bounce protection")
    cc_list: List[str] = Field(..., description="List of CC email addresses")
    bcc_list: List[str] = Field(..., description="List of BCC email addresses")

class CampaignCreate(BaseModel):
    """Model for creating a new campaign."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "My Campaign",
                "email_gap": 10,
                "random_wait_max": 10,
                "text_only": False,
                "email_list": ["john@doe.com"],
                "daily_limit": 100,
                "stop_on_reply": False,
                "email_tag_list": ["0196eed7-b516-7082-bd55-11a1e14138ca"],
                "link_tracking": True,
                "open_tracking": True,
                "stop_on_auto_reply": False,
                "daily_max_leads": 100,
                "prioritize_new_leads": False,
                "auto_variant_select": {"trigger": "click_rate"},
                "match_lead_esp": False,
                "stop_for_company": False,
                "insert_unsubscribe_header": False,
                "allow_risky_contacts": False,
                "disable_bounce_protect": False,
                "cc_list": ["john@doe.com"],
                "bcc_list": ["john@doe.com"]
            }
        }
    )

    name: str = Field(..., description="The name of the campaign")
    email_gap: int = Field(..., description="The gap between emails in minutes")
    random_wait_max: int = Field(..., description="Maximum random wait time in minutes")
    text_only: bool = Field(..., description="Whether to send text-only emails")
    email_list: List[str] = Field(..., description="List of email addresses to send to")
    daily_limit: int = Field(..., description="Maximum number of emails to send per day")
    stop_on_reply: bool = Field(..., description="Whether to stop sending when a reply is received")
    email_tag_list: List[str] = Field(..., description="List of email tag IDs")
    link_tracking: bool = Field(..., description="Whether to track link clicks")
    open_tracking: bool = Field(..., description="Whether to track email opens")
    stop_on_auto_reply: bool = Field(..., description="Whether to stop on auto-replies")
    daily_max_leads: int = Field(..., description="Maximum number of leads to process per day")
    prioritize_new_leads: bool = Field(..., description="Whether to prioritize new leads")
    auto_variant_select: Optional[AutoVariantSelect] = Field(None, description="Auto variant selection settings")
    match_lead_esp: bool = Field(..., description="Whether to match lead ESP")
    stop_for_company: bool = Field(..., description="Whether to stop for company")
    insert_unsubscribe_header: bool = Field(..., description="Whether to insert unsubscribe header")
    allow_risky_contacts: bool = Field(..., description="Whether to allow risky contacts")
    disable_bounce_protect: bool = Field(..., description="Whether to disable bounce protection")
    cc_list: List[str] = Field(..., description="List of CC email addresses")
    bcc_list: List[str] = Field(..., description="List of BCC email addresses")

class CampaignUpdate(BaseModel):
    """Model for updating an existing campaign."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Updated Campaign Name",
                "email_gap": 15,
                "random_wait_max": 15,
                "text_only": True,
                "daily_limit": 150,
                "stop_on_reply": True,
                "link_tracking": False,
                "open_tracking": False,
                "stop_on_auto_reply": True,
                "daily_max_leads": 150,
                "prioritize_new_leads": True,
                "auto_variant_select": {"trigger": "open_rate"},
                "match_lead_esp": True,
                "stop_for_company": True,
                "insert_unsubscribe_header": True,
                "allow_risky_contacts": True,
                "disable_bounce_protect": True,
                "cc_list": ["jane@doe.com"],
                "bcc_list": ["jane@doe.com"]
            }
        }
    )

    name: Optional[str] = Field(None, description="The name of the campaign")
    email_gap: Optional[int] = Field(None, description="The gap between emails in minutes")
    random_wait_max: Optional[int] = Field(None, description="Maximum random wait time in minutes")
    text_only: Optional[bool] = Field(None, description="Whether to send text-only emails")
    daily_limit: Optional[int] = Field(None, description="Maximum number of emails to send per day")
    stop_on_reply: Optional[bool] = Field(None, description="Whether to stop sending when a reply is received")
    link_tracking: Optional[bool] = Field(None, description="Whether to track link clicks")
    open_tracking: Optional[bool] = Field(None, description="Whether to track email opens")
    stop_on_auto_reply: Optional[bool] = Field(None, description="Whether to stop on auto-replies")
    daily_max_leads: Optional[int] = Field(None, description="Maximum number of leads to process per day")
    prioritize_new_leads: Optional[bool] = Field(None, description="Whether to prioritize new leads")
    auto_variant_select: Optional[AutoVariantSelect] = Field(None, description="Auto variant selection settings")
    match_lead_esp: Optional[bool] = Field(None, description="Whether to match lead ESP")
    stop_for_company: Optional[bool] = Field(None, description="Whether to stop for company")
    insert_unsubscribe_header: Optional[bool] = Field(None, description="Whether to insert unsubscribe header")
    allow_risky_contacts: Optional[bool] = Field(None, description="Whether to allow risky contacts")
    disable_bounce_protect: Optional[bool] = Field(None, description="Whether to disable bounce protection")
    cc_list: Optional[List[str]] = Field(None, description="List of CC email addresses")
    bcc_list: Optional[List[str]] = Field(None, description="List of BCC email addresses") 