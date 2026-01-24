# webrtc-battleship
A vibe coded PoC of the game battleship  P2P playable through WebRTC

# Build
`docker build -t  battleship .`

Specifically pull the latest coturn/coturn image to ensure you have the right architecture image pulled
`docker pull coturn/coturn:latest`

# Adjust & ensure
- WebRTC username and password in
  - `coturn.conf`
  - `index.html`
- TURN cli username and password
  - in `coturn.conf`
- required udp ports for TURN server are exposed on your host

# Before run
- execute in directory on host to ensure operability
  - `dos2unix entrypoint.sh`
  - `chmod +x entrypoint.sh` 

# Run
`docker-compose up -d`
