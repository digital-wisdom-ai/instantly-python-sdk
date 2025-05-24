"""
Base API class for Instantly.ai
"""

from typing import Any, Dict, List, Optional, Union
from uuid import UUID

class BaseAPI:
    """Base class for all API endpoints."""
    
    def __init__(self, client):
        """
        Initialize the API with a client.
        
        Args:
            client: The InstantlyClient instance
        """
        self._client = client
    
    def _get(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a GET request.
        
        Args:
            path: The API path
            params: Optional query parameters
            
        Returns:
            The response data
        """
        return self._client.get(path, params=params)
    
    def _post(self, path: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a POST request.
        
        Args:
            path: The API path
            json: Optional JSON data
            
        Returns:
            The response data
        """
        return self._client.post(path, json=json)
    
    def _patch(self, path: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a PATCH request.
        
        Args:
            path: The API path
            json: Optional JSON data
            
        Returns:
            The response data
        """
        return self._client.patch(path, json=json)
    
    def _delete(self, path: str) -> None:
        """
        Make a DELETE request.
        
        Args:
            path: The API path
        """
        self._client.delete(path) 