from datetime import datetime
from typing import Optional, Dict, Any, List, Literal
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_serializer

class LeadStatusSummary(BaseModel):
    from_: str = Field(alias="from")
    step_id: str
    timestamp_executed: datetime

class LeadStatusSummarySubseq(BaseModel):
    from_: str = Field(alias="from")
    step_id: str
    timestamp_executed: datetime

class ListLeadsRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    limit: Optional[int] = Field(default=100, ge=1, le=100)
    starting_after: Optional[str] = None
    campaign: Optional[UUID] = None
    list_id: Optional[UUID] = None
    status: Optional[Literal[1, 2, 3, -1, -2, -3]] = Field(
        description="1: Active, 2: Paused, 3: Completed, -1: Bounced, -2: Unsubscribed, -3: Skipped"
    )
    interest_status: Optional[Literal[1, 2, 3]] = Field(
        description="1: Interested, 2: Not Interested, 3: Maybe Later"
    )
    verification_status: Optional[int] = None
    enrichment_status: Optional[Literal[1, 11, -1, -2]] = Field(
        description="1: Enriched, 11: Pending, -1: Not Available, -2: Error"
    )
    assigned_to: Optional[UUID] = None
    uploaded_by_user: Optional[UUID] = None
    upload_method: Optional[Literal["manual", "api", "website-visitor"]] = None
    is_website_visitor: Optional[bool] = None
    esp_code: Optional[Literal[0, 1, 2, 3, 9, 10, 12, 13, 999, 1000]] = Field(
        description="0: In Queue, 1: Google, 2: Microsoft, 3: Zoho, 9: Yahoo, 10: Yandex, 12: Web.de, 13: Libero.it, 999: Other, 1000: Not Found"
    )

    @field_serializer("campaign", "list_id", "assigned_to", "uploaded_by_user", mode="plain")
    def serialize_uuid(cls, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

class LeadCreateRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    company_name: Optional[str] = None
    company_domain: Optional[str] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    personalization: Optional[str] = None
    campaign: Optional[UUID] = None
    list_id: Optional[UUID] = None

    @field_serializer("campaign", "list_id", mode="plain")
    def serialize_uuid(cls, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

class LeadUpdateRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    company_name: Optional[str] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    personalization: Optional[str] = None
    assigned_to: Optional[UUID] = None
    lt_interest_status: Optional[int] = None  # See API docs for enum values
    pl_value_lead: Optional[str] = None
    custom_variables: Optional[Dict[str, Any]] = None

    @field_serializer("assigned_to", mode="plain")
    def serialize_uuid(cls, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

class LeadMergeRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    primary_lead_id: str
    secondary_lead_id: str

class LeadInterestStatusRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    lead_id: str
    status: Literal[1, 2, 3] = Field(description="1: Interested, 2: Not Interested, 3: Maybe Later")

class LeadSubsequenceRemoveRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    lead_id: str

class LeadBulkAssignRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    lead_ids: List[str]
    user_id: str

class LeadMoveRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    lead_ids: List[str]
    target_id: str
    target_type: Literal["campaign", "list"]

class LeadExportRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    lead_ids: List[str]
    app_id: str

class LeadSubsequenceMoveRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    lead_id: str
    subsequence_id: str

class Lead(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    id: str
    timestamp_created: datetime
    timestamp_updated: datetime
    organization: UUID
    campaign: Optional[UUID] = None
    status: Optional[int] = None
    email: str
    personalization: Optional[str] = None
    website: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    company_name: Optional[str] = None
    phone: Optional[str] = None
    email_open_count: Optional[int] = 0
    email_reply_count: Optional[int] = 0
    email_click_count: Optional[int] = 0
    company_domain: Optional[str] = None
    status_summary: Optional[LeadStatusSummary] = None
    payload: Optional[Dict[str, Any]] = None
    status_summary_subseq: Optional[LeadStatusSummarySubseq] = None
    last_step_from: Optional[str] = None
    last_step_id: Optional[str] = None
    last_step_timestamp_executed: Optional[datetime] = None
    email_opened_step: Optional[int] = None
    email_opened_variant: Optional[int] = None
    email_replied_step: Optional[int] = None
    email_replied_variant: Optional[int] = None
    email_clicked_step: Optional[int] = None
    email_clicked_variant: Optional[int] = None
    lt_interest_status: Optional[int] = None
    subsequence_id: Optional[UUID] = None
    verification_status: Optional[int] = None
    pl_value_lead: Optional[str] = None
    timestamp_added_subsequence: Optional[datetime] = None
    timestamp_last_contact: Optional[datetime] = None
    timestamp_last_open: Optional[datetime] = None
    timestamp_last_reply: Optional[datetime] = None
    timestamp_last_interest_change: Optional[datetime] = None
    timestamp_last_click: Optional[datetime] = None
    enrichment_status: Optional[int] = None
    list_id: Optional[UUID] = None
    last_contacted_from: Optional[str] = None
    uploaded_by_user: Optional[UUID] = None
    upload_method: Optional[str] = None
    assigned_to: Optional[UUID] = None
    is_website_visitor: Optional[bool] = None
    timestamp_last_touch: Optional[datetime] = None
    esp_code: Optional[int] = None

    @field_serializer("timestamp_created", "timestamp_updated", "last_step_timestamp_executed", "timestamp_added_subsequence", "timestamp_last_contact", "timestamp_last_open", "timestamp_last_reply", "timestamp_last_interest_change", "timestamp_last_click", "timestamp_last_touch", mode="plain")
    def serialize_datetime(cls, v: Optional[datetime]):
        if v is None:
            return None
        return v.isoformat().replace('+00:00', 'Z')

    @field_serializer("organization", "campaign", "subsequence_id", "list_id", "uploaded_by_user", "assigned_to", mode="plain")
    def serialize_uuid(cls, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

class BulkAssignLeadsResult(BaseModel):
    model_config = ConfigDict(validate_by_name=True)
    assigned_count: int
    user_id: UUID
    lead_ids: List[str]

    @field_serializer("user_id", mode="plain")
    def serialize_uuid(cls, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

class MoveLeadsResult(BaseModel):
    model_config = ConfigDict(validate_by_name=True)
    moved_count: int
    target_id: UUID
    target_type: Literal["campaign", "list"]
    lead_ids: List[str]
    job_id: Optional[str] = None  # background job id if async

    @field_serializer("target_id", mode="plain")
    def serialize_uuid(cls, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

class ExportLeadsResult(BaseModel):
    model_config = ConfigDict(validate_by_name=True)
    exported_count: int
    app_id: str
    lead_ids: List[str]
    job_id: Optional[str] = None  # background job id if async 