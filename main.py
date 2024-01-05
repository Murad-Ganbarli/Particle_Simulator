# main.py
from particle import Particle
from space import Space

# Example usage
space = Space(x_range=(-1e-9, 1e9), y_range=(-1e-9, 1e-9), z_range=(-1e-9, 1e-9))

particles = [
    Particle(charge=-1.602e-19, mass=9.109e-31, initial_velocity=[0, 0, 0], initial_position=[-1e-6, 0, 0], name="C1"),
    Particle(charge=-1.602e-19, mass=2*9.109e-31, initial_velocity=[0, 0, 0], initial_position=[1e-6, 0, 0], name="C2"),
    Particle(charge=1.602e-19, mass=3*9.109e-31, initial_velocity=[0, 0, 0], initial_position=[0.5e-6, 1e-6, 0], name="C3"),
]

for particle in particles:
    space.add_particle(particle)

# Visualize the particle motion with trajectories and electromagnetic effects
space.visualize_particles(dt=1e-12, frames =100 , interval =20 , save_as_mp4=True )
