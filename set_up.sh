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