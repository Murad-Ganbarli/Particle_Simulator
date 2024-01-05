#include "Space.h"

Space::Space() {
    if (SDL_Init(SDL_INIT_VIDEO) != 0) {
        std::cerr << "SDL initialization failed: " << SDL_GetError() << std::endl;
        // Handle initialization failure
    }

    SDL_Window* window = SDL_CreateWindow("Particle Simulation", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 600, SDL_WINDOW_SHOWN);
    renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (!renderer) {
        std::cerr << "Failed to create SDL renderer: " << SDL_GetError() << std::endl;
        // Handle renderer creation failure
    }
}

Space::~Space() {
    SDL_DestroyRenderer(renderer);
    SDL_Quit();
}

void Space::addParticle(const Particle& particle) {
    particles.push_back(particle);
}

void Space::calculateElectricField(int particleId, std::array<double, 3>& electricField) {
    // Implement electric field calculation
    electricField = {0.0, 0.0, 0.0};

    const Particle& particle = particles[particleId];

    for (size_t otherParticleId = 0; otherParticleId < particles.size(); ++otherParticleId) {
        if (particleId != otherParticleId) {
            const Particle& otherParticle = particles[otherParticleId];

            std::array<double, 3> r = {particle.getPosition()[0] - otherParticle.getPosition()[0],
                                       particle.getPosition()[1] - otherParticle.getPosition()[1],
                                       particle.getPosition()[2] - otherParticle.getPosition()[2]};

            double distance = std::sqrt(r[0] * r[0] + r[1] * r[1] + r[2] * r[2]);

            std::array<double, 3> coulombField = (otherParticle.getCharge() / (4 * M_PI * otherParticle.getEpsilon0())) * r / std::pow(distance, 3);

            electricField += coulombField;
        }
    }
}

void Space::calculateMagneticField(const std::array<double, 3>& observationPoint, std::array<double, 3>& magneticField) {
    // Implement magnetic field calculation
    magneticField = {0.0, 0.0, 0.0};

    for (const Particle& particle : particles) {
        if (observationPoint != particle.getPosition()) {
            std::array<double, 3> r = {observationPoint[0] - particle.getPosition()[0],
                                       observationPoint[1] - particle.getPosition()[1],
                                       observationPoint[2] - particle.getPosition()[2]};

            double distance = std::sqrt(r[0] * r[0] + r[1] * r[1] + r[2] * r[2]);

            if (distance != 0) {
                std::array<double, 3> velocityCrossR = cross(particle.getVelocity(), r);

                std::array<double, 3> magneticFieldParticle = (particle.getMu0() * particle.getCharge() / (4 * M_PI)) * velocityCrossR / std::pow(distance, 3);

                magneticField += magneticFieldParticle;
            }
        }
    }
}

void Space::calculateGravitationalForce(const Particle& particle, std::array<double, 3>& gravitationalForce) {
    // Implement gravitational force calculation
    gravitationalForce = {0.0, 0.0, 0.0};

    for (const Particle& otherParticle : particles) {
        if (&particle != &otherParticle) {
            std::array<double, 3> r = {particle.getPosition()[0] - otherParticle.getPosition()[0],
                                       particle.getPosition()[1] - otherParticle.getPosition()[1],
                                       particle.getPosition()[2] - otherParticle.getPosition()[2]};

            double distance = std::sqrt(r[0] * r[0] + r[1] * r[1] + r[2] * r[2]);

            std::array<double, 3> gravitationalForceParticle = (particle.getGravityAcceleration() * particle.getMass() * otherParticle.getMass() / std::pow(distance, 2)) * r / distance;

            gravitationalForce += gravitationalForceParticle;
        }
    }
}

void Space::updateParticles(double dt) {
    for (size_t i = 0; i < particles.size(); ++i) {
        particles[i].update(dt);
    }
}

void Space::visualizeParticles(double dt, int frames, int interval, bool saveAsMp4) {
    bool quit = false;
    SDL_Event e;

    for (int frame = 0; frame < frames && !quit; ++frame) {
        while (SDL_PollEvent(&e)) {
            if (e.type == SDL_QUIT) {
                quit = true;
            }
        }

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        for (const Particle& particle : particles) {
            drawParticle(particle);
        }

        SDL_RenderPresent(renderer);
        SDL_Delay(interval);
    }

    if (saveAsMp4) {
        // Implement saving as MP4 (you may use an external library for this, like FFmpeg)
    }
}

void Space::drawParticle(const Particle& particle) {
    // Draw a simple point for each particle
    SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
    SDL_RenderDrawPoint(renderer, static_cast<int>(particle.getPosition()[0]), static_cast<int>(particle.getPosition()[1]));
}
