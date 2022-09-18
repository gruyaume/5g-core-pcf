# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.


from fastapi.testclient import TestClient

from main import app

BASE_URL = "npcf-ue-policy-control/v1"
POLICIES_ENDPOINT = f"{BASE_URL}/policies"


def test_given_policy_association_request_when_create_policy_then_():
    client = TestClient(app)
    policy_association_request = {"notificationUri": "abcd", "suppFeat": "1234", "supi": "1234"}

    response = client.post(f"{POLICIES_ENDPOINT}/", json=policy_association_request)

    assert response.status_code == 201
