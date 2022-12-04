import raylib
from pyray import *


class Particle:
    def __init__(self, p_id, pos_x, pos_y):
        match p_id:
            case 0:  # empty tile
                self.color = BLACK
            case 1:  # sand
                self.color = YELLOW
            case 2:  # water
                self.color = BLUE
            case _:
                raise ValueError('Wrong particle ID. No such particle exists.')
        self.p_id = p_id
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __repr__(self):
        match self.p_id:
            case 0: return ' '
            case 1: return 'sand'
            case 2: return 'water'
