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

# Running the game on the host
`docker-compose up -d`

# Creating a game session + Gameplay
1. Both players open the webpage with their client
2. One player Clicks the button `Create a Session`
    1. The player waits for the key generation and shares it with the other peer
    2. After the other player has shared their response key (3.2) the player clicks the button `Refresh`
3. The other player Clicks the button `Participate in a Session`
    1. The player enters the shared key
    2. The player clicks the button `Submit Offer Key`
4. Both players select at least one ship they want to place
5. Both players have to at least once click `Random placement` to place the ships on the grid.
6. After both players have clicked `Accept & Ready` the game is started and the player offering the session starts to shoot for the opponents ships.
7. The turns alternate whenever a players shot did not hit a target.
8. The game ends when one player sinks all of it's opponents ships.