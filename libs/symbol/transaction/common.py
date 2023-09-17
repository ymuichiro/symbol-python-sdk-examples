from enum import Enum


class FeeConfig(Enum):
    free = 0
    slow = 1
    normal = 1.2
    fast = 2
