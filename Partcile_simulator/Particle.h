// Particle.h

#ifndef PARTICLE_H
#define PARTICLE_H

#include <array>
#include <vector>
#include <tuple>
#include <string>

class Particle {
public:
    Particle(double charge, double mass, const std::array<double, 3>& initial_velocity, const std::array<double, 3>& initial_position, const std::string& name);

    // Accessors for private members
    double getCharge() const;
    double getMass() const;
    std::string getName() const;

private:
    double charge;
    double mass;
    std::array<double, 3> velocity;
    std::array<double, 3> position;
    std::vector<std::tuple<double, double, double>> trajectory;
    std::string name;

    // Other members and functions...
};

#endif
