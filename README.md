
# NetShield

NetShield is a robust server-client interaction interface designed to enhance security through the implementation of a sophisticated firewall system. The primary objectives of this project are to allow only valid IP addresses and monitor request rates effectively. This system ensures a secure and controlled communication environment, preventing unauthorized access and mitigating potential threats.

## Features

#### IP Whitelisting:

NetShield employs an advanced IP whitelisting mechanism, allowing only specified IP addresses to connect to the server. This feature ensures that communication is restricted to trusted sources, enhancing overall network security.

#### Request Rate Limiting:

To prevent abuse and potential denial-of-service attacks, SecureSocketGuard incorporates a request rate limiting feature. This monitors the rate at which requests are made and takes preventive measures when predefined thresholds are exceeded.

#### Customizable Configuration:

NetShield is highly customizable, allowing administrators to define and adjust security parameters based on the specific needs of the network environment. This flexibility ensures that the system can adapt to changing security requirements.

#### Trace File Logging:

NetShield introduces a trace file feature that keeps a detailed log of all events taking place during server-client communication. This trace file includes information about incoming connections, firewall actions, and other relevant events. The trace file serves as a valuable resource for analyzing and diagnosing issues, as well as for auditing and security monitoring purposes.
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
touch rate_limit.txt
touch trace.json
echo "<Enter the client_ip>"  >> valid_ip.txt

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
copy nul rate_limit.txt
copy nul trace.json
echo Enter the client_ip > valid_ip.txt

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
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Disclaimer

This tool is for educational purposes only. Use responsibly and ensure compliance with applicable laws and regulations.
