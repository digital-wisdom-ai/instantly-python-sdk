"""
Tests for the base client functionality
"""

import pytest
import httpx

from instantly import InstantlyClient, InstantlyConfig

def test_client_initialization(config):
    """Test client initialization."""
    client = InstantlyClient(config)
    assert client.config == config
    assert isinstance(client._client, httpx.Client)
    assert str(client._client.base_url).rstrip("/") == config.base_url.rstrip("/")
    timeout = client._client.timeout
    assert timeout.connect == config.timeout
    assert timeout.read == config.timeout
    assert timeout.write == config.timeout
    assert timeout.pool == config.timeout

def test_client_headers(config):
    """Test client headers."""
    client = InstantlyClient(config)
    headers = client._client.headers
    
    assert "Authorization" in headers
    assert headers["Authorization"] == f"Bearer {config.api_key.get_secret_value()}"
    assert headers["Content-Type"] == "application/json"
    assert headers["Accept"] == "application/json"

def test_client_close(config):
    """Test client close method."""
    client = InstantlyClient(config)
    client.close()
    # The client should be closed and not raise an error
    with pytest.raises(Exception):
        client.get("/test") 