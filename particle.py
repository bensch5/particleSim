import raylib
from pyray import *


class Particle:
    def __init__(self, p_id, pos_x, pos_y):
        match p_id:
            case 0:
                self.color = None
            case 1:
                self.color = YELLOW
            case 2:
                self.color = BLUE
            case _:
                raise ValueError('Wrong particle ID. No such particle exists.')
        self.p_id = p_id
        self.pos_x = pos_x
        self.pos_y = pos_y
