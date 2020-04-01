# UDP DoS

Denial of Service implementation using User Datagram Protocol. Developed and tested on CATLab machines.

## High-level architecture

<!--- HTML markdown to center the image --->
<p align="center">
    <img alt="architecture" src="img/architecture.png" width="700px" />
</p>


## Parts

- **UDP Server**: Simple UDP server listenning to all IPs on port 9000. Source: [server.py](src/server.py)
- **UDP Client**: Simple UDP client communicating with the UDP Server via short messages. Source: [client.py](src/client.py)
- **Bot Client**: Bot UDP Client sends messages of 1024 bytes long to the UDP Server at very high rates. Source: [bot_client.py](src/bot_client.py)
- **CPU Tracker**: Extra tool to track CPU usage of local machines. Used on the UDP Server during development. Source: [get_cpu.py](src/get_cpu.py)

## Sample Flow

1. Start the UDP Server
2. Start the UDP Client
3. Server and Client should be exchanging messages at this point
4. Add the first Bot Client
5. Add another
6. Our sample runs show that two bots are enough to DoS the server and time out regular client's session.
