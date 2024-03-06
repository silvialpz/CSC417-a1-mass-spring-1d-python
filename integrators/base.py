import numpy as np

class Integrator:
    def __init__(self, q=1.0, qdot=0.0):
        self.q = q
        self.qdot = qdot

    def step(self):
        pass

    def rigid_transform(self, vertices: np.ndarray) -> np.ndarray:
        """Move vertices by q in x dimension"""
        return vertices + np.array([[self.q, 0, 0]])

    def scale_x(self, vertices: np.ndarray) -> np.ndarray:
        """Scale vertices in x dimension by q"""
        return vertices * np.array([[self.q, 1, 1]])
