# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from fiveg_core_common_schemas.SupportedFeatures import SupportedFeatures
from pydantic import BaseModel

from schemas.PolicyAssociationRequest import PolicyAssociationRequest
from schemas.RequestTrigger import RequestTrigger
from schemas.UePolicy import UePolicy


class PolicyAssociation(BaseModel):
    request: PolicyAssociationRequest = None
    uePolicy: UePolicy = None
    triggers: List[RequestTrigger] = None
    # pras: map[PresenceInfo]  # TODO: Implement
    suppFeat: SupportedFeatures
