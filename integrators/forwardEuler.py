from .base import Integrator

class ForwardEulerIntegrator(Integrator):
    def step(self, dt: float, mass: float, force: callable):
        f = force(self.q, self.qdot)

        self.q = self.q + dt * self.qdot
        self.qdot = self.qdot - (f / mass) * dt

        print(self.q)

        return
