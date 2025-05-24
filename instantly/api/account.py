"""
Account API client for the Instantly.ai API
"""

from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from instantly.client import InstantlyClient
from instantly.models.account import Account, AccountCreate, AccountUpdate

class AccountAPI:
    """Client for the Account API endpoints."""
    
    def __init__(self, client: 'InstantlyClient'):
        """
        Initialize the Account API client.
        
        Args:
            client: The main Instantly.ai client
        """
        self._client = client
        
    def get_account(self, account_id: str) -> Account:
        """
        Get an account by ID.
        
        Args:
            account_id: The ID of the account to retrieve
            
        Returns:
            The account details
        """
        response = self._client.get(f"/api/v2/accounts/{account_id}")
        return Account.model_validate(response)
        
    def list_accounts(self, limit: Optional[int] = None, offset: Optional[int] = None) -> List[Account]:
        """
        List all accounts.
        
        Args:
            limit: Maximum number of accounts to return
            offset: Number of accounts to skip
            
        Returns:
            List of accounts
        """
        params = {}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
            
        response = self._client.get("/api/v2/accounts", params=params)
        return [Account.model_validate(account) for account in response["items"]]
        
    def create_account(self, account: AccountCreate) -> Account:
        """
        Create a new account.
        
        Args:
            account: The account details to create
            
        Returns:
            The created account
        """
        response = self._client.post("/api/v2/accounts", json=account.model_dump(by_alias=True))
        return Account.model_validate(response)
        
    def update_account(self, account_id: str, account: AccountUpdate) -> Account:
        """
        Update an existing account.
        
        Args:
            account_id: The ID of the account to update
            account: The updated account details
            
        Returns:
            The updated account
        """
        response = self._client.put(
            f"/api/v2/accounts/{account_id}",
            json=account.model_dump(by_alias=True, exclude_unset=True),
        )
        return Account.model_validate(response)
        
    def delete_account(self, account_id: str) -> None:
        """
        Delete an account.
        
        Args:
            account_id: The ID of the account to delete
        """
        self._client.delete(f"/api/v2/accounts/{account_id}") 