import numpy as np

class Integrator:
    def __init__(self, q=1, qdot=0):
        self.q = q
        self.qdot = qdot

    def step(self):
        raise NotImplementedError

    def rigid_transform(self, v):
        return v + np.array([[self.q, 0, 0]])

    def scale_x(self, v):
        return v * np.array([[self.q, 1, 1]])
