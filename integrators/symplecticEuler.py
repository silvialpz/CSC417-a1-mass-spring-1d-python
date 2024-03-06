from .base import Integrator

class SymplecticEulerIntegrator(Integrator):
    def step(self, dt: float, mass: float, force: callable):
        """ TODO: Take a time step of the mass spring system using Symplectic Euler

        Args:
            dt : the time step in seconds
            mass : the mass
            force(q, qdot) : a function that computes the force acting on the mass. This takes q and qdot as parameters.
        Output:
            q : set q to the updated generalized coordinate using Backward Euler time integration
            qdot : set qdot to the updated generalized velocity using Backward Euler time integration
        """
        self.q = 0          # TODO: Update q and qdot properties
        self.qdot = 0
        raise NotImplementedError
