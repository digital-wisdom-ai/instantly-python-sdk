"""
Custom tag API endpoints for Instantly.ai
"""

from typing import Optional, List, Dict, Any
from uuid import UUID

from ..models.custom_tag import CustomTag
from .base import BaseAPI

class CustomTagAPI(BaseAPI):
    """API endpoints for custom tags."""
    
    def create_custom_tag(
        self,
        name: str,
        color: str,
        description: Optional[str] = None,
        resource_ids: Optional[List[UUID]] = None
    ) -> CustomTag:
        """
        Create a new custom tag.
        
        Args:
            name: The name of the tag
            color: The color of the tag in hex format
            description: Optional description of the tag
            resource_ids: Optional list of resource IDs to apply the tag to
            
        Returns:
            The created custom tag
        """
        data = {
            "name": name,
            "color": color,
            "description": description,
            "resource_ids": [str(rid) for rid in (resource_ids or [])]
        }
        data = {k: v for k, v in data.items() if v is not None}
        
        response = self._post("/custom-tags", json=data)
        return CustomTag(**response)
    
    def list_custom_tags(
        self,
        workspace_id: Optional[UUID] = None,
        limit: int = 100,
        starting_after: Optional[str] = None
    ) -> List[CustomTag]:
        """
        List custom tags.
        
        Args:
            workspace_id: Optional workspace ID to filter by
            limit: Maximum number of tags to return
            starting_after: Cursor for pagination
            
        Returns:
            List of custom tags
        """
        params = {
            "limit": limit,
            "starting_after": starting_after,
            "workspace_id": str(workspace_id) if workspace_id else None
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self._get("/custom-tags", params=params)
        return [CustomTag(**tag) for tag in response["items"]]
    
    def get_custom_tag(self, tag_id: str) -> CustomTag:
        """
        Get a specific custom tag.
        
        Args:
            tag_id: The ID of the custom tag
            
        Returns:
            The custom tag
        """
        response = self._get(f"/custom-tags/{tag_id}")
        return CustomTag(**response)
    
    def update_custom_tag(
        self,
        tag_id: str,
        name: Optional[str] = None,
        color: Optional[str] = None,
        description: Optional[str] = None,
        resource_ids: Optional[List[UUID]] = None
    ) -> CustomTag:
        """
        Update a custom tag.
        
        Args:
            tag_id: The ID of the custom tag
            name: Optional new name for the tag
            color: Optional new color for the tag
            description: Optional new description for the tag
            resource_ids: Optional new list of resource IDs
            
        Returns:
            The updated custom tag
        """
        data = {
            "name": name,
            "color": color,
            "description": description,
            "resource_ids": [str(rid) for rid in (resource_ids or [])]
        }
        data = {k: v for k, v in data.items() if v is not None}
        
        response = self._patch(f"/custom-tags/{tag_id}", json=data)
        return CustomTag(**response)
    
    def delete_custom_tag(self, tag_id: str) -> None:
        """
        Delete a custom tag.
        
        Args:
            tag_id: The ID of the custom tag to delete
        """
        self._delete(f"/custom-tags/{tag_id}")
    
    def toggle_resource(
        self,
        tag_id: str,
        resource_id: UUID,
        add: bool = True
    ) -> CustomTag:
        """
        Add or remove a resource from a custom tag.
        
        Args:
            tag_id: The ID of the custom tag
            resource_id: The ID of the resource to add/remove
            add: Whether to add (True) or remove (False) the resource
            
        Returns:
            The updated custom tag
        """
        data = {
            "resource_id": str(resource_id),
            "add": add
        }
        
        response = self._post(f"/custom-tags/{tag_id}/toggle-resource", json=data)
        return CustomTag(**response) 