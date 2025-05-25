"""
Campaign API client for the Instantly.ai API
"""

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from instantly.client import InstantlyClient
from instantly.models.campaign import Campaign, CampaignCreate, CampaignUpdate

class CampaignAPI:
    """Client for the Campaign API endpoints."""
    
    def __init__(self, client: 'InstantlyClient'):
        """
        Initialize the Campaign API client.
        
        Args:
            client: The main Instantly.ai client
        """
        self._client = client
        
    def get_campaign(self, campaign_id: str) -> Campaign:
        """
        Get a campaign by ID.
        
        Args:
            campaign_id: The ID of the campaign to retrieve
            
        Returns:
            The campaign details
        """
        response = self._client.get(f"/campaigns/{campaign_id}")
        return Campaign.model_validate(response)
        
    def list_campaigns(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[Campaign]:
        """
        List all campaigns.
        
        Args:
            limit: Maximum number of campaigns to return
            offset: Number of campaigns to skip
            
        Returns:
            List of campaigns
        """
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
            
        response = self._client.get("/campaigns", params=params)
        return [Campaign.model_validate(campaign) for campaign in response["items"]]
        
    def create_campaign(self, campaign: CampaignCreate) -> Campaign:
        """
        Create a new campaign.
        
        Args:
            campaign: The campaign details to create
            
        Returns:
            The created campaign
        """
        response = self._client.post("/campaigns", json=campaign.model_dump(exclude_none=True, by_alias=True))
        return Campaign.model_validate(response)
        
    def update_campaign(self, campaign_id: str, campaign: CampaignUpdate) -> Campaign:
        """
        Update an existing campaign.
        
        Args:
            campaign_id: The ID of the campaign to update
            campaign: The updated campaign details
            
        Returns:
            The updated campaign
        """
        response = self._client.put(
            f"/campaigns/{campaign_id}",
            json=campaign.model_dump(exclude_none=True, by_alias=True, exclude_unset=True),
        )
        return Campaign.model_validate(response)
        
    def delete_campaign(self, campaign_id: str) -> None:
        """
        Delete a campaign.
        
        Args:
            campaign_id: The ID of the campaign to delete
        """
        self._client.delete(f"/campaigns/{campaign_id}")
        
    def activate_campaign(self, campaign_id: str) -> Campaign:
        """
        Activate a campaign.
        
        Args:
            campaign_id: The ID of the campaign to activate
            
        Returns:
            The activated campaign
        """
        response = self._client.post(f"/campaigns/{campaign_id}/activate")
        return Campaign.model_validate(response)
        
    def pause_campaign(self, campaign_id: str) -> Campaign:
        """
        Pause a campaign.
        
        Args:
            campaign_id: The ID of the campaign to pause
            
        Returns:
            The paused campaign
        """
        response = self._client.post(f"/campaigns/{campaign_id}/pause")
        return Campaign.model_validate(response)
        
    def get_campaign_analytics(self, campaign_id: str) -> dict:
        """
        Get analytics for a campaign.
        
        Args:
            campaign_id: The ID of the campaign to get analytics for
            
        Returns:
            Campaign analytics data
        """
        return self._client.get(f"/campaigns/{campaign_id}/analytics")
        
    def get_campaign_analytics_overview(self) -> dict:
        """
        Get analytics overview for all campaigns.
        
        Returns:
            Campaign analytics overview data
        """
        return self._client.get("/campaigns/analytics/overview")
        
    def get_daily_campaign_analytics(self, campaign_id: str) -> dict:
        """
        Get daily analytics for a campaign.
        
        Args:
            campaign_id: The ID of the campaign to get daily analytics for
            
        Returns:
            Daily campaign analytics data
        """
        return self._client.get(f"/campaigns/{campaign_id}/analytics/daily")
        
    def get_campaign_steps_analytics(self, campaign_id: str) -> dict:
        """
        Get step-by-step analytics for a campaign.
        
        Args:
            campaign_id: The ID of the campaign to get step analytics for
            
        Returns:
            Campaign step analytics data
        """
        return self._client.get(f"/campaigns/{campaign_id}/analytics/steps") 