import polyscope as ps
import igl
import argparse
from integrators.forwardEuler import ForwardEulerIntegrator
from integrators.backwardEuler import BackwardEulerIntegrator
from integrators.symplecticEuler import SymplecticEulerIntegrator
from integrators.rungeKutta import RungeKuttaIntegrator
from derivatives.dV import dV_spring_particle_particle_dq
from derivatives.d2V import d2V_spring_particle_particle_dq2

# Simulation parameters
mass = 1.0
stiffness = 100.0
dt = 1e-2
integrator_type = ""
integrator = None
ps_spring, ps_spot = None, None

# Load data for animations
v1, _, _, f1, _, _ = igl.read_obj("data/spot.obj")
v2, _, _, f2, _, _ = igl.read_obj("data/spring.obj")

def force(q, qdot) -> float:
    return -dV_spring_particle_particle_dq(q, qdot, stiffness)

def stiff(q, qdot):
    return -d2V_spring_particle_particle_dq2(q, qdot, stiffness)

def callback():
    # Take a time step
    if integrator_type in ["fe", "se", "rk"]:
        integrator.step(dt, mass, force)
    elif integrator_type == "be":
        integrator.step(dt, mass, force, stiff)

    # Rigid transform for cow
    ps_spot.update_vertex_positions(integrator.rigid_transform(v1))
    # Scale x for spring
    ps_spring.update_vertex_positions(integrator.scale_x(v2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("integrator_type", type=str, default="fe")

    args = parser.parse_args()

    integrator_type = args.integrator_type

    if integrator_type == "fe":
        integrator = ForwardEulerIntegrator()
    elif integrator_type == "be":
        integrator = BackwardEulerIntegrator()
    elif integrator_type == "se":
        integrator = SymplecticEulerIntegrator()
    elif integrator_type == "rk":
        integrator = RungeKuttaIntegrator()

    ps.init()
    # Register the meshes
    ps_spot = ps.register_surface_mesh("spot", v1, f1, smooth_shade=True)
    ps_spring = ps.register_surface_mesh("spring", v2, f2, smooth_shade=True)
    # Set the callback function for the animation
    ps.set_user_callback(callback)
    # View the point cloud and mesh we just registered in the 3D UI
    ps.show()
    # Clean up the callbacks
    ps.clear_user_callback()
