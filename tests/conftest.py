import pytest
from src.api_client import UOSApiClient
from src import config


@pytest.fixture(scope="session")
def api_client():
    """Tworzy klienta API do komunikacji z UOS Server."""
    base = f"{config.BASE_URL}/{config.SITE_ID}"
    return UOSApiClient(base_url=base, api_key=config.API_KEY, verify_ssl=config.VERIFY_SSL)


@pytest.fixture
def voucher_id(api_client):
    """Tworzy testowy voucher przed testem i usuwa go po teście."""
    payload = {
        "count": 1,
        "name": "qa_test_voucher",
        "timeLimitMinutes": 5,
        "authorizedGuestLimit": 1
    }
    create_resp = api_client.post("hotspot/vouchers", payload)
    assert create_resp.status_code == 201, f"Voucher creation failed: {create_resp.text}"

    data = create_resp.json()
    assert "vouchers" in data, f"Unexpected response: {data}"
    voucher = data["vouchers"][0]
    voucher_id = voucher.get("id")

    yield voucher_id

    delete_resp = api_client.delete(f"hotspot/vouchers/{voucher_id}")
    if delete_resp.status_code not in (200, 204, 404):
        raise AssertionError(f"Cleanup failed: {delete_resp.text}")
