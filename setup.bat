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
