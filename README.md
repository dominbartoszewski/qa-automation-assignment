# QA Automation Assignment 

## Configuration

Set environment variables:
```bash
export UOS_BASE_URL="https://<your_local_ip>/proxy/network/integration/v1/sites"
export UOS_SITE_ID="<your_site_id>"
export UOS_API_KEY="<your_api_key>"
export UOS_VERIFY_SSL=false
```

## Run tests
```bash
pip install -r requirements.txt
pytest -v --alluredir=reports/
```

## Test Flow
1. POST /hotspot/vouchers → create test voucher  
2. GET /hotspot/vouchers/{id} → verify creation  
3. DELETE /hotspot/vouchers/{id} → remove  
4. GET /hotspot/vouchers/{id} → expect 404 or 400
