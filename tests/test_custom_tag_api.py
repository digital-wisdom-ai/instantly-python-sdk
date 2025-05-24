"""
Tests for the custom tag API endpoints
"""

import pytest
from unittest.mock import patch

from instantly.api.custom_tag import CustomTagAPI

def test_create_custom_tag(client, custom_tag_data):
    """Test creating a custom tag."""
    with patch.object(client, 'post') as mock_post:
        mock_post.return_value = custom_tag_data
        
        api = CustomTagAPI(client)
        tag = api.create_custom_tag(name=custom_tag_data["name"], color=custom_tag_data["color"])
        
        assert tag.id == custom_tag_data["id"]
        
        called_args, called_kwargs = mock_post.call_args
        assert called_args[0] == "/custom-tags"
        for k, v in {"name": custom_tag_data["name"], "color": custom_tag_data["color"]}.items():
            assert called_kwargs["json"][k] == v

def test_list_custom_tags(client, custom_tag_data):
    """Test listing custom tags."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = {"items": [custom_tag_data]}
        
        api = CustomTagAPI(client)
        tags = api.list_custom_tags()
        
        assert len(tags) == 1
        assert tags[0].id == custom_tag_data["id"]
        
        mock_get.assert_called_once_with(
            "/custom-tags", params={"limit": 100}
        )

def test_get_custom_tag(client, custom_tag_data):
    """Test getting a specific custom tag."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = custom_tag_data
        
        api = CustomTagAPI(client)
        tag = api.get_custom_tag(custom_tag_data["id"])
        
        assert tag.id == custom_tag_data["id"]
        assert tag.name == custom_tag_data["name"]
        assert tag.color == custom_tag_data["color"]
        
        mock_get.assert_called_once_with(
            f"/custom-tags/{custom_tag_data['id']}",
            params=None
        )

def test_update_custom_tag(client, custom_tag_data):
    """Test updating a custom tag."""
    with patch.object(client, 'patch') as mock_patch:
        mock_patch.return_value = custom_tag_data
        
        api = CustomTagAPI(client)
        tag = api.update_custom_tag(custom_tag_data["id"], name="Updated Name")
        
        assert tag.id == custom_tag_data["id"]
        
        called_args, called_kwargs = mock_patch.call_args
        assert called_args[0] == f"/custom-tags/{custom_tag_data['id']}"
        assert "name" in called_kwargs["json"]
        assert called_kwargs["json"]["name"] == "Updated Name"

def test_delete_custom_tag(client, custom_tag_data):
    """Test deleting a custom tag."""
    with patch.object(client, 'delete') as mock_delete:
        mock_delete.return_value = None
        api = CustomTagAPI(client)
        api.delete_custom_tag(custom_tag_data["id"])
        
        mock_delete.assert_called_once_with(
            f"/custom-tags/{custom_tag_data['id']}"
        )

def test_toggle_resource(client, custom_tag_data):
    """Test toggling a resource on a custom tag."""
    with patch.object(client, 'post') as mock_post:
        mock_post.return_value = custom_tag_data
        
        api = CustomTagAPI(client)
        tag = api.toggle_resource(custom_tag_data["id"], resource_id="abc123")
        
        assert tag.id == custom_tag_data["id"]
        
        called_args, called_kwargs = mock_post.call_args
        assert called_args[0] == f"/custom-tags/{custom_tag_data['id']}/toggle-resource"
        assert called_kwargs["json"]["resource_id"] == "abc123" 