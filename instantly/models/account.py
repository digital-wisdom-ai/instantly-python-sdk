"""
Account models for the Instantly.ai API
"""

from typing import Optional

from pydantic import BaseModel, Field, ConfigDict

from instantly.models.base import InstantlyModel

class Account(BaseModel):
    model_config = ConfigDict(extra="allow")
    id: str = Field(alias="email")
    created_at: str = Field(alias="timestamp_created")
    updated_at: str = Field(alias="timestamp_updated")
    first_name: str
    last_name: str
    status: int  # e.g., 1 for 'active'
    plan: str = Field(default="pro")
    timezone: str = Field(default="UTC")

class AccountCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    timezone: str = Field(default="UTC")

class AccountUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    timezone: str | None = None 