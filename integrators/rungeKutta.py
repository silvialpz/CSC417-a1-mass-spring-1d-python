from .base import Integrator

class RungeKuttaIntegrator(Integrator):
    def step(self, dt, mass, force):
        q1 = self.q
        qdot1 = self.qdot
        f1 = force(q1, qdot1)

        k1 = qdot1
        k1dot = f1 / mass

        q2 = self.q + k1 * dt / 2
        qdot2 = self.qdot - k1dot * dt / 2
        f2 = force(q2, qdot2)

        k2 = qdot2
        k2dot = f2 / mass

        q3 = self.q + k2 * dt / 2
        qdot3 = self.qdot - k2dot * dt / 2
        f3 = force(q3, qdot3)

        k3 = qdot3
        k3dot = f3 / mass

        q4 = self.q + k3 * dt
        qdot4 = self.qdot - k3dot * dt
        f4 = force(q4, qdot4)

        k4 = qdot4
        k4dot = f4 / mass

        self.q = self.q + dt * (k1 + 2 * k2 + 2 * k3 + k4) / 6
        self.qdot = self.qdot - dt * (k1dot + 2 * k2dot + 2 * k3dot + k4dot) / 6

        return
