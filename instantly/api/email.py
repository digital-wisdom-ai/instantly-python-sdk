"""
Email API endpoints for Instantly.ai
"""

from typing import List, Optional, Dict, Any
from datetime import datetime

from ..client import InstantlyClient
from ..models.email import (
    EmailUpdate, Email, EmailReplyResponse, 
    EmailListResponse, UnreadCountResponse, 
    MarkAsReadResponse
)

class EmailAPI:
    """Email API endpoints."""

    def __init__(self, client: InstantlyClient):
        self._client = client

    def reply(self, thread_id: str, subject: str, body: str, to_address: str, 
              cc_address: Optional[str] = None, bcc_address: Optional[str] = None,
              reply_to: Optional[str] = None) -> EmailReplyResponse:
        """
        Reply to an email thread.

        Args:
            thread_id: The ID of the thread to reply to
            subject: Subject line of the email
            body: Body of the email
            to_address: Recipient email address
            cc_address: Optional CC email addresses (comma-separated)
            bcc_address: Optional BCC email addresses (comma-separated)
            reply_to: Optional reply-to email address

        Returns:
            EmailReplyResponse containing the created email details
        """
        data = {
            "thread_id": thread_id,
            "subject": subject,
            "body": body,
            "to_address": to_address,
        }
        if cc_address:
            data["cc_address"] = cc_address
        if bcc_address:
            data["bcc_address"] = bcc_address
        if reply_to:
            data["reply_to"] = reply_to

        response = self._client.post("/emails/reply", json=data)
        return EmailReplyResponse(**response)

    def list_emails(self, page: int = 1, per_page: int = 50) -> EmailListResponse:
        """
        List emails.

        Args:
            page: Page number for pagination
            per_page: Number of items per page

        Returns:
            EmailListResponse containing list of emails and pagination info
        """
        params = {"page": page, "per_page": per_page}
        response = self._client.get("/emails", params=params)
        return EmailListResponse(**response)

    def get_email(self, email_id: str) -> Email:
        """
        Get a specific email by ID.

        Args:
            email_id: The ID of the email to retrieve

        Returns:
            Email object containing email details
        """
        response = self._client.get(f"/emails/{email_id}")
        return Email(**response)

    def update_email(self, email_id: str, data: EmailUpdate) -> Email:
        """
        Update an email's properties.

        Args:
            email_id: The ID of the email to update
            data: EmailUpdate model containing the fields to update

        Returns:
            Email object containing updated email details
        """
        response = self._client.patch(f"/emails/{email_id}", json=data.model_dump(exclude_none=True))
        return Email(**response)

    def delete_email(self, email_id: str) -> None:
        """
        Delete an email.

        Args:
            email_id: The ID of the email to delete
        """
        self._client.delete(f"/emails/{email_id}")

    def get_unread_count(self) -> UnreadCountResponse:
        """
        Get count of unread emails.

        Returns:
            UnreadCountResponse containing count of unread emails
        """
        response = self._client.get("/emails/unread/count")
        return UnreadCountResponse(**response)

    def mark_thread_as_read(self, thread_id: str) -> MarkAsReadResponse:
        """
        Mark all emails in a thread as read.

        Args:
            thread_id: The ID of the thread to mark as read

        Returns:
            MarkAsReadResponse containing success status
        """
        response = self._client.post(f"/emails/threads/{thread_id}/mark-as-read")
        return MarkAsReadResponse(**response) 