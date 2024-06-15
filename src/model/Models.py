import string
from dataclasses import dataclass


@dataclass
class CameraRegistryModel:
    uuid: string
    ip: string
    name: string