"""
Configuration for the Instantly.ai SDK
"""

from typing import Optional

from pydantic import Field, SecretStr

class InstantlyConfig:
    """Configuration for the Instantly.ai SDK client."""
    
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.instantly.ai/api/v2",
        timeout: int = 30,
    ):
        """
        Initialize the Instantly.ai SDK configuration.
        
        Args:
            api_key: Your Instantly.ai API key
            base_url: The base URL for the API (defaults to v2 API)
            timeout: Request timeout in seconds
        """
        self.api_key = SecretStr(api_key)
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        
    @property
    def headers(self) -> dict[str, str]:
        """Get the headers required for API authentication."""
        return {
            "Authorization": f"Bearer {self.api_key.get_secret_value()}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        } 