"""
Email API endpoints for Instantly.ai
"""

from typing import List, Optional, Dict, Any
from datetime import datetime

from ..client import InstantlyClient

class EmailAPI:
    """Email API endpoints."""

    def __init__(self, client: InstantlyClient):
        self._client = client

    def reply(self, thread_id: str, subject: str, body: str, to_address: str, 
              cc_address: Optional[str] = None, bcc_address: Optional[str] = None,
              reply_to: Optional[str] = None) -> Dict[str, Any]:
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
            Dict containing the created email details
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

        return self._client.post("/emails/reply", json=data)

    def list_emails(self, page: int = 1, per_page: int = 50) -> Dict[str, Any]:
        """
        List emails.

        Args:
            page: Page number for pagination
            per_page: Number of items per page

        Returns:
            Dict containing list of emails and pagination info
        """
        params = {"page": page, "per_page": per_page}
        return self._client.get("/emails", params=params)

    def get_email(self, email_id: str) -> Dict[str, Any]:
        """
        Get a specific email by ID.

        Args:
            email_id: The ID of the email to retrieve

        Returns:
            Dict containing email details
        """
        return self._client.get(f"/emails/{email_id}")

    def update_email(self, email_id: str, **kwargs) -> Dict[str, Any]:
        """
        Update an email's properties.

        Args:
            email_id: The ID of the email to update
            **kwargs: Fields to update (subject, body, etc.)

        Returns:
            Dict containing updated email details
        """
        return self._client.patch(f"/emails/{email_id}", json=kwargs)

    def delete_email(self, email_id: str) -> Dict[str, Any]:
        """
        Delete an email.

        Args:
            email_id: The ID of the email to delete

        Returns:
            Dict containing success status
        """
        return self._client.delete(f"/emails/{email_id}")

    def get_unread_count(self) -> Dict[str, int]:
        """
        Get count of unread emails.

        Returns:
            Dict containing count of unread emails
        """
        return self._client.get("/emails/unread/count")

    def mark_thread_as_read(self, thread_id: str) -> Dict[str, bool]:
        """
        Mark all emails in a thread as read.

        Args:
            thread_id: The ID of the thread to mark as read

        Returns:
            Dict containing success status
        """
        return self._client.post(f"/emails/threads/{thread_id}/mark-as-read") 