"""
Lead List API endpoints for Instantly.ai
"""

from typing import Dict, Any, List, Optional

from ..client import InstantlyClient

class LeadListAPI:
    """Lead List API endpoints."""

    def __init__(self, client: InstantlyClient):
        self._client = client

    def create_list(self, name: str, description: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new lead list.

        Args:
            name: Name of the list
            description: Optional description of the list

        Returns:
            Dict containing the created list details
        """
        data = {"name": name}
        if description:
            data["description"] = description
        return self._client.post("/lead-lists", json=data)

    def list_lists(self, page: int = 1, per_page: int = 50) -> Dict[str, Any]:
        """
        List all lead lists.

        Args:
            page: Page number for pagination
            per_page: Number of items per page

        Returns:
            Dict containing list of lead lists and pagination info
        """
        params = {"page": page, "per_page": per_page}
        return self._client.get("/lead-lists", params=params)

    def get_list(self, list_id: str) -> Dict[str, Any]:
        """
        Get a specific lead list by ID.

        Args:
            list_id: The ID of the list to retrieve

        Returns:
            Dict containing list details
        """
        return self._client.get(f"/lead-lists/{list_id}")

    def update_list(self, list_id: str, name: Optional[str] = None, 
                   description: Optional[str] = None) -> Dict[str, Any]:
        """
        Update a lead list's properties.

        Args:
            list_id: The ID of the list to update
            name: Optional new name for the list
            description: Optional new description for the list

        Returns:
            Dict containing updated list details
        """
        data = {}
        if name is not None:
            data["name"] = name
        if description is not None:
            data["description"] = description
        return self._client.patch(f"/lead-lists/{list_id}", json=data)

    def delete_list(self, list_id: str) -> Dict[str, Any]:
        """
        Delete a lead list.

        Args:
            list_id: The ID of the list to delete

        Returns:
            Dict containing success status
        """
        return self._client.delete(f"/lead-lists/{list_id}") 