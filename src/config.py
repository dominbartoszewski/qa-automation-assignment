import os

# Test environment configuration
BASE_URL = os.getenv("UOS_BASE_URL", "https://<your_local_ip>/proxy/network/integration/v1/sites")
SITE_ID = os.getenv("UOS_SITE_ID", "<your_site_id>")
API_KEY = os.getenv("UOS_API_KEY", "<your_api_key>")
VERIFY_SSL = os.getenv("UOS_VERIFY_SSL", "false").lower() == "true"
