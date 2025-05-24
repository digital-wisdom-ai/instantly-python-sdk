"""
Account campaign mapping API endpoints for Instantly.ai
"""

from typing import Optional
from uuid import UUID

from ..models.account_campaign_mapping import AccountCampaignMapping
from .base import BaseAPI

class AccountCampaignMappingAPI(BaseAPI):
    """API endpoints for account campaign mappings."""
    
    def get_account_campaign_mapping(self, email: str) -> AccountCampaignMapping:
        """
        Get the campaign mapping for an account.
        
        Args:
            email: The email address of the account
            
        Returns:
            The account campaign mapping
        """
        response = self._get(f"/account-campaign-mappings/{email}")
        return AccountCampaignMapping(**response) 