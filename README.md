# QA Automation Assignment 

## Configuration

Set environment variables:
```bash
export UOS_BASE_URL="https://127.0.0.1:11443/proxy/network/integration/v1/sites"
export UOS_SITE_ID="88f7af54-98f8-306a-a1c7-c9349722b1f6"
export UOS_API_KEY="hIMqFbTBgX1MA3yBDFEq9YSp1qEGofO3"
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
