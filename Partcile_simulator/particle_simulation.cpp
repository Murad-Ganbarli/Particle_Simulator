// ... (previous C++ code)

#include <iostream>
#include <cstring>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>

void sendToPython(const Eigen::Vector3d& position) {
    int clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket == -1) {
        std::cerr << "Error creating socket" << std::endl;
        return;
    }

    sockaddr_in serverAddress{};
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(8888);  // Adjust the port as needed
    serverAddress.sin_addr.s_addr = htonl(INADDR_LOOPBACK);

    if (connect(clientSocket, reinterpret_cast<const sockaddr*>(&serverAddress), sizeof(serverAddress)) == -1) {
        std::cerr << "Error connecting to Python server" << std::endl;
        close(clientSocket);
        return;
    }

    // Convert position to string
    std::string positionStr = std::to_string(position[0]) + "," +
                              std::to_string(position[1]) + "," +
                              std::to_string(position[2]);

    // Send position to Python
    send(clientSocket, positionStr.c_str(), positionStr.size(), 0);

    close(clientSocket);
}

int main() {
    // ... (previous C++ code)

    // Inside the loop where particle positions are updated
    for (int frame = 0; frame < frames; ++frame) {
        // ... (update particle positions and trajectories)
        
        // Send particle positions to Python for visualization
        for (const auto& particle : particles) {
            Eigen::Vector3d position = particle.getPosition();
            sendToPython(position);
        }

        // ... (rest of the simulation logic)
    }

    // ... (remaining C++ code)
    return 0;
}
