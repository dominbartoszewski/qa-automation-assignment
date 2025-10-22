import os

# Test environment configuration
BASE_URL = os.getenv("UOS_BASE_URL", "https://127.0.0.1:11443/proxy/network/integration/v1/sites")
SITE_ID = os.getenv("UOS_SITE_ID", "88f7af54-98f8-306a-a1c7-c9349722b1f6")
API_KEY = os.getenv("UOS_API_KEY", "hIMqFbTBgX1MA3yBDFEq9YSp1qEGofO3")
VERIFY_SSL = os.getenv("UOS_VERIFY_SSL", "false").lower() == "true"
