"""
Email models for the Instantly.ai API
"""

from datetime import datetime
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, ConfigDict

from instantly.models.base import InstantlyModel

class EmailBody(BaseModel):
    """Email body content in both text and HTML formats."""
    text: str = Field(..., description="Text content of the email")
    html: Optional[str] = Field(None, description="HTML content of the email")

class Email(InstantlyModel):
    """Email model representing a campaign email, a reply, a manually sent email, or any other email that's visible in the Unibox."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "0196eed7-b534-73c3-89c3-59983154bb30",
                "timestamp_created": "2025-05-20T17:57:16.212Z",
                "timestamp_email": "2025-05-20T17:57:16.212Z",
                "message_id": "<example123@mail.gmail.com>",
                "subject": "Re: Your inquiry",
                "to_address_email_list": "recipient@example.com",
                "body": {
                    "text": "This is a test email",
                    "html": "<p>This is a test email</p>"
                },
                "organization_id": "0196eed7-b534-73c3-89c3-599910a8191a",
                "eaccount": "eaccount-123",
                "from_address_email": "sender@example.com",
                "cc_address_email_list": "cc@example.com",
                "bcc_address_email_list": "bcc@example.com",
                "reply_to": "replyto@example.com",
                "campaign_id": "0196eed7-b534-73c3-89c3-599ab314f890",
                "subsequence_id": "0196eed7-b534-73c3-89c3-599b9efd35a3",
                "list_id": "0196eed7-b534-73c3-89c3-599c4518a8fa",
                "lead": "jondoe@example.com",
                "lead_id": "0196eed7-b534-73c3-89c3-599dcef61345",
                "ue_type": 3,
                "step": "step-123",
                "is_unread": True,
                "is_auto_reply": False,
                "reminder_ts": "2025-05-20T17:57:16.212Z",
                "ai_interest_value": 0.75,
                "ai_assisted": 1,
                "is_focused": 1,
                "i_status": 0,
                "thread_id": "0196eed7-b534-73c3-89c3-599e9a10d0dd",
                "content_preview": "This is a preview of the email content.",
                "from_address_json": None,
                "to_address_json": None,
                "cc_address_json": None
            }
        }
    )

    timestamp_email: datetime = Field(..., description="The timestamp of the email, as provided by the email server")
    message_id: str = Field(..., description="Unique email ID from the email server")
    subject: str = Field(..., description="Subject line of the email message")
    to_address_email_list: str = Field(..., description="Comma-separated list of recipient email addresses")
    body: EmailBody = Field(..., description="An object containing the email body in HTML and text format")
    eaccount: str = Field(..., description="The email account that was used to send the email")
    from_address_email: Optional[str] = Field(None, description="The sender email address")
    cc_address_email_list: Optional[str] = Field(None, description="Comma-separated list of CC email addresses")
    bcc_address_email_list: Optional[str] = Field(None, description="Comma-separated list of BCC email addresses")
    reply_to: Optional[str] = Field(None, description="Reply-to email address")
    campaign_id: Optional[str] = Field(None, description="The id of the campaign that the email is associated with")
    subsequence_id: Optional[str] = Field(None, description="The id of the campaign subsequence that the email is associated with")
    list_id: Optional[str] = Field(None, description="The id of the list (if the lead is part of a list)")
    lead: Optional[str] = Field(None, description="The email address of the lead that the email is associated with")
    lead_id: Optional[str] = Field(None, description="The lead id (if any)")
    ue_type: Optional[int] = Field(None, description="Email type based on the life cycle of the email")
    step: Optional[str] = Field(None, description="The campaign step that the email is associated with")
    is_unread: Optional[bool] = Field(None, description="Indicates if the email is unread")
    is_auto_reply: Optional[bool] = Field(None, description="Indicates if the email is an auto-reply")
    reminder_ts: Optional[datetime] = Field(None, description="Timestamp for the reminder")
    ai_interest_value: Optional[float] = Field(None, description="AI interest value")
    ai_assisted: Optional[int] = Field(None, description="Indicates if AI assistance was used")
    is_focused: Optional[int] = Field(None, description="Indicates if the email is focused (is in the primary tab in the Unibox)")
    i_status: Optional[int] = Field(None, description="Indicates the interest status of the email")
    thread_id: Optional[str] = Field(None, description="Identifier for the email thread")
    content_preview: Optional[str] = Field(None, description="A short preview of the email content")
    from_address_json: Optional[List[Any]] = Field(None, description="List of from address details")
    to_address_json: Optional[List[Any]] = Field(None, description="List of to address details")
    cc_address_json: Optional[List[Any]] = Field(None, description="List of CC address details")

class EmailCreate(BaseModel):
    """Model for creating a new email."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "subject": "Your inquiry",
                "to_address_email_list": "recipient@example.com",
                "body": {
                    "text": "This is a test email",
                    "html": "<p>This is a test email</p>"
                },
                "eaccount": "eaccount-123",
                "cc_address_email_list": "cc@example.com",
                "bcc_address_email_list": "bcc@example.com",
                "reply_to": "replyto@example.com",
                "campaign_id": "0196eed7-b534-73c3-89c3-599ab314f890",
                "subsequence_id": "0196eed7-b534-73c3-89c3-599b9efd35a3",
                "list_id": "0196eed7-b534-73c3-89c3-599c4518a8fa",
                "lead": "jondoe@example.com",
                "lead_id": "0196eed7-b534-73c3-89c3-599dcef61345",
                "step": "step-123"
            }
        }
    )

    subject: str = Field(..., description="Subject line of the email message")
    to_address_email_list: str = Field(..., description="Comma-separated list of recipient email addresses")
    body: EmailBody = Field(..., description="An object containing the email body in HTML and text format")
    eaccount: str = Field(..., description="The email account that was used to send the email")
    cc_address_email_list: Optional[str] = Field(None, description="Comma-separated list of CC email addresses")
    bcc_address_email_list: Optional[str] = Field(None, description="Comma-separated list of BCC email addresses")
    reply_to: Optional[str] = Field(None, description="Reply-to email address")
    campaign_id: Optional[str] = Field(None, description="The id of the campaign that the email is associated with")
    subsequence_id: Optional[str] = Field(None, description="The id of the campaign subsequence that the email is associated with")
    list_id: Optional[str] = Field(None, description="The id of the list (if the lead is part of a list)")
    lead: Optional[str] = Field(None, description="The email address of the lead that the email is associated with")
    lead_id: Optional[str] = Field(None, description="The lead id (if any)")
    step: Optional[str] = Field(None, description="The campaign step that the email is associated with")

class EmailUpdate(BaseModel):
    """Model for updating an existing email."""
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "subject": "Updated subject",
                "body": {
                    "text": "Updated text content",
                    "html": "<p>Updated HTML content</p>"
                },
                "cc_address_email_list": "newcc@example.com",
                "bcc_address_email_list": "newbcc@example.com",
                "reply_to": "newreplyto@example.com",
                "is_unread": True,
                "reminder_ts": "2025-05-20T17:57:16.212Z"
            }
        }
    )

    subject: Optional[str] = Field(None, description="Subject line of the email message")
    body: Optional[EmailBody] = Field(None, description="An object containing the email body in HTML and text format")
    cc_address_email_list: Optional[str] = Field(None, description="Comma-separated list of CC email addresses")
    bcc_address_email_list: Optional[str] = Field(None, description="Comma-separated list of BCC email addresses")
    reply_to: Optional[str] = Field(None, description="Reply-to email address")
    is_unread: Optional[bool] = Field(None, description="Indicates if the email is unread")
    reminder_ts: Optional[datetime] = Field(None, description="Timestamp for the reminder")

class EmailReplyResponse(InstantlyModel):
    """Response model for email reply operation."""
    id: str = Field(..., description="The ID of the created email")
    thread_id: str = Field(..., description="The ID of the email thread")
    timestamp_created: datetime = Field(..., description="When the email was created")
    subject: str = Field(..., description="Subject line of the email")
    to_address_email_list: str = Field(..., description="Comma-separated list of recipient email addresses")
    body: EmailBody = Field(..., description="Email body content")
    from_address_email: str = Field(..., description="Sender email address")
    cc_address_email_list: Optional[str] = Field(None, description="Comma-separated list of CC email addresses")
    bcc_address_email_list: Optional[str] = Field(None, description="Comma-separated list of BCC email addresses")
    reply_to: Optional[str] = Field(None, description="Reply-to email address")

class EmailListResponse(InstantlyModel):
    """Response model for listing emails."""
    items: List[Email] = Field(..., description="List of emails")
    total: int = Field(..., description="Total number of emails")
    page: int = Field(..., description="Current page number")
    per_page: int = Field(..., description="Number of items per page")

class UnreadCountResponse(InstantlyModel):
    """Response model for unread email count."""
    count: int = Field(..., description="Number of unread emails")

class MarkAsReadResponse(InstantlyModel):
    """Response model for marking thread as read."""
    success: bool = Field(..., description="Whether the operation was successful") 