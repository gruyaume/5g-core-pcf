# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

import uuid

from fastapi import APIRouter, Response

from schemas.PolicyAssociationRequest import PolicyAssociationRequest
from schemas.PolicyAssociation import PolicyAssociation


router = APIRouter()


@router.post(
    path="/",
    status_code=201,
    response_model=PolicyAssociation,
)
async def create_policy(
    policy_association_request: PolicyAssociationRequest,
    response: Response,
):

    """"""

    # Here the PCF Is supposed to assign a UE policy association ID

    """
    - shall determine the applicable UE policy as detailed in subclause 4.2.2.2, for the V-PCF taking into
    consideration any policy received from the H-PCF in the reply to the possible request for the Creation of a policy
    association;
    - if the PCF is a V-PCF and determines that UE policy needs to be provisioned, shall use the
    Namf_Communication service specified in 3GPP TS 29.518 [14] to provision the UE policy according to
    subclause 4.2.2.2 and as follows:
      (i) the V-PCF shall subscribe at the AMF to notifications of N1 messages for UE Policy Delivery Results using
    the Namf_Communication_N1N2MessageSubscribe service operation;
      (ii) the V-PCF shall send the determined UE policy using Namf_Communication_N1N2MessageTransfer service
    operation(s); and
      (iii) the V-PCF shall be prepared to receive UE Policy Delivery Results from the AMF within the
    Namf_Communication_N1MessageNotify service operation and if the received UE Policy Delivery results
    relate to UE policy sections provided by the H-PCF shall use the Npcf_UEPolicyControl_Update Service
    Operation to send those UE Policy Delivery results to the H-PCF; 
    """
    policy_association_id = str(uuid.uuid4())
    response.headers["Location"] = f"/policies/{policy_association_id}"
    return PolicyAssociation(
        suppFeat=policy_association_request.suppFeat,
        request=policy_association_request,
    )
