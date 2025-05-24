"""
Tests for the account campaign mapping API endpoints
"""

import pytest
from unittest.mock import patch

from instantly.api.account_campaign_mapping import AccountCampaignMappingAPI

def test_get_account_campaign_mapping(client, account_campaign_mapping_data):
    """Test getting an account campaign mapping."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = account_campaign_mapping_data
        
        api = AccountCampaignMappingAPI(client)
        mapping = api.get_account_campaign_mapping("test@example.com")
        
        assert mapping.id == account_campaign_mapping_data["id"]
        assert str(mapping.account_id) == account_campaign_mapping_data["account_id"]
        assert str(mapping.campaign_id) == account_campaign_mapping_data["campaign_id"]
        assert mapping.is_active == account_campaign_mapping_data["is_active"]
        
        mock_get.assert_called_once_with(
            "/account-campaign-mappings/test@example.com", params=None
        ) 