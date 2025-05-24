"""
Test configuration and fixtures
"""

import pytest
from uuid import uuid4

from instantly import InstantlyClient, InstantlyConfig

@pytest.fixture
def config():
    """Create a test configuration."""
    return InstantlyConfig(
        api_key="test-api-key",
        base_url="https://developer.instantly.ai/_mock/api/v2",
        timeout=30,
    )

@pytest.fixture
def client(config):
    """Create a test client."""
    return InstantlyClient(config)

@pytest.fixture
def account_data():
    """Sample account data for testing."""
    return {
        "id": "acc_123",
        "name": "Test Account",
        "email": "test@example.com",
        "status": "active",
        "plan": "pro",
        "timezone": "UTC",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z",
    }

@pytest.fixture
def campaign_data():
    """Sample campaign data for testing."""
    return {
        "id": "camp_123",
        "name": "Test Campaign",
        "status": "active",
        "schedule": {
            "timezone": "UTC",
            "start_time": "09:00",
            "end_time": "17:00",
            "days": [1, 2, 3, 4, 5],
            "max_emails_per_day": 100
        },
        "email_list_id": "list_123",
        "sequence_id": "seq_123",
        "daily_limit": 100,
        "stop_on_reply": True,
        "stop_on_auto_reply": True,
        "link_tracking": True,
        "open_tracking": True,
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }

@pytest.fixture
def lead_data():
    """Sample lead data for testing."""
    return {
        "id": "lead_123",
        "email": "test@example.com",
        "first_name": "John",
        "last_name": "Doe",
        "company_name": "Test Company",
        "company_domain": "example.com",
        "phone": "+1234567890",
        "website": "https://example.com",
        "status": 1,  # Active
        "email_open_count": 0,
        "email_reply_count": 0,
        "email_click_count": 0,
        "campaign": "camp_123",
        "list_id": "list_123",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }

@pytest.fixture
def background_job_data():
    """Sample background job data for testing."""
    return {
        "id": "job_123",
        "workspace_id": str(uuid4()),
        "user_id": str(uuid4()),
        "type": "move-leads",
        "entity_id": str(uuid4()),
        "entity_type": "list",
        "data": {},
        "progress": 0,
        "status": "pending",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }

@pytest.fixture
def custom_tag_data():
    """Sample custom tag data for testing."""
    return {
        "id": "tag_123",
        "workspace_id": str(uuid4()),
        "name": "Test Tag",
        "color": "#FF0000",
        "description": "Test description",
        "resource_ids": [str(uuid4())],
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }

@pytest.fixture
def block_list_entry_data():
    """Sample block list entry data for testing."""
    return {
        "id": "block_123",
        "workspace_id": str(uuid4()),
        "type": "email",
        "value": "test@example.com",
        "reason": "Test reason",
        "expires_at": "2024-12-31T00:00:00Z",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }

@pytest.fixture
def lead_label_data():
    """Sample lead label data for testing."""
    return {
        "id": "label_123",
        "workspace_id": str(uuid4()),
        "name": "Test Label",
        "color": "#00FF00",
        "description": "Test description",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }

@pytest.fixture
def api_key_data():
    """Sample API key data for testing."""
    return {
        "id": "key_123",
        "workspace_id": str(uuid4()),
        "name": "Test API Key",
        "key": "test-api-key-value",
        "scopes": ["read", "write"],
        "expires_at": "2024-12-31T00:00:00Z",
        "last_used_at": "2024-01-02T00:00:00Z",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    }

@pytest.fixture
def account_campaign_mapping_data():
    """Sample account campaign mapping data for testing."""
    return {
        "id": "mapping_123",
        "workspace_id": str(uuid4()),
        "account_id": str(uuid4()),
        "campaign_id": str(uuid4()),
        "is_active": True,
        "last_used_at": "2024-01-02T00:00:00Z",
        "created_at": "2024-01-01T00:00:00Z",
        "updated_at": "2024-01-02T00:00:00Z"
    } 