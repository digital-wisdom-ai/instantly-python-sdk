"""
Tests for the Lead List API endpoints
"""

import pytest
from unittest.mock import Mock, patch

from instantly import InstantlyClient, InstantlyConfig
from instantly.api.lead_list import LeadListAPI

@pytest.fixture
def lead_list_api(config):
    """Create a LeadListAPI instance for testing."""
    client = InstantlyClient(config)
    return LeadListAPI(client)

def test_create_list(lead_list_api):
    """Test creating a new lead list."""
    name = "Test List"
    description = "A test list"
    expected_data = {
        "name": name,
        "description": description
    }
    
    with patch.object(lead_list_api._client, 'post') as mock_post:
        mock_post.return_value = {
            "id": "test-list-123",
            "name": name,
            "description": description
        }
        response = lead_list_api.create_list(name, description)
        
        mock_post.assert_called_once_with("/lead-lists", json=expected_data)
        assert response == {
            "id": "test-list-123",
            "name": name,
            "description": description
        }

def test_list_lists(lead_list_api):
    """Test listing lead lists."""
    with patch.object(lead_list_api._client, 'get') as mock_get:
        mock_get.return_value = {
            "lists": [],
            "total": 0,
            "page": 1,
            "per_page": 50
        }
        response = lead_list_api.list_lists(page=2, per_page=25)
        
        mock_get.assert_called_once_with("/lead-lists", params={"page": 2, "per_page": 25})
        assert response == {
            "lists": [],
            "total": 0,
            "page": 1,
            "per_page": 50
        }

def test_get_list(lead_list_api):
    """Test getting a specific lead list."""
    list_id = "test-list-123"
    with patch.object(lead_list_api._client, 'get') as mock_get:
        mock_get.return_value = {
            "id": list_id,
            "name": "Test List",
            "description": "A test list"
        }
        response = lead_list_api.get_list(list_id)
        
        mock_get.assert_called_once_with(f"/lead-lists/{list_id}")
        assert response == {
            "id": list_id,
            "name": "Test List",
            "description": "A test list"
        }

def test_update_list(lead_list_api):
    """Test updating a lead list."""
    list_id = "test-list-123"
    new_name = "Updated List"
    new_description = "Updated description"
    expected_data = {
        "name": new_name,
        "description": new_description
    }
    
    with patch.object(lead_list_api._client, 'patch') as mock_patch:
        mock_patch.return_value = {
            "id": list_id,
            "name": new_name,
            "description": new_description
        }
        response = lead_list_api.update_list(list_id, name=new_name, description=new_description)
        
        mock_patch.assert_called_once_with(f"/lead-lists/{list_id}", json=expected_data)
        assert response == {
            "id": list_id,
            "name": new_name,
            "description": new_description
        }

def test_delete_list(lead_list_api):
    """Test deleting a lead list."""
    list_id = "test-list-123"
    with patch.object(lead_list_api._client, 'delete') as mock_delete:
        mock_delete.return_value = {"success": True}
        response = lead_list_api.delete_list(list_id)
        
        mock_delete.assert_called_once_with(f"/lead-lists/{list_id}")
        assert response == {"success": True} 