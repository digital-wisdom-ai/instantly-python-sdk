"""
Lead label API endpoints for Instantly.ai
"""

from typing import Optional, List
from uuid import UUID

from ..models.lead_label import LeadLabel
from .base import BaseAPI

class LeadLabelAPI(BaseAPI):
    """API endpoints for lead labels."""
    
    def create_lead_label(
        self,
        name: str,
        color: str,
        description: Optional[str] = None
    ) -> LeadLabel:
        """
        Create a new lead label.
        
        Args:
            name: The name of the label
            color: The color of the label in hex format
            description: Optional description of the label
            
        Returns:
            The created lead label
        """
        data = {
            "name": name,
            "color": color,
            "description": description
        }
        data = {k: v for k, v in data.items() if v is not None}
        
        response = self._post("/lead-labels", json=data)
        return LeadLabel(**response)
    
    def list_lead_labels(
        self,
        workspace_id: Optional[UUID] = None,
        limit: int = 100,
        starting_after: Optional[str] = None
    ) -> List[LeadLabel]:
        """
        List lead labels.
        
        Args:
            workspace_id: Optional workspace ID to filter by
            limit: Maximum number of labels to return
            starting_after: Cursor for pagination
            
        Returns:
            List of lead labels
        """
        params = {
            "limit": limit,
            "starting_after": starting_after,
            "workspace_id": str(workspace_id) if workspace_id else None
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self._get("/lead-labels", params=params)
        return [LeadLabel(**label) for label in response["items"]]
    
    def get_lead_label(self, label_id: str) -> LeadLabel:
        """
        Get a specific lead label.
        
        Args:
            label_id: The ID of the lead label
            
        Returns:
            The lead label
        """
        response = self._get(f"/lead-labels/{label_id}")
        return LeadLabel(**response)
    
    def update_lead_label(
        self,
        label_id: str,
        name: Optional[str] = None,
        color: Optional[str] = None,
        description: Optional[str] = None
    ) -> LeadLabel:
        """
        Update a lead label.
        
        Args:
            label_id: The ID of the lead label
            name: Optional new name for the label
            color: Optional new color for the label
            description: Optional new description for the label
            
        Returns:
            The updated lead label
        """
        data = {
            "name": name,
            "color": color,
            "description": description
        }
        data = {k: v for k, v in data.items() if v is not None}
        
        response = self._patch(f"/lead-labels/{label_id}", json=data)
        return LeadLabel(**response)
    
    def delete_lead_label(self, label_id: str) -> None:
        """
        Delete a lead label.
        
        Args:
            label_id: The ID of the lead label to delete
        """
        self._delete(f"/lead-labels/{label_id}") 