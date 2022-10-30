from mcrcon import MCRcon
import interactions
from interactions.ext.wait_for import wait_for,setup

Token = "TOKEN"

bot = interactions.Client(token=Token, intents = interactions.Intents.ALL)

@bot.command(
    name="whitelist",
    description="Add a player to the whitelist",
        options = [
            interactions.Option(
                name="player",
                description="mcid",
                type=interactions.OptionType.STRING,
                required=True,
            ),
        ]
)

async def whitelist(ctx: interactions.CommandContext, player: str):
    print(player)
    username = player
    embed = interactions.Embed(title=f":white_check_mark: {player} has been added to the white list!", color=0xdb8b00)
    await ctx.send(embeds=embed)

    server_address = "ServerAddress"
    server_pass = "RconPassword"
    server_port = int("RconPort")

    with MCRcon(server_address, server_pass, server_port) as mcr: 
        resp = mcr.command("whitelist add " + username)
        
    print(resp)

bot.start()
