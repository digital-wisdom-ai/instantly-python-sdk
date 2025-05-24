from typing import Optional, List, Dict, Any, Union, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from ..client import InstantlyClient


class LeadAPI:
    """Lead API endpoints for Instantly.ai"""

    def __init__(self, client: "InstantlyClient"):
        self.client = client

    def create_lead(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new lead.

        Args:
            data: Lead data including required fields like email, first_name, last_name, etc.

        Returns:
            Dict containing the created lead data
        """
        return self.client.post("/api/v2/leads", json=data)

    def list_leads(self, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        List leads with optional filtering.

        Args:
            params: Optional query parameters for filtering and pagination

        Returns:
            Dict containing the list of leads and pagination info
        """
        return self.client.get("/api/v2/leads", params=params)

    def get_lead(self, lead_id: str) -> Dict[str, Any]:
        """
        Get a specific lead by ID.

        Args:
            lead_id: The unique identifier of the lead

        Returns:
            Dict containing the lead data
        """
        return self.client.get(f"/api/v2/leads/{lead_id}")

    def update_lead(self, lead_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update a lead's information.

        Args:
            lead_id: The unique identifier of the lead
            data: The updated lead data

        Returns:
            Dict containing the updated lead data
        """
        return self.client.patch(f"/api/v2/leads/{lead_id}", json=data)

    def delete_lead(self, lead_id: str) -> None:
        """
        Delete a lead.

        Args:
            lead_id: The unique identifier of the lead to delete
        """
        self.client.delete(f"/api/v2/leads/{lead_id}")

    def merge_leads(self, primary_lead_id: str, secondary_lead_id: str) -> Dict[str, Any]:
        """
        Merge two leads, keeping the primary lead's data.

        Args:
            primary_lead_id: The ID of the lead to keep
            secondary_lead_id: The ID of the lead to merge into the primary

        Returns:
            Dict containing the merged lead data
        """
        data = {
            "primary_lead_id": primary_lead_id,
            "secondary_lead_id": secondary_lead_id
        }
        return self.client.post("/api/v2/leads/merge", json=data)

    def update_interest_status(self, lead_id: str, status: int) -> Dict[str, Any]:
        """
        Update the interest status of a lead.

        Args:
            lead_id: The unique identifier of the lead
            status: The new interest status (1: Interested, 2: Not Interested, 3: Maybe Later)

        Returns:
            Dict containing the updated lead data
        """
        data = {
            "lead_id": lead_id,
            "status": status
        }
        return self.client.post("/api/v2/leads/update-interest-status", json=data)

    def remove_from_subsequence(self, lead_id: str) -> Dict[str, Any]:
        """
        Remove a lead from a subsequence.

        Args:
            lead_id: The unique identifier of the lead

        Returns:
            Dict containing the updated lead data
        """
        data = {"lead_id": lead_id}
        return self.client.post("/api/v2/leads/subsequence/remove", json=data)

    def bulk_assign_leads(self, lead_ids: List[str], user_id: str) -> Dict[str, Any]:
        """
        Bulk assign leads to organization users.

        Args:
            lead_ids: List of lead IDs to assign
            user_id: The ID of the user to assign the leads to

        Returns:
            Dict containing the assignment results
        """
        data = {
            "lead_ids": lead_ids,
            "user_id": user_id
        }
        return self.client.post("/api/v2/leads/bulk-assign", json=data)

    def move_leads(self, lead_ids: List[str], target_id: str, target_type: str) -> Dict[str, Any]:
        """
        Move leads to a campaign or list.

        Args:
            lead_ids: List of lead IDs to move
            target_id: The ID of the target campaign or list
            target_type: The type of target ('campaign' or 'list')

        Returns:
            Dict containing the move results
        """
        data = {
            "lead_ids": lead_ids,
            "target_id": target_id,
            "target_type": target_type
        }
        return self.client.post("/api/v2/leads/move", json=data)

    def export_leads(self, lead_ids: List[str], app_id: str) -> Dict[str, Any]:
        """
        Export leads to an external app.

        Args:
            lead_ids: List of lead IDs to export
            app_id: The ID of the external app to export to

        Returns:
            Dict containing the export results
        """
        data = {
            "lead_ids": lead_ids,
            "app_id": app_id
        }
        return self.client.post("/api/v2/leads/export", json=data)

    def move_to_subsequence(self, lead_id: str, subsequence_id: str) -> Dict[str, Any]:
        """
        Move a lead to a subsequence.

        Args:
            lead_id: The unique identifier of the lead
            subsequence_id: The ID of the subsequence to move the lead to

        Returns:
            Dict containing the updated lead data
        """
        data = {
            "lead_id": lead_id,
            "subsequence_id": subsequence_id
        }
        return self.client.post("/api/v2/leads/subsequence/move", json=data) 