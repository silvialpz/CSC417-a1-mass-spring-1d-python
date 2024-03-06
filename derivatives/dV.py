def dV_spring_particle_particle_dq(q, qdot, stiffness) -> float:
    return -1 * stiffness * q
