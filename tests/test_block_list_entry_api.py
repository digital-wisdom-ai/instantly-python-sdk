"""
Tests for the block list entry API endpoints
"""

import pytest
from unittest.mock import patch

from instantly.api.block_list_entry import BlockListEntryAPI

def test_create_block_list_entry(client, block_list_entry_data):
    """Test creating a block list entry."""
    with patch.object(client, 'post') as mock_post:
        mock_post.return_value = block_list_entry_data
        
        api = BlockListEntryAPI(client)
        entry = api.create_block_list_entry(type=block_list_entry_data["type"], value=block_list_entry_data["value"], reason=block_list_entry_data["reason"])
        
        assert entry.id == block_list_entry_data["id"]
        
        mock_post.assert_called_once_with(
            "/block-lists-entries", json={"type": block_list_entry_data["type"], "value": block_list_entry_data["value"], "reason": block_list_entry_data["reason"]}
        )

def test_list_block_list_entries(client, block_list_entry_data):
    """Test listing block list entries."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = {"items": [block_list_entry_data]}
        
        api = BlockListEntryAPI(client)
        entries = api.list_block_list_entries()
        
        assert len(entries) == 1
        assert entries[0].id == block_list_entry_data["id"]
        
        mock_get.assert_called_once_with(
            "/block-lists-entries", params={"limit": 100}
        )

def test_get_block_list_entry(client, block_list_entry_data):
    """Test getting a specific block list entry."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = block_list_entry_data
        
        api = BlockListEntryAPI(client)
        entry = api.get_block_list_entry(block_list_entry_data["id"])
        
        assert entry.id == block_list_entry_data["id"]
        
        mock_get.assert_called_once_with(
            f"/block-lists-entries/{block_list_entry_data['id']}", params=None
        )

def test_update_block_list_entry(client, block_list_entry_data):
    """Test updating a block list entry."""
    with patch.object(client, 'patch') as mock_patch:
        mock_patch.return_value = block_list_entry_data
        
        api = BlockListEntryAPI(client)
        entry = api.update_block_list_entry(block_list_entry_data["id"], reason="Updated Reason")
        
        assert entry.id == block_list_entry_data["id"]
        
        mock_patch.assert_called_once_with(
            f"/block-lists-entries/{block_list_entry_data['id']}", json={"reason": "Updated Reason"}
        )

def test_delete_block_list_entry(client, block_list_entry_data):
    """Test deleting a block list entry."""
    with patch.object(client, 'delete') as mock_delete:
        mock_delete.return_value = None
        api = BlockListEntryAPI(client)
        api.delete_block_list_entry(block_list_entry_data["id"])
        
        mock_delete.assert_called_once_with(
            f"/block-lists-entries/{block_list_entry_data['id']}"
        ) 