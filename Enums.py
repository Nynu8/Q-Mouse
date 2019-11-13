from enum import Enum
class TileType(Enum):
    GROUND = 0
    MOUSE = 1
    CAT = 2
    CHEESE = 3

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3