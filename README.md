
# NetShield

NetShield is an implementation of a sophisticated firewall system for a server-client interaction interface . The primary objectives of this project are to allow only valid IP addresses and monitor request rates effectively. This system ensures a secure and controlled communication environment, preventing unauthorized access and mitigating potential threats.It just simulates how a server handles the situation when it is flooded with multiple requests from a single source. For the scope of this project, I have considered only one client to contact the server at a time.  

## Features

#### Whitelisting and Blacklisting:

The firewall supports whitelisting and blacklisting of client IP addresses. Clients on the whitelist are granted access, while blacklisted clients are denied access. This feature ensures that communication is restricted to trusted sources, enhancing overall network security.

#### Request Rate Limiting:

To prevent abuse and potential denial-of-service attacks, SecureSocketGuard incorporates a request rate limiting feature. This monitors the rate at which requests are made and takes preventive measures when predefined thresholds are exceeded.

#### Customizable Configuration:

NetShield is highly customizable, allowing administrators to define and adjust security parameters based on the specific needs of the network environment. This flexibility ensures that the system can adapt to changing security requirements.

#### Trace File Logging:

NetShield introduces a trace file feature that keeps a detailed log of all events taking place during server-client communication. This trace file includes information about incoming connections, firewall actions, and other relevant events. The trace file serves as a valuable resource for analyzing and diagnosing issues, as well as for auditing and security monitoring purposes.

#### Blacklisting on Exceedance
When a client exceeds the maximum request rate limit multiple times within a specified range, the server blacklists the client, preventing further access.
## Installation

Clone the project

```bash
  https://github.com/Dark-Menace/NetShield.git
```

Go to the project directory

```bash
  cd NetShield
```
Install dependencies

```bash
  pip install -r requirements.txt

```




## Setting up the environment

#### LINUX

Add the server IPv4 address in the .env file and the client IPv4 address in the valid_ip.txt for whitelisting it.
```bash
#!/bin/bash

# Create or update .env file
echo "SERVER_IP=\"<Enter the server_ip>\"" >> .env
echo "PORT=3000" >> .env

# Create or update other text files
touch rate_limit.json
touch trace.json
touch blacklist.txt
echo "<Enter the client_ip>"  >> whitelist.txt

# Additional setup commands can be added as needed

echo "Setup complete!"
```

Execution permission for the bash file:
```bash
  chmod +x set_up.sh
```
Execute the bash script:
```bash
  ./set_up.sh
```

#### WINDOWS

Add the server IPv4 address in the .env file and the client IPv4 address in the valid_ip.txt for whitelisting it.
```batch
@echo off

:: Create or update .env file
echo SERVER_IP="<Enter the server_ip>" > .env
echo PORT=3000 >> .env

:: Create or update other text files
copy nul rate_limit.json
copy nul trace.json
copy nul blacklist.txt
echo Enter the client_ip > whitelist.txt

:: Additional setup commands can be added as needed

echo Setup complete!

```

Execute the bash script:
```bash
  setup.bat
```
## Usage

#### SERVER 

Run the server.py script and you can also customize the flag values to change the firewall configuration.

```bash
  python server.py
```

#### CLIENT

Run the client.py script and you can also customize the flag values to alter the messages sent.

```bash
  python client.py
```
## Help
```bash
 _____ _____ _____ _____ _____ _____ 
|   __|   __| __  |  |  |   __| __  |
|__   |   __|    -|  |  |   __|    -|
|_____|_____|__|__|\___/|_____|__|__|
                                     
usage: server.py <flags>

Server 1.1

options:
  -h, --help            show this help message and exit
  -r MAXREQ, --maxreq MAXREQ
                        Maximum requests the firewall allows the client to send at a time.
  -s SLEEPTIME, --sleeptime SLEEPTIME
                        Waiting time, if the request rate exceeds.
  -me MAXEXCEED, --maxexceed MAXEXCEED
                        Maximum times the firewall allows a client to exceed the request rate
                        limit.
```
```bash
 _____ __    _____ _____ _____ _____ 
|     |  |  |     |   __|   | |_   _|
|   --|  |__|-   -|   __| | | | | |  
|_____|_____|_____|_____|_|___| |_|  
                                     
usage: client.py <flags>

Client 1.1

options:
  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        Number of messages to be sent.
  -m MESSAGE, --message MESSAGE
                        Mulitiple messages to be sent separated by semicolon
```
## Example
```bash
python server.py -r 3 -s 20.0 -me 3
```
```bash
python client.py -n 3 -m "Hello;How are you;Im good"
```

## License

[MIT](https://choosealicense.com/licenses/mit/)


## Disclaimer

This tool is for educational purposes only. Use responsibly and ensure compliance with applicable laws and regulations.
