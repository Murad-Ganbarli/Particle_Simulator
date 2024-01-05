from space import Space
from particle import Particle
from constants import ELECTRON_CHARGE, ELECTRON_MASS
import numpy as np

space = Space()

for i in range(20):
    space.add_particle(
        Particle(charge=ELECTRON_CHARGE*np.random.randint(-1, 1),
                 mass=ELECTRON_MASS,
                 #initial_velocity=np.random.uniform(-1e6, 1e6,  size=(3)),
                 initial_position=np.random.uniform(-1e-6, 1e-6,  size=(3))
                 
    ))
space.visualize_particles(dt=1e-12)
