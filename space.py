import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
from particle import Particle
from constants import *

# space.py
import numpy as np
from constants import ELECTRON_CHARGE, ELECTRON_MASS, MU_ZERO, EPSILON_ZERO, GRAVITY_ACCELERATION

class Space:
    def __init__(self, x_range=(-1e-9, 1e9), y_range=(-1e-9, 1e-9), z_range=(-1e-9, 1e-9)):
        self.x_range = x_range
        self.y_range = y_range
        self.z_range = z_range
        self.particles = []

    def add_particle(self, particle):
        self.particles.append(particle)

    def calculate_electric_field(self, particle_id):
        electric_field = np.zeros(3)
        particle = self.particles[particle_id]

        for other_particle_id, other_particle in enumerate(self.particles):
            if particle_id != other_particle_id:
                r = particle.position - other_particle.position
                distance = np.linalg.norm(r)
                coulomb_field = (other_particle.charge / (4 * np.pi * particle.epsilon_0)) * r / distance**3
                electric_field += coulomb_field

        return electric_field

    def calculate_magnetic_field(self, observation_point):
        magnetic_field = np.zeros(3)
        for particle in self.particles:
            if not np.array_equal(observation_point, particle.position):
                r = observation_point - particle.position
                velocity_cross_r = np.cross(particle.velocity, r)
                magnetic_field_particle = (particle.mu_0 * particle.charge / (4 * np.pi)) * velocity_cross_r / np.linalg.norm(r)**3
                magnetic_field += magnetic_field_particle
        return magnetic_field

    def calculate_gravitational_force(self, particle):
        gravitational_force = np.zeros(3)
        for other_particle in self.particles:
            if particle != other_particle:
                r = particle.position - other_particle.position
                distance = np.linalg.norm(r)
                gravitational_force_particle = (GRAVITY_ACCELERATION * particle.mass * other_particle.mass / distance**2) * r / distance
                gravitational_force += gravitational_force_particle
        return gravitational_force

    def update_particles(self, dt):
        for i, particle in enumerate(self.particles):
            # Calculate electric, magnetic, and gravitational fields at the particle positions
            electric_field = self.calculate_electric_field(i)
            magnetic_field = self.calculate_magnetic_field(particle.position)
            gravitational_force = self.calculate_gravitational_force(particle)

            # Update velocity using Lorentz force equation and gravitational force
            lorentz_force = particle.charge * (electric_field + np.cross(particle.velocity, magnetic_field))
            total_force = lorentz_force + gravitational_force
            acceleration = total_force / particle.mass
            particle.velocity += acceleration * dt

            # Update position using the updated velocity
            particle.position += particle.velocity * dt

            # Store current position in the trajectory list
            particle.trajectory.append(tuple(particle.position.copy()))

    def visualize_particles(self, dt=1e-11, frames =range(10000) , interval = 300 , save_as_mp4=False):
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')

        start_time = time.time()  # Record start time

        def update(frame, dt=dt):
            nonlocal start_time  # Use the start_time variable defined outside the function

            ax.clear()

            # Update particle positions and trajectories at each frame
            self.update_particles(dt=dt)

            for particle_id, particle in enumerate(self.particles):
                # Update position using the updated velocity
                particle.position += particle.velocity * dt

                # Store current position in the trajectory list
                particle.trajectory.append(tuple(particle.position.copy()))

                # Plot trajectory lines
                if len(particle.trajectory) > 1:
                    trajectory_points = np.array(particle.trajectory)
                    ax.plot(
                        trajectory_points[:, 0], trajectory_points[:, 1], trajectory_points[:, 2],
                        linestyle='--', color='gray'
                    )

                # Plot particle positions
                ax.scatter(
                    particle.position[0], particle.position[1], particle.position[2],
                    marker='o', label=particle.name
                )

                # Plot electric field vector
                electric_field = self.calculate_electric_field(particle_id)
                ax.quiver(
                    particle.position[0], particle.position[1], particle.position[2],
                    electric_field[0], electric_field[1], electric_field[2],
                    color='blue', label='Electric Field', length=1e-18, normalize=True, arrow_length_ratio=0.3
                )

            # Calculate and display elapsed time
            elapsed_time = time.time() - start_time
            ax.text2D(0.05, 0.95, f'Time: {elapsed_time:.2f} seconds', transform=ax.transAxes)

        ani = FuncAnimation(fig, update, frames=frames, interval=interval, repeat=False)

        # Set up plot parameters
        ax.set_xlim(self.x_range)
        ax.set_ylim(self.y_range)
        ax.set_zlim(self.z_range)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()

        if save_as_mp4:
            ani.save('particle_motion.mp4', writer='ffmpeg', fps=30)

        plt.show()

# Example usage
if __name__=="__main__":
    space = Space(x_range=(-1e-9, 1e9), y_range=(-1e-9, 1e-9), z_range=(-1e-9, 1e-9))

    # Create one proton and one electron within the specified space
    particles = [
        Particle(charge=ELECTRON_CHARGE, mass=ELECTRON_MASS, initial_velocity=[0, 0, 0], initial_position=[-1e-6, 0, 0], name="Electron-1"),
        Particle(charge=-ELECTRON_CHARGE, mass=ELECTRON_MASS, initial_velocity=[1e4, 0, 0], initial_position=[1e-6, 0, 0], name="Positron-1"),
        Particle(charge=-ELECTRON_CHARGE, mass=ELECTRON_MASS, initial_velocity=[1e4, 0, 0], initial_position=[0.5e-6, 1e-6, 0], name="Positron-2"),
        
    ]

    for particle in particles:
        space.add_particle(particle)

    # Visualize the particle motion with trajectories and electromagnetic effects
    space.visualize_particles(dt=1e-11)
