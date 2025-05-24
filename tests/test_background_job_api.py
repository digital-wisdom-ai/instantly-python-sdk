"""
Tests for the background job API endpoints
"""

import pytest
from unittest.mock import patch

from instantly.api.background_job import BackgroundJobAPI

def test_list_background_jobs(client, background_job_data):
    """Test listing background jobs."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = {"items": [background_job_data]}
        
        api = BackgroundJobAPI(client)
        jobs = api.list_background_jobs()
        
        assert len(jobs) == 1
        assert jobs[0].id == background_job_data["id"]
        assert jobs[0].type == background_job_data["type"]
        assert jobs[0].status == background_job_data["status"]
        
        mock_get.assert_called_once_with(
            "/background-jobs", params={"limit": 100}
        )

def test_list_background_jobs_with_filters(client, background_job_data):
    """Test listing background jobs with filters."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = {"items": [background_job_data]}
        
        api = BackgroundJobAPI(client)
        jobs = api.list_background_jobs(status="completed", limit=5, starting_after="abc123")
        
        assert len(jobs) == 1
        assert jobs[0].id == background_job_data["id"]
        mock_get.assert_called_once_with(
            "/background-jobs", params={"status": "completed", "limit": 5, "starting_after": "abc123"}
        )

def test_get_background_job(client, background_job_data):
    """Test getting a background job by ID."""
    with patch.object(client, 'get') as mock_get:
        mock_get.return_value = background_job_data
        
        api = BackgroundJobAPI(client)
        job = api.get_background_job(background_job_data["id"])
        
        assert job.id == background_job_data["id"]
        assert job.type == background_job_data["type"]
        assert job.status == background_job_data["status"]
        
        mock_get.assert_called_once_with(
            f"/background-jobs/{background_job_data['id']}", params=None
        ) 