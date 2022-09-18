# Copyright 2022 Guillaume Belanger
# See LICENSE file for licensing details.

from enum import Enum


class RequestTrigger(Enum):
    LOC_CH = "LOC_CH"
    PRA_CH = "PRA_CH"
    UE_POLICY = "UE_POLICY"
