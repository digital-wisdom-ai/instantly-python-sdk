from typing import Optional, List, Dict, Any, Union, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from ..client import InstantlyClient
from ..models.lead import (
    Lead, LeadStatusSummary, LeadStatusSummarySubseq,
    LeadCreateRequest, LeadUpdateRequest, LeadMergeRequest,
    LeadInterestStatusRequest, LeadSubsequenceRemoveRequest,
    LeadBulkAssignRequest, LeadMoveRequest, LeadExportRequest,
    LeadSubsequenceMoveRequest, ListLeadsRequest,
    BulkAssignLeadsResult, MoveLeadsResult, ExportLeadsResult
)


class LeadAPI:
    """Lead API endpoints for Instantly.ai"""

    def __init__(self, client: "InstantlyClient"):
        self.client = client

    def create_lead(self, data: LeadCreateRequest) -> Lead:
        """
        Create a new lead.

        Args:
            data: Lead creation data including required fields like email

        Returns:
            Lead object containing the created lead data
        """
        response = self.client.post("/api/v2/leads", json=data.model_dump(exclude_none=True))
        return Lead.parse_obj(response)

    def list_leads(self, params: Optional[ListLeadsRequest] = None) -> List[Lead]:
        """
        List leads with optional filtering.

        Args:
            params: Optional filtering parameters for the leads list

        Returns:
            List of Lead objects
        """
        if params is None:
            params = ListLeadsRequest()
        response = self.client.post("/leads/list", json=params.model_dump(exclude_none=True))
        return [Lead.parse_obj(item) for item in response.get("items", [])]

    def get_lead(self, lead_id: str) -> Lead:
        """
        Get a specific lead by ID.

        Args:
            lead_id: The unique identifier of the lead

        Returns:
            Lead object containing the lead data
        """
        response = self.client.get(f"/api/v2/leads/{lead_id}")
        return Lead.parse_obj(response)

    def update_lead(self, lead_id: str, data: LeadUpdateRequest) -> Lead:
        """
        Update a lead's information.

        Args:
            lead_id: The unique identifier of the lead
            data: The updated lead data

        Returns:
            Lead object containing the updated lead data
        """
        response = self.client.patch(f"/api/v2/leads/{lead_id}", json=data.model_dump(exclude_none=True))
        return Lead.parse_obj(response)

    def delete_lead(self, lead_id: str) -> None:
        """
        Delete a lead.

        Args:
            lead_id: The unique identifier of the lead to delete
        """
        self.client.delete(f"/api/v2/leads/{lead_id}")

    def merge_leads(self, data: LeadMergeRequest) -> Lead:
        """
        Merge two leads, keeping the primary lead's data.

        Args:
            data: The merge request data containing primary and secondary lead IDs

        Returns:
            Lead object containing the merged lead data
        """
        response = self.client.post("/api/v2/leads/merge", json=data.model_dump())
        return Lead.parse_obj(response)

    def update_interest_status(self, data: LeadInterestStatusRequest) -> Lead:
        """
        Update the interest status of a lead.

        Args:
            data: The interest status update request data

        Returns:
            Lead object containing the updated lead data
        """
        response = self.client.post("/api/v2/leads/update-interest-status", json=data.model_dump())
        return Lead.parse_obj(response)

    def remove_from_subsequence(self, data: LeadSubsequenceRemoveRequest) -> Lead:
        """
        Remove a lead from a subsequence.

        Args:
            data: The subsequence removal request data

        Returns:
            Lead object containing the updated lead data
        """
        response = self.client.post("/api/v2/leads/subsequence/remove", json=data.model_dump())
        return Lead.parse_obj(response)

    def bulk_assign_leads(self, data: LeadBulkAssignRequest) -> BulkAssignLeadsResult:
        """
        Bulk assign leads to organization users.

        Args:
            data: The bulk assignment request data

        Returns:
            Dict containing the assignment results
        """
        response = self.client.post("/api/v2/leads/bulk-assign", json=data.model_dump())
        return BulkAssignLeadsResult.model_validate(response)

    def move_leads(self, data: LeadMoveRequest) -> MoveLeadsResult:
        """
        Move leads to a campaign or list.

        Args:
            data: The move request data

        Returns:
            Dict containing the move results
        """
        response = self.client.post("/api/v2/leads/move", json=data.model_dump())
        return MoveLeadsResult.model_validate(response)

    def export_leads(self, data: LeadExportRequest) -> ExportLeadsResult:
        """
        Export leads to an external app.

        Args:
            data: The export request data

        Returns:
            Dict containing the export results
        """
        response = self.client.post("/api/v2/leads/export", json=data.model_dump())
        return ExportLeadsResult.model_validate(response)

    def move_to_subsequence(self, data: LeadSubsequenceMoveRequest) -> Lead:
        """
        Move a lead to a subsequence.

        Args:
            data: The subsequence move request data

        Returns:
            Lead object containing the updated lead data
        """
        response = self.client.post("/api/v2/leads/subsequence/move", json=data.model_dump())
        return Lead.parse_obj(response) 