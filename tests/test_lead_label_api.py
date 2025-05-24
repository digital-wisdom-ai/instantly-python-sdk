"""
Tests for the lead label API endpoints
"""

import pytest
from unittest.mock import patch

from instantly.api.lead_label import LeadLabelAPI

def test_create_lead_label(client, lead_label_data):
    """Test creating a lead label."""
    with patch.object(client, 'post') as mock_post:
        mock_post.return_value = lead_label_data
        
        api = LeadLabelAPI(client)
        label = api.create_lead_label(name=lead_label_data["name"], color=lead_label_data["color"])
        
        assert label.id == lead_label_data["id"]
        assert label.name == lead_label_data["name"]
        assert label.color == lead_label_data["color"]
        assert label.description == lead_label_data["description"]
        
        mock_post.assert_called_once_with(
            "/lead-labels", json={"name": lead_label_data["name"], "color": lead_label_data["color"]}
        )

def test_list_lead_labels(client, lead_label_data):
    """Test listing lead labels."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = {"items": [lead_label_data]}
        
        api = LeadLabelAPI(client)
        labels = api.list_lead_labels()
        
        assert len(labels) == 1
        assert labels[0].id == lead_label_data["id"]
        assert labels[0].name == lead_label_data["name"]
        
        mock_get.assert_called_once_with(
            "/lead-labels", params={"limit": 100}
        )

def test_get_lead_label(client, lead_label_data):
    """Test getting a specific lead label."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = lead_label_data
        
        api = LeadLabelAPI(client)
        label = api.get_lead_label(lead_label_data["id"])
        
        assert label.id == lead_label_data["id"]
        assert label.name == lead_label_data["name"]
        assert label.color == lead_label_data["color"]
        
        mock_get.assert_called_once_with(
            f"/lead-labels/{lead_label_data['id']}",
            params=None
        )

def test_update_lead_label(client, lead_label_data):
    """Test updating a lead label."""
    with patch.object(client, 'patch') as mock_patch:
        mock_patch.return_value = lead_label_data
        
        api = LeadLabelAPI(client)
        label = api.update_lead_label(
            lead_label_data["id"],
            name="Updated Name",
            color="#0000FF",
            description="Updated description"
        )
        
        assert label.id == lead_label_data["id"]
        
        mock_patch.assert_called_once_with(
            f"/lead-labels/{lead_label_data['id']}",
            json={
                "name": "Updated Name",
                "color": "#0000FF",
                "description": "Updated description"
            }
        )

def test_delete_lead_label(client, lead_label_data):
    """Test deleting a lead label."""
    with patch.object(client, 'delete') as mock_delete:
        mock_delete.return_value = None
        api = LeadLabelAPI(client)
        api.delete_lead_label(lead_label_data["id"])
        
        mock_delete.assert_called_once_with(
            f"/lead-labels/{lead_label_data['id']}"
        ) 