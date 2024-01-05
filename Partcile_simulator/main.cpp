// main.cpp

#include <iostream>
#include "Particle.h"

int main() {
    // Test Particle class
    Particle electron(-1.602e-19, 9.109e-31, {0, 0, 0}, {0, 0, 0}, "Electron-1");

    std::cout << "Particle Info:" << std::endl;
    std::cout << "Name: " << electron.getName() << std::endl;
    std::cout << "Charge: " << electron.getCharge() << std::endl;
    std::cout << "Mass: " << electron.getMass() << std::endl;

    return 0;
}
