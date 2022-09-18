# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from fastapi import APIRouter

from api.npcf_ue_policy_control.v1.endpoints import policies

api_router = APIRouter()
api_router.include_router(
    policies.router,
    prefix="/npcf-ue-policy-control/v1/policies",
)
