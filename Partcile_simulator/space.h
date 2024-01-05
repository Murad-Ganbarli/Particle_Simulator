// space.h

#ifndef SPACE_H
#define SPACE_H

#include <vector>
#include "Particle.h"

class Space {
public:
    Space(double x_range[2] = {-1e-9, 1e9}, double y_range[2] = {-1e-9, 1e-9}, double z_range[2] = {-1e-9, 1e-9});

    void addParticle(const Particle& particle);
    void calculateElectricField(int particle_id, std::array<double, 3>& electric_field);
    void calculateMagneticField(const std::array<double, 3>& observation_point, std::array<double, 3>& magnetic_field);
    void calculateGravitationalForce(const Particle& particle, std::array<double, 3>& gravitational_force);
    void updateParticles(double dt);
    void visualizeParticles(double dt, int frames, int interval, bool save_as_mp4);

private:
    double x_range[2];
    double y_range[2];
    double z_range[2];
    std::vector<Particle> particles;
};

#endif
