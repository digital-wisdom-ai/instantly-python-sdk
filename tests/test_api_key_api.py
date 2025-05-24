"""
Tests for the API key API endpoints
"""

import pytest
from unittest.mock import patch

from instantly.api.api_key import APIKeyAPI

def test_create_api_key(client, api_key_data):
    """Test creating an API key."""
    with patch.object(client, 'post') as mock_post:
        mock_post.return_value = api_key_data
        
        api = APIKeyAPI(client)
        key = api.create_api_key(
            name=api_key_data["name"],
            scopes=api_key_data["scopes"],
            expires_at=api_key_data["expires_at"]
        )
        
        assert key.id == api_key_data["id"]
        assert key.name == api_key_data["name"]
        assert key.key == api_key_data["key"]
        assert key.scopes == api_key_data["scopes"]
        assert str(key.workspace_id) == api_key_data["workspace_id"]
        assert key.created_at.isoformat().replace('+00:00', 'Z') == api_key_data["created_at"]
        assert key.updated_at.isoformat().replace('+00:00', 'Z') == api_key_data["updated_at"]
        assert key.last_used_at.isoformat().replace('+00:00', 'Z') == api_key_data["last_used_at"]
        assert key.expires_at.isoformat().replace('+00:00', 'Z') == api_key_data["expires_at"]
        
        mock_post.assert_called_once_with(
            "/api-keys",
            json={
                "name": api_key_data["name"],
                "scopes": api_key_data["scopes"],
                "expires_at": api_key_data["expires_at"]
            }
        )

def test_list_api_keys(client, api_key_data):
    """Test listing API keys."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = {"items": [api_key_data]}
        
        api = APIKeyAPI(client)
        keys = api.list_api_keys()
        
        assert len(keys) == 1
        assert keys[0].id == api_key_data["id"]
        assert keys[0].name == api_key_data["name"]
        
        mock_get.assert_called_once_with(
            "/api-keys",
            params={"limit": 100}
        )

def test_delete_api_key(client, api_key_data):
    """Test deleting an API key."""
    with patch.object(client, 'delete') as mock_delete:
        mock_delete.return_value = None
        api = APIKeyAPI(client)
        api.delete_api_key(api_key_data["id"])
        
        mock_delete.assert_called_once_with(
            f"/api-keys/{api_key_data['id']}"
        ) 