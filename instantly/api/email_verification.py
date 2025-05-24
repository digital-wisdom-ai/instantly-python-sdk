"""
Email Verification API endpoints for Instantly.ai
"""

from typing import Dict, Any

from ..client import InstantlyClient

class EmailVerificationAPI:
    """Email Verification API endpoints."""

    def __init__(self, client: InstantlyClient):
        self._client = client

    def verify_email(self, email: str) -> Dict[str, Any]:
        """
        Verify an email address.

        Args:
            email: The email address to verify

        Returns:
            Dict containing verification results
        """
        data = {"email": email}
        return self._client.post("/email-verification", json=data)

    def get_verification_status(self, email: str) -> Dict[str, Any]:
        """
        Get the verification status of an email address.

        Args:
            email: The email address to check

        Returns:
            Dict containing verification status
        """
        return self._client.get(f"/email-verification/{email}") 