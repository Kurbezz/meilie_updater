import os

import httpx


response = httpx.get(
    "http://localhost:8080/api/v1/healthcheck",
    headers={"Authorization": os.environ["API_KEY"]},
)
print(f"HEALTHCHECK STATUS: {response.status_code}")
exit(0 if response.status_code == 200 else 1)
