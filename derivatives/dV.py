def dV_spring_particle_particle_dq(q: float, qdot: float, stiffness: float) -> float:
    return -1 * stiffness * q
