import numpy as np

class Fruit:
    x: float
    y: float
    v_x: float
    v_y: float
    radius: float
    tier: int

    def __init__(self, x, y, radius, tier, v_x = 0 , v_y = 0):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.radius = radius
        self.tier = tier

    def to_array(self):
        return np.array([self.x. self.y, self.v_x, self.v_y, self.radius, self.tier])