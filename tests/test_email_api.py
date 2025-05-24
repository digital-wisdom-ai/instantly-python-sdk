"""
Tests for the Email API endpoints
"""

import pytest
from unittest.mock import Mock, patch

from instantly import InstantlyClient, InstantlyConfig
from instantly.api.email import EmailAPI

@pytest.fixture
def email_api(config):
    """Create an EmailAPI instance for testing."""
    client = InstantlyClient(config)
    return EmailAPI(client)

def test_reply_to_email(email_api):
    """Test replying to an email thread."""
    thread_id = "test-thread-123"
    subject = "Test Reply"
    body = "This is a test reply"
    to_address = "test@example.com"
    
    expected_data = {
        "thread_id": thread_id,
        "subject": subject,
        "body": body,
        "to_address": to_address
    }
    
    with patch.object(email_api._client, 'post') as mock_post:
        mock_post.return_value = {"id": "test-email-123"}
        response = email_api.reply(thread_id, subject, body, to_address)
        
        mock_post.assert_called_once_with("/emails/reply", json=expected_data)
        assert response == {"id": "test-email-123"}

def test_list_emails(email_api):
    """Test listing emails."""
    with patch.object(email_api._client, 'get') as mock_get:
        mock_get.return_value = {"emails": [], "total": 0}
        response = email_api.list_emails(page=2, per_page=25)
        
        mock_get.assert_called_once_with("/emails", params={"page": 2, "per_page": 25})
        assert response == {"emails": [], "total": 0}

def test_get_email(email_api):
    """Test getting a specific email."""
    email_id = "test-email-123"
    with patch.object(email_api._client, 'get') as mock_get:
        mock_get.return_value = {"id": email_id}
        response = email_api.get_email(email_id)
        
        mock_get.assert_called_once_with(f"/emails/{email_id}")
        assert response == {"id": email_id}

def test_update_email(email_api):
    """Test updating an email."""
    email_id = "test-email-123"
    update_data = {"subject": "Updated Subject"}
    
    with patch.object(email_api._client, 'patch') as mock_patch:
        mock_patch.return_value = {"id": email_id, "subject": "Updated Subject"}
        response = email_api.update_email(email_id, **update_data)
        
        mock_patch.assert_called_once_with(f"/emails/{email_id}", json=update_data)
        assert response == {"id": email_id, "subject": "Updated Subject"}

def test_delete_email(email_api):
    """Test deleting an email."""
    email_id = "test-email-123"
    with patch.object(email_api._client, 'delete') as mock_delete:
        mock_delete.return_value = {"success": True}
        response = email_api.delete_email(email_id)
        
        mock_delete.assert_called_once_with(f"/emails/{email_id}")
        assert response == {"success": True}

def test_get_unread_count(email_api):
    """Test getting unread email count."""
    with patch.object(email_api._client, 'get') as mock_get:
        mock_get.return_value = {"count": 5}
        response = email_api.get_unread_count()
        
        mock_get.assert_called_once_with("/emails/unread/count")
        assert response == {"count": 5}

def test_mark_thread_as_read(email_api):
    """Test marking a thread as read."""
    thread_id = "test-thread-123"
    with patch.object(email_api._client, 'post') as mock_post:
        mock_post.return_value = {"success": True}
        response = email_api.mark_thread_as_read(thread_id)
        
        mock_post.assert_called_once_with(f"/emails/threads/{thread_id}/mark-as-read")
        assert response == {"success": True} 