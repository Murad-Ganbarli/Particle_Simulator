# Particle Simulator

This is a simple particle simulator written in C++.

## Dependencies
- C++ compiler (e.g., g++)
- [matplotlib-cpp](https://github.com/lava/matplotlib-cpp) (for visualization)

## How to Compile and Run
1. Make sure you have a C++ compiler installed (e.g., g++).
2. Install matplotlib-cpp by following the instructions [here](https://github.com/lava/matplotlib-cpp).
3. Open a terminal and navigate to the project directory.
4. Compile the code using the following command:
   ```bash
   g++ main.cpp Particle.cpp space.cpp -o simulator -std=c++11
