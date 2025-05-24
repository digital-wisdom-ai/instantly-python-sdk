"""
Main client for interacting with the Instantly.ai API
"""

from typing import Any, Dict, Optional

import httpx

from instantly.config import InstantlyConfig

class InstantlyClient:
    """Main client for interacting with the Instantly.ai API."""
    
    def __init__(self, config: InstantlyConfig):
        """
        Initialize the Instantly.ai client.
        
        Args:
            config: The configuration for the client
        """
        self.config = config
        self._client = httpx.Client(
            base_url=config.base_url,
            headers=config.headers,
            timeout=config.timeout,
        )
        
        # Initialize API clients
        self._init_api_clients()
        
    def _init_api_clients(self):
        """Initialize API clients to avoid circular imports."""
        from instantly.api.account import AccountAPI
        from instantly.api.campaign import CampaignAPI
        from instantly.api.lead import LeadAPI
        from instantly.api.email import EmailAPI
        from instantly.api.email_verification import EmailVerificationAPI
        from instantly.api.lead_list import LeadListAPI
        
        self.accounts = AccountAPI(self)
        self.campaigns = CampaignAPI(self)
        self.leads = LeadAPI(self)
        self.emails = EmailAPI(self)
        self.email_verification = EmailVerificationAPI(self)
        self.lead_lists = LeadListAPI(self)
        
    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Make a request to the Instantly.ai API.
        
        Args:
            method: The HTTP method to use
            endpoint: The API endpoint to call
            params: Query parameters
            json: JSON body for POST/PUT requests
            
        Returns:
            The JSON response from the API
            
        Raises:
            httpx.HTTPError: If the request fails
        """
        response = self._client.request(
            method=method,
            url=endpoint,
            params=params,
            json=json,
        )
        response.raise_for_status()
        return response.json()
        
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request to the API."""
        return self._request("GET", endpoint, params=params)
        
    def post(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        """Make a POST request to the API."""
        return self._request("POST", endpoint, json=json)
        
    def put(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        """Make a PUT request to the API."""
        return self._request("PUT", endpoint, json=json)
        
    def patch(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        """Make a PATCH request to the API."""
        return self._request("PATCH", endpoint, json=json)
        
    def delete(self, endpoint: str) -> Dict[str, Any]:
        """Make a DELETE request to the API."""
        return self._request("DELETE", endpoint)
        
    def close(self) -> None:
        """Close the HTTP client."""
        self._client.close()
        
    def __enter__(self) -> "InstantlyClient":
        """Context manager entry."""
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Context manager exit."""
        self.close() 