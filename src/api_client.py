import requests

class UOSApiClient:
    """Klient API do komunikacji z UniFi OS Server (Integration API)."""

    def __init__(self, base_url, api_key, verify_ssl = False):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.verify = verify_ssl
        self.session.headers.update({
            "X-API-KEY": api_key,
            "Accept": "application/json",
            "Content-Type": "application/json"
        })

    def get(self, endpoint):
        return self.session.get(f"{self.base_url}/{endpoint}")

    def post(self, endpoint, payload):
        return self.session.post(f"{self.base_url}/{endpoint}", json=payload)

    def delete(self, endpoint):
        return self.session.delete(f"{self.base_url}/{endpoint}")
