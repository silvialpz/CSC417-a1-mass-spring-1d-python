from .base import Integrator

class SymplecticEulerIntegrator(Integrator):
    def step(self, dt, mass, force):
        f = force(self.q, self.qdot)

        self.qdot = self.qdot - (f / mass) * dt
        self.q = self.q + dt * self.qdot

        return
