# The Safe Place Discord Bot
A simple python-based Discord bot for all the gamers to use.

## Features:
* Get a random cat picture when using the cat emoji.

<br>

# Installation Instructions
Pre-requisites:
* Pip3 & Python3
* Docker
<br>

Pull git project and install required Python modules using the command: <br>
```
pip install -r requirements.txt
```
<br>

Create a `secrets/.env` file and include required secrets in the format: <br>

```
APIKEY=
TOKEN=
```

To run the project locally:
```
python3 main.py
```

To run the project in a local container:
```
docker build -t discord-bot-img
docker run -it --rm --name tsp-discord-bot discord-bot-img
```
---
### Common Issues
#### Receiving an `SSLCertVerificationError`
* For Mac Users, go to MacintoshHD -> Applications -> Python3.x -> Double click "Install Certificates.commad"