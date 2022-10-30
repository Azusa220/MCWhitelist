# MCWhitelist

Add player to whitelist from Discord bot

# Usage

Make sure you have set up Rcon in Server Properties

| Setting  | Example |
| ----------- | ------ |
|  rcon.port  | 25575  |
| enable-rcon  | true  |
| rcon.password  | minecraft  |

Example
```python
    server_address = "Localhost"
    server_pass = "minecraft"
    server_port = int("25575")

    with MCRcon(server_address, server_pass, server_port) as mcr: 
        resp = mcr.command("whitelist add " + username)
```

# Picture

![whitelist1](https://user-images.githubusercontent.com/112402169/198860553-54d02668-3eff-4a6a-9776-722d67763b69.png)
