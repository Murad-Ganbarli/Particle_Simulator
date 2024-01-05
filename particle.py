# particle.py
import numpy as np
from constants import ELECTRON_CHARGE, ELECTRON_MASS, MU_ZERO, EPSILON_ZERO, GRAVITY_ACCELERATION

class Particle:
    def __init__(self, charge, mass, initial_velocity=[0,0,0], initial_position=[0,0,0], name=__name__):
        self.name = name
        self.charge = charge
        self.mass = mass
        self.velocity = np.array(initial_velocity, dtype=float)
        self.position = np.array(initial_position, dtype=float)
        self.trajectory = []  # List to store trajectory points

        # Constants for the particle
        self.epsilon_0 = EPSILON_ZERO  # Permittivity of free space
        self.mu_0 = MU_ZERO  # Permeability of free space
        self.gravity_acceleration = GRAVITY_ACCELERATION  # Acceleration due to gravity
