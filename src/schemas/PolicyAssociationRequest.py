# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from typing import List

from fiveg_core_common_schemas.AccessType import AccessType
from fiveg_core_common_schemas.Gpsi import Gpsi
from fiveg_core_common_schemas.GroupId import GroupId
from fiveg_core_common_schemas.Guami import Guami
from fiveg_core_common_schemas.Ipv4Addr import Ipv4Addr
from fiveg_core_common_schemas.Ipv6Addr import Ipv6Addr
from fiveg_core_common_schemas.NetworkId import NetworkId
from fiveg_core_common_schemas.NfInstanceId import NfInstanceId
from fiveg_core_common_schemas.Pei import Pei
from fiveg_core_common_schemas.RatType import RatType
from fiveg_core_common_schemas.Supi import Supi
from fiveg_core_common_schemas.SupportedFeatures import SupportedFeatures
from fiveg_core_common_schemas.TimeZone import TimeZone
from fiveg_core_common_schemas.Uri import Uri
from fiveg_core_common_schemas.UserLocation import UserLocation
from pydantic import BaseModel

from schemas.UePolicyRequest import UePolicyRequest


class PolicyAssociationRequest(BaseModel):
    notificationUri: Uri
    altNotifIpv4Addrs: List[Ipv4Addr] = None
    altNotifIpv6Addrs: List[Ipv6Addr] = None
    supi: Supi
    gpsi: Gpsi = None
    accessType: AccessType = None
    pei: Pei = None
    userLoc: UserLocation = None
    timeZone: TimeZone = None
    servingPlmn: NetworkId = None
    ratType: RatType = None
    groupIds: List[GroupId] = None
    hPcfId: str = None
    uePolReq: UePolicyRequest = None
    guami: Guami = None
    serviceName: str = None
    servingNfId: NfInstanceId = None
    suppFeat: SupportedFeatures
