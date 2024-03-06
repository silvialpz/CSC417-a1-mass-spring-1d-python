from .base import Integrator

class BackwardEulerIntegrator(Integrator):
    def step(self, dt: float, mass: float, force: callable, stiff: callable):
        f = force(self.q, self.qdot)

        q_prev = self.q
        qdot_prev = self.qdot

        self.q = self.q + dt * self.qdot
        self.qdot = self.qdot - dt * (f / mass)

        f = force(self.q, self.qdot)

        self.q = q_prev + self.qdot * dt
        self.qdot = qdot_prev - (f / mass) * dt

        return
