"""
Tests for the Email Verification API endpoints
"""

import pytest
from unittest.mock import Mock, patch

from instantly import InstantlyClient, InstantlyConfig
from instantly.api.email_verification import EmailVerificationAPI

@pytest.fixture
def email_verification_api(config):
    """Create an EmailVerificationAPI instance for testing."""
    client = InstantlyClient(config)
    return EmailVerificationAPI(client)

def test_verify_email(email_verification_api):
    """Test verifying an email address."""
    email = "test@example.com"
    expected_data = {"email": email}
    
    with patch.object(email_verification_api._client, 'post') as mock_post:
        mock_post.return_value = {
            "email": email,
            "status": "valid",
            "score": 0.95
        }
        response = email_verification_api.verify_email(email)
        
        mock_post.assert_called_once_with("/email-verification", json=expected_data)
        assert response == {
            "email": email,
            "status": "valid",
            "score": 0.95
        }

def test_get_verification_status(email_verification_api):
    """Test getting verification status of an email."""
    email = "test@example.com"
    with patch.object(email_verification_api._client, 'get') as mock_get:
        mock_get.return_value = {
            "email": email,
            "status": "valid",
            "last_verified": "2024-03-20T12:00:00Z"
        }
        response = email_verification_api.get_verification_status(email)
        
        mock_get.assert_called_once_with(f"/email-verification/{email}")
        assert response == {
            "email": email,
            "status": "valid",
            "last_verified": "2024-03-20T12:00:00Z"
        } 