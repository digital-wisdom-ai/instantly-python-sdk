# Instantly.ai Python SDK

A Python SDK for interacting with the Instantly.ai API.

## Installation

### Using pip
```bash
pip install instantly-python-sdk
```

### Using uv
```bash
uv pip install instantly-python-sdk
```

## Development

1. Clone the repository
2. Install development dependencies:

Using pip:
```bash
pip install -e ".[dev]"
```

Using uv:
```bash
uv pip install -e ".[dev]"
```

3. Run tests:
```bash
pytest
```

## Usage

```python
from instantly import InstantlyClient, InstantlyConfig

# Initialize the client
config = InstantlyConfig(
    api_key="your-api-key",
    base_url="https://api.instantly.ai",  # Optional: defaults to production API URL
    timeout=30  # Optional: defaults to 30 seconds
)
client = InstantlyClient(config)

# List all accounts
accounts = client.accounts.list_accounts()

# Get a specific account
account = client.accounts.get_account("account-id")

# Create a new account
new_account = client.accounts.create_account({
    "name": "My Account",
    "email": "account@example.com",
    "timezone": "UTC"
})

# Update an account
updated_account = client.accounts.update_account("account-id", {
    "name": "Updated Account Name"
})

# Delete an account
client.accounts.delete_account("account-id")

# Use as a context manager
with InstantlyClient(config) as client:
    accounts = client.accounts.list_accounts()
```

## License

MIT
