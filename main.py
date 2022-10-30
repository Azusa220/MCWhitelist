from mcrcon import MCRcon
import interactions
from interactions.ext.wait_for import wait_for,setup

Token = "TOKEN"

bot = interactions.Client(token=Token, intents = interactions.Intents.ALL)

@bot.command(
    name="whitelist",
    description="ホワイトリストにプレイヤーを追加します",
        options = [
            interactions.Option(
                name="player",
                description="ユーザー名",
                type=interactions.OptionType.STRING,
                required=True,
            ),
        ]
)

async def whitelist(ctx: interactions.CommandContext, player: str):
    print(player)
    username = player
    embed = interactions.Embed(title=f":white_check_mark: {player} がホワイトリストに追加されました！", color=0xdb8b00)
    await ctx.send(embeds=embed)

    server_address = "サーバーアドレス"
    server_pass = "rcon パスワード"
    server_port = int("rcon ポート")

    with MCRcon(server_address, server_pass, server_port) as mcr: 
        resp = mcr.command("whitelist add " + username)
        
    print(resp)

bot.start()
