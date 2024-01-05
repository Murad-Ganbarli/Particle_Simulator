// Particle.cpp

#include "Particle.h"

Particle::Particle(double charge, double mass, const std::array<double, 3>& initial_velocity, const std::array<double, 3>& initial_position, const std::string& name)
    : charge(charge), mass(mass), velocity(initial_velocity), position(initial_position), name(name) {
    // Other constructor initialization...
}

double Particle::getCharge() const {
    return charge;
}

double Particle::getMass() const {
    return mass;
}

std::string Particle::getName() const {
    return name;
}

// Other member function implementations...
