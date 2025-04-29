import requests
import json
import time

token = "" # token here

headers = {
    "Authorization": token,
    "Content-Type": "application/json"
}

response = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=headers)
if response.status_code != 200:
    print(f"Failed to fetch guilds. Status Code: {response.status_code}")
    exit()

guilds = response.json()
gtags = [guild for guild in guilds if "GUILD_TAGS" in guild.get("features", [])]

if not gtags:
    print("No servers found with GUILD_TAGS.")
    exit()

print(f"Found clan tags.")

headers2 = {
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    'Accept-Encoding': "gzip, deflate, br, zstd",
    'Content-Type': "application/json",
    'Authorization': token,
    'x-discord-locale': "en-US",
    'origin': "https://discord.com",
    'accept-language': "en-US,en;q=0.9",
    'priority': "u=1, i",
}

while True:
    for guild in gtags:
        payload = {
            "identity_guild_id": guild["id"],
            "identity_enabled": True
        }

        response = requests.put("https://discord.com/api/v9/users/@me/clan", data=json.dumps(payload), headers=headers2)
        
        if response.status_code == 200:
            print(f"Changed to: {guild['name']} (ID: {guild['id']})")
        else:
            print(f"Failed to change clan for {guild['name']} - Status Code: {response.status_code}")
            print(response.text)

        time.sleep(2)  
