# -*- coding: utf-8 -*-

from inori.ems.messager import EMSMessager

from inori.ems.settings import (
    EMS_MESSAGER,
    EMS_MESSAGER_SETTINGS,
)

messager = EMSMessager(EMS_MESSAGER, EMS_MESSAGER_SETTINGS)
