"""
Block list entry API endpoints for Instantly.ai
"""

from typing import Optional, List
from uuid import UUID

from ..models.block_list_entry import BlockListEntry
from .base import BaseAPI

class BlockListEntryAPI(BaseAPI):
    """API endpoints for block list entries."""
    
    def create_block_list_entry(
        self,
        type: str,
        value: str,
        reason: Optional[str] = None,
        expires_at: Optional[str] = None
    ) -> BlockListEntry:
        """
        Create a new block list entry.
        
        Args:
            type: The type of block list entry (email or domain)
            value: The email or domain to block
            reason: Optional reason for blocking
            expires_at: Optional expiration date for the block
            
        Returns:
            The created block list entry
        """
        data = {
            "type": type,
            "value": value,
            "reason": reason,
            "expires_at": expires_at
        }
        data = {k: v for k, v in data.items() if v is not None}
        
        response = self._post("/block-lists-entries", json=data)
        return BlockListEntry(**response)
    
    def list_block_list_entries(
        self,
        workspace_id: Optional[UUID] = None,
        type: Optional[str] = None,
        limit: int = 100,
        starting_after: Optional[str] = None
    ) -> List[BlockListEntry]:
        """
        List block list entries.
        
        Args:
            workspace_id: Optional workspace ID to filter by
            type: Optional entry type to filter by
            limit: Maximum number of entries to return
            starting_after: Cursor for pagination
            
        Returns:
            List of block list entries
        """
        params = {
            "limit": limit,
            "starting_after": starting_after,
            "workspace_id": str(workspace_id) if workspace_id else None,
            "type": type
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self._get("/block-lists-entries", params=params)
        return [BlockListEntry(**entry) for entry in response["items"]]
    
    def get_block_list_entry(self, entry_id: str) -> BlockListEntry:
        """
        Get a specific block list entry.
        
        Args:
            entry_id: The ID of the block list entry
            
        Returns:
            The block list entry
        """
        response = self._get(f"/block-lists-entries/{entry_id}")
        return BlockListEntry(**response)
    
    def update_block_list_entry(
        self,
        entry_id: str,
        reason: Optional[str] = None,
        expires_at: Optional[str] = None
    ) -> BlockListEntry:
        """
        Update a block list entry.
        
        Args:
            entry_id: The ID of the block list entry
            reason: Optional new reason for blocking
            expires_at: Optional new expiration date
            
        Returns:
            The updated block list entry
        """
        data = {
            "reason": reason,
            "expires_at": expires_at
        }
        data = {k: v for k, v in data.items() if v is not None}
        
        response = self._patch(f"/block-lists-entries/{entry_id}", json=data)
        return BlockListEntry(**response)
    
    def delete_block_list_entry(self, entry_id: str) -> None:
        """
        Delete a block list entry.
        
        Args:
            entry_id: The ID of the block list entry to delete
        """
        self._delete(f"/block-lists-entries/{entry_id}") 