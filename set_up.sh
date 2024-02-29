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