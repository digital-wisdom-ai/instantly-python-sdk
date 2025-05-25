from datetime import datetime
from typing import Optional, Dict, Any, List, Literal
from uuid import UUID
from pydantic import BaseModel, Field, EmailStr, ConfigDict, field_serializer

class LeadStatusSummary(BaseModel):
    from_: Optional[str] = Field(alias="from", default=None)
    step_id: Optional[str] = None
    timestamp_executed: Optional[datetime] = None

class LeadStatusSummarySubseq(BaseModel):
    from_: Optional[str] = Field(alias="from", default=None)
    step_id: Optional[str] = None
    timestamp_executed: Optional[datetime] = None

class ListLeadsRequest(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    limit: Optional[int] = Field(default=100, ge=1, le=100)
    starting_after: Optional[str] = Field(default=None)
    campaign: Optional[UUID] = Field(default=None)
    list_id: Optional[UUID] = Field(default=None)
    status: Optional[Literal[1, 2, 3, -1, -2, -3]] = Field(
        default=None,
        description="1: Active, 2: Paused, 3: Completed, -1: Bounced, -2: Unsubscribed, -3: Skipped"
    )
    interest_status: Optional[Literal[1, 2, 3]] = Field(
        default=None,
        description="1: Interested, 2: Not Interested, 3: Maybe Later"
    )
    verification_status: Optional[int] = Field(default=None)
    enrichment_status: Optional[Literal[1, 11, -1, -2]] = Field(
        default=None,
        description="1: Enriched, 11: Pending, -1: Not Available, -2: Error"
    )
    assigned_to: Optional[UUID] = Field(default=None)
    uploaded_by_user: Optional[UUID] = Field(default=None)
    upload_method: Optional[Literal["manual", "api", "website-visitor"]] = Field(default=None)
    is_website_visitor: Optional[bool] = Field(default=None)
    esp_code: Optional[Literal[0, 1, 2, 3, 9, 10, 12, 13, 999, 1000]] = Field(
        default=None,
        description="0: In Queue, 1: Google, 2: Microsoft, 3: Zoho, 9: Yahoo, 10: Yandex, 12: Web.de, 13: Libero.it, 999: Other, 1000: Not Found"
    )

    @field_serializer("campaign", "list_id", "assigned_to", "uploaded_by_user", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
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
    def serialize_uuid(self, v: Optional[UUID]):
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
    def serialize_uuid(self, v: Optional[UUID]):
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

    search: Optional[str] = Field(
        default=None,
        description="A search string to search the leads against - can be First Name, Last Name, or Email"
    )
    filter: Optional[Literal[
        "FILTER_VAL_CONTACTED",
        "FILTER_VAL_NOT_CONTACTED",
        "FILTER_VAL_COMPLETED",
        "FILTER_VAL_UNSUBSCRIBED",
        "FILTER_VAL_ACTIVE",
        "FILTER_LEAD_INTERESTED",
        "FILTER_LEAD_NOT_INTERESTED",
        "FILTER_LEAD_MEETING_BOOKED",
        "FILTER_LEAD_MEETING_COMPLETED",
        "FILTER_LEAD_CLOSED"
    ]] = Field(
        default=None,
        description="Filter criteria for leads. For custom lead labels, use the interest_status field."
    )
    campaign: Optional[UUID] = Field(
        default=None,
        description="Campaign ID to filter leads"
    )
    list_id: Optional[UUID] = Field(
        default=None,
        description="List ID to filter leads"
    )
    in_campaign: Optional[bool] = Field(
        default=None,
        description="Whether the lead is in a campaign"
    )
    in_list: Optional[bool] = Field(
        default=None,
        description="Whether the lead is in a list"
    )
    ids: Optional[List[str]] = Field(
        default=None,
        description="Array of lead IDs to include"
    )
    queries: Optional[List[Dict[str, Any]]] = Field(
        default=None,
        description="Array of query objects"
    )
    excluded_ids: Optional[List[str]] = Field(
        default=None,
        description="Array of lead IDs to exclude"
    )
    contacts: Optional[List[str]] = Field(
        default=None,
        description="Array of emails the leads needs to have"
    )
    to_campaign_id: Optional[UUID] = Field(
        default=None,
        description="Campaign ID to move leads to"
    )
    to_list_id: Optional[UUID] = Field(
        default=None,
        description="List ID to move leads to"
    )
    check_duplicates_in_campaigns: Optional[bool] = Field(
        default=None,
        description="Whether to check for duplicates in campaigns"
    )
    skip_leads_in_verification: Optional[bool] = Field(
        default=None,
        description="Whether to skip leads in verification"
    )
    limit: Optional[int] = Field(
        default=None,
        description="Maximum number of leads to move"
    )
    assigned_to: Optional[UUID] = Field(
        default=None,
        description="User ID to assign leads to"
    )
    esp_code: Optional[Literal[0, 1, 2, 3, 9, 10, 12, 13, 999, 1000]] = Field(
        default=None,
        description="Email service provider code: 0: In Queue, 1: Google, 2: Microsoft, 3: Zoho, 9: Yahoo, 10: Yandex, 12: Web.de, 13: Libero.it, 999: Other, 1000: Not Found"
    )
    copy_leads: Optional[bool] = Field(
        default=None,
        description="Whether to copy leads instead of moving them"
    )

    @field_serializer("campaign", "list_id", "to_campaign_id", "to_list_id", "assigned_to", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

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
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

class BulkAssignLeadsResult(BaseModel):
    model_config = ConfigDict(validate_by_name=True)
    assigned_count: int
    user_id: UUID
    lead_ids: List[str]

    @field_serializer("user_id", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

class MoveLeadsResult(BaseModel):
    model_config = ConfigDict(validate_by_name=True)

    id: str = Field(
        description="Unique identifier for the background job"
    )
    workspace_id: UUID = Field(
        description="Workspace ID"
    )
    type: Literal["move-leads", "import-leads", "export-leads"] = Field(
        description="Type of background job"
    )
    progress: int = Field(
        ge=0,
        le=100,
        description="Progress of the job as a percentage (from 0 to 100)"
    )
    status: Literal["pending", "in-progress", "success", "failed"] = Field(
        description="Job status"
    )
    created_at: datetime = Field(
        description="Timestamp when the job was created"
    )
    updated_at: datetime = Field(
        description="Timestamp when the job was last updated"
    )
    user_id: Optional[UUID] = Field(
        default=None,
        description="The id of the user that triggered the action that created the job"
    )
    entity_id: Optional[UUID] = Field(
        default=None,
        description="The id of the entity that the job is related to"
    )
    entity_type: Optional[Literal["list", "campaign"]] = Field(
        default=None,
        description="Type of entity"
    )
    data: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Data about the job, used to store any additional information we need to process the job"
    )

    @field_serializer("workspace_id", "user_id", "entity_id", mode="plain")
    def serialize_uuid(self, v: Optional[UUID]):
        if v is None:
            return None
        return str(v)

    @field_serializer("created_at", "updated_at", mode="plain")
    def serialize_datetime(self, v: Optional[datetime]):
        if v is None:
            return None
        return v.isoformat().replace('+00:00', 'Z')

class ExportLeadsResult(BaseModel):
    model_config = ConfigDict(validate_by_name=True)
    exported_count: int
    app_id: str
    lead_ids: List[str]
    job_id: Optional[str] = None  # background job id if async 