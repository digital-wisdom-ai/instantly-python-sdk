"""
Background job API endpoints for Instantly.ai
"""

from typing import Optional, List
from uuid import UUID

from ..models.background_job import BackgroundJob
from .base import BaseAPI

class BackgroundJobAPI(BaseAPI):
    """API endpoints for background jobs."""
    
    def list_background_jobs(
        self,
        workspace_id: Optional[UUID] = None,
        type: Optional[str] = None,
        status: Optional[str] = None,
        limit: int = 100,
        starting_after: Optional[str] = None
    ) -> List[BackgroundJob]:
        """
        List background jobs.
        
        Args:
            workspace_id: Optional workspace ID to filter by
            type: Optional job type to filter by
            status: Optional job status to filter by
            limit: Maximum number of jobs to return
            starting_after: Cursor for pagination
            
        Returns:
            List of background jobs
        """
        params = {
            "limit": limit,
            "starting_after": starting_after,
            "workspace_id": str(workspace_id) if workspace_id else None,
            "type": type,
            "status": status
        }
        params = {k: v for k, v in params.items() if v is not None}
        
        response = self._get("/background-jobs", params=params)
        return [BackgroundJob(**job) for job in response["items"]]
    
    def get_background_job(self, job_id: str) -> BackgroundJob:
        """
        Get a specific background job.
        
        Args:
            job_id: The ID of the background job
            
        Returns:
            The background job
        """
        response = self._get(f"/background-jobs/{job_id}")
        return BackgroundJob(**response) 