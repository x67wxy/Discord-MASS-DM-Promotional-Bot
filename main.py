import discord
from discord.ext import commands, tasks

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ #

 # Edit Prefix Here!
i_am_1337_dogla = "1337"

# Add Your Bot Token Here
dogla_fenix_tkn = "OTg2NzAxNDU2MzczNjA4NDg4.GPBhXm.QQAwZJe1l9-lJisb8pPh3r9jCRJ9t8Zz3xVIA0"

intents = discord.Intents.all() # No Edit Needed

FenixPlayZxDogla = commands.Bot(command_prefix=i_am_1337_dogla, intents=intents)


@FenixPlayZxDogla.event
async def on_ready():
    print(f"Bot Ready")

#### EDIT HERE ####
@FenixPlayZxDogla.event
async def on_member_join(member):
    dogla_fenix = discord.Embed(
        title="FenixPlayZ",
        description=
        f"Hey, {member.mention} Join [DOGLA](https://discord.gg/dogla)")
    dogla_fenix.set_thumbnail(
        url=
        "https://cdn.discordapp.com/banners/853810604842287136/8b9d79d894d2e704335a7841d9b38dbb.png?size=512")
    dogla_fenix.set_image(
        url=
        "https://cdn.discordapp.com/banners/853810604842287136/8b9d79d894d2e704335a7841d9b38dbb.png?size=512")
    dogla_fenix.set_footer(
        text="FenixPlayZ",
        icon_url=
        "https://cdn.discordapp.com/banners/853810604842287136/8b9d79d894d2e704335a7841d9b38dbb.png?size=512")
    await member.send(
        f"Hello, {member.mention}",embed=dogla_fenix,mention_author=True)

#MassDm [ Note It Only DM's In Particular Server!!!!]
# Usage: {prefix}dm <msg_to_dm>
@commands.is_owner()
@FenixPlayZxDogla.command(alases=['dm'])
async def send_dm(ctx, *, message: str):
    for dogla in list(ctx.guild.members):
        try:
            await dogla.send(message)
            print(f"Sending DM")
        except:
            print(f"Error While Sending!!")

#######################################
FenixPlayZxDogla.run(dogla_fenix_tkn)
