"""
API key API endpoints for Instantly.ai
"""

from typing import Optional, List
from uuid import UUID

from ..models.api_key import APIKey
from .base import BaseAPI

class APIKeyAPI(BaseAPI):
    """API endpoints for API keys."""
    
    def create_api_key(
        self,
        name: str,
        scopes: List[str],
        expires_at: Optional[str] = None
    ) -> APIKey:
        """
        Create a new API key.
        
        Args:
            name: The name of the API key
            scopes: List of scopes this API key has access to
            expires_at: Optional expiration date for the API key
            
        Returns:
            The created API key
        """
        data = {
            "name": name,
            "scopes": scopes,
            "expires_at": expires_at
        }
        data = {k: v for k, v in data.items() if v is not None}
        
        response = self._post("/api-keys", json=data)
        return APIKey(**response)
    
    def list_api_keys(
        self,
        workspace_id: Optional[UUID] = None,
        limit: int = 100,
        starting_after: Optional[str] = None
    ) -> List[APIKey]:
        """
        List API keys.
        
        Args:
            workspace_id: Optional workspace ID to filter by
            limit: Maximum number of keys to return
            starting_after: Cursor for pagination
            
        Returns:
            List of API keys
        """
        params = {
            "limit": limit,
            "starting_after": starting_after,
            "workspace_id": str(workspace_id) if workspace_id else None
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self._get("/api-keys", params=params)
        return [APIKey(**key) for key in response["items"]]
    
    def delete_api_key(self, key_id: str) -> None:
        """
        Delete an API key.
        
        Args:
            key_id: The ID of the API key to delete
        """
        self._delete(f"/api-keys/{key_id}") 