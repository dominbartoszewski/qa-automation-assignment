def test_create_and_get_voucher(api_client, voucher_id):
    """Tworzy voucher i sprawdza, że można go pobrać."""
    resp = api_client.get(f"hotspot/vouchers/{voucher_id}")
    assert resp.status_code == 200, f"GET failed: {resp.text}"
    data = resp.json()
    assert data["id"] == voucher_id
    assert data["name"] == "qa_test_voucher"


def test_delete_voucher(api_client, voucher_id):
    """Usuwa voucher i sprawdza, że już go nie można pobrać."""
    delete_resp = api_client.delete(f"hotspot/vouchers/{voucher_id}")
    assert delete_resp.status_code in (200, 204), f"Delete failed: {delete_resp.text}"

    get_resp = api_client.get(f"hotspot/vouchers/{voucher_id}")
    assert get_resp.status_code in (404, 400), f"Voucher still exists: {get_resp.text}"
