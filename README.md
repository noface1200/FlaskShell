# Reverse Shell using Flask (Proof of Concept)

[!IMPORTANT]
this can only be used if you are on the same wifi connection, as the target machine although I am working on a workaround


This is a simple proof of concept for a reverse shell built with Python and the Flask framework. It allows a client to input commands on a webpage and execute them remotely on the target computer as long as they are in the same (Wi-Fi/LAN) network as you. This tool is for educational purposes only and should be used in a controlled environment for security research or ethical hacking practices.

## Features

- Flask web server: Flask is used to set up a simple HTTP server on the target machine.
- Command execution: Allows the execution of system commands from the client to the server.
- Local network only: Works within the same local network (Wi-Fi/LAN) for isolated testing.

## Example

![GIF](https://github.com/noface1200/FlaskShell/blob/main/git/flaskshell.gif?raw=true)

## Requirements

- Python 3.x
- Flask
- Requests

## Usage

### On the target machine (server)

1. Clone the repository
2. run "pip install flask requests
3. edit main.py and replace line 11's WEBHOOK_URL string with your webhook either on https://webhook.site/ or a discord webhook
4. run main.py

### On your machine
1. check your webhook and open the IP address you received in a web browser
