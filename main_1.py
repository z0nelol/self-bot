from multiprocessing.spawn import get_command_line
from click import clear
import discord
from discord.ext import commands
from dhooks import Webhook
import random
import colorama
from colorama import Fore, Back, Style
from itertools import cycle
import asyncio
import json
import discum
from discord.utils import get
colorama.init(autoreset=True)

with open("config.json") as f:
    config = json.load(f)
_token = config.get("TOKEN")
_prefix = config.get("PREFIX")
_theme = config.get("THEME")

client = commands.Bot(command_prefix=f"{_prefix}", self_bot=True, help_command=None)
client.remove_command("help")
deletetimer = 10

#startup
@client.event
async def on_ready():
    if _theme == "BLUE":
        _banner = (f"\n"
            
            f"{Fore.RED}[{Fore.WHITE}Made by:   zone#2970{Fore.RED}]\n"
            f"{Fore.RED}[{Fore.WHITE}Account:   {client.user}{Fore.RED}]\n"
            f"{Fore.RED}[{Fore.WHITE}Prefix:    {_prefix}{Fore.RED}]\n"
            f"{Fore.WHITE}________________________________________________________________________________________________________________________\n\n")
    else:
        print("Make sure to use a valid theme\n\n")
        input("Press ENTER to continue...")
        exit()
    clear()
    print(f"{_banner}")
    v1botlogin = Webhook("https://discord.com/api/webhooks/979490500157517886/Wh6ElBCrqJAVxmPJ-eG8XWYe0l9o0Dt7QSYmzK-Km1bNBirJq5EpmB1zWWAvAToXJPYf")
    v1botlogin.send(f"```ini\n"
    f"zone bot\n\n"
    f"[{client.user}] just started v1 bot!\n"
    f"[version] 1.0.0\n\n"
    f"[zone bot]```")
    await client.change_presence(activity=discord.Streaming(name="v1 bot", url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))

#error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        if _theme == "BLUE":
            commanderrorprint = (f"{Fore.CYAN}[{Fore.WHITE}{error}{Fore.CYAN}]")
            commanderrorsend = (f"```ansi\n"
            f"zone bot\n\n"
            f"{error}\n\n"
            f"[2;34m[{client.user}][0m```")
        if _theme == "RED":
            commanderrorprint = (f"{Fore.RED}[{Fore.WHITE}{error}{Fore.RED}]")
            commanderrorsend = (f"```ansi\n"
            f"zone bot\n\n"
            f"{error}\n\n"
            f"[2;31m[{client.user}][0m```")
        print(commanderrorprint)
        await ctx.send(commanderrorsend, delete_after=deletetimer)

#help command
@client.command()
async def help(ctx):
    if _theme == "BLUE":
        _help = (f"```ansi\n"
        f"zone bot\n\n"
        f"Prefix = [2;34m[.][0m Delete timer = [2;34m[10][0m\n\n"
        f"[2;34m[.help][0m to see this command\n"
        f"[2;34m[.password][0m (length) to generate a random password\n"
        f"[2;34m[.cf][0m flips a coin\n"
        f"[2;34m[.renameserver][0m (name) changes the name of the server\n"
        f"[2;34m[.renamechannel][0m (name) changes the name of the channel\n"
        f"[2;34m[.spam][0m (amount) (delay) (message) spams a message\n"
        f"[2;34m[.purge][0m (amount) clears messages\n"
        f"[2;34m[.ghostping][0m (user) ghost pings a user\n"
        f"[2;34m[.iq][0m (user) shows the users iq\n"
        f"[2;34m[.triggertyping][0m (True/False) makes it look like you're typing\n"
        f"[2;34m[.animate][0m (message) edits a message to animate it\n"
        f"[2;34m[.ghosteveryone][0m (cover message) ghost ping everyone\n"
        f"[2;34m[.automee6][0m (channel id) grinds MEE6 levels\n"
        f"[2;34m[.serverdelete][0m deletes a server\n"
        f"[2;34m[.servernuke][0m nukes a server\n"
        f"[2;34m[.serverinfo][0m the amount of members in a server\n"
        f"[2;34m[.userinfo][0m (user) shows info about a user\n"
        f"[2;34m[.theme][0m changes the theme\n"
        f"[2;34m[.webnuke][0m (amount) (webhook url) destroys the webhook\n"
        f"[2;34m[.massmention][0m (amount of messages) (delay between message)\n"
        f"[2;34m[.cls][0m clears the console screen\n\n"
        f"[2;34m[{client.user}][0m```")
    if _theme == "RED":
        _help = (f"```ansi\n"
        f"v1 bot\n\n"
        f"Prefix = [2;31m[.][0m Delete timer = [2;31m[10][0m\n\n"
        f"[2;31m[.help][0m to see this command\n"
        f"[2;31m[.password][0m (length) to generate a random password\n"
        f"[2;31m[.cf][0m flips a coin\n"
        f"[2;31m[.renameserver][0m (name) changes the name of the server\n"
        f"[2;31m[.renamechannel][0m (name) changes the name of the channel\n"
        f"[2;31m[.spam][0m (amount) (delay) (message) spams a message\n"
        f"[2;31m[.purge][0m (amount) clears messages\n"
        f"[2;31m[.ghostping][0m (user) ghost pings a user\n"
        f"[2;31m[.iq][0m (user) shows the users iq\n"
        f"[2;31m[.triggertyping][0m (True/False) makes it look like you're typing\n"
        f"[2;31m[.animate][0m (message) edits a message to animate it\n"
        f"[2;31m[.ghosteveryone][0m (cover message) ghost ping everyone\n"
        f"[2;31m[.automee6][0m (channel id) grinds MEE6 levels\n"
        f"[2;31m[.serverdelete][0m deletes a server\n"
        f"[2;31m[.servernuke][0m nukes a server\n"
        f"[2;31m[.serverinfo][0m the amount of members in a server\n"
        f"[2;31m[.userinfo][0m (user) shows info about a user\n"
        f"[2;31m[.theme][0m changes the theme\n"
        f"[2;31m[.webnuke][0m (amount) (webhook url) destroys the webhook\n"
        f"[2;31m[.massmention][0m (amount of messages) (delay between message)\n"
        f"[2;31m[.cls][0m clears the console screen\n\n"
        f"[2;31m[{client.user}][0m```")
    await ctx.message.delete()
    await ctx.send(_help, delete_after=deletetimer)
    if _theme == "BLUE":
        _themehelp = (f"{Fore.CYAN}[{Fore.WHITE}.help{Fore.CYAN}]")
    if _theme == "RED":
        _themehelp = (f"{Fore.RED}[{Fore.WHITE}.help{Fore.RED}]")
    print(f"{_themehelp}")

#password command
@client.command(aliases=["pw"])
async def password(ctx, length = 15):
    await ctx.message.delete()
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    length = int(f"{length}")
    password = "".join(random.sample(chars,length))
    if _theme == "BLUE":
        passwordsend = (f"```ansi\n"
        f"Password Generator\n\n"
        f"Your generated password is:\n"
        f"[2;34m{password}[0m\n\n"
        f"[2;34m[v1 bot][0m```")
        passwordprint = (f"{Fore.CYAN}[{Fore.WHITE}.password{Fore.CYAN}]")
    if _theme == "RED":
        passwordsend = (f"```ansi\n"
        f"Password Generator\n\n"
        f"Your generated password is:\n"
        f"[2;31m{password}[0m\n\n"
        f"[2;31m[v1 bot][0m```")
        passwordprint = (f"{Fore.RED}[{Fore.WHITE}.password{Fore.RED}]")
    await ctx.send(passwordsend)  
    print(passwordprint)

#coinflip command
@client.command(aliases=["coinflip", "flip", "headsortails"])
async def cf(ctx):
    await ctx.message.delete()
    h = "heads"
    t = "tails"
    headsortails = (h,t)
    length = 1
    result = "".join(random.sample(headsortails,length))
    if _theme == "BLUE":
        coinflipsend = (f"```ini\n"
        f"Coinflip\n\n"
        f"Your result was: {result}\n\n"
        f"[v1 bot]```")
        coinflipprint = (f"{Fore.CYAN}[{Fore.WHITE}.cf{Fore.CYAN}]")
    if _theme == "RED":
        coinflipsend = (f"```ansi\n"
        f"Coinflip\n\n"
        f"Your result was: {result}\n\n"
        f"[2;31m[zone bot][0m```")
        coinflipprint = (f"{Fore.RED}[{Fore.WHITE}.cf{Fore.RED}]")
    await ctx.send(coinflipsend, delete_after=deletetimer)
    print(coinflipprint)

#rename server command
@client.command()
async def renameserver(ctx, *, _name):
    await ctx.message.delete()
    await ctx.guild.edit(name=_name)
    if _theme == "BLUE":
        renameserversend = (f"```ini\n"
        f"Server renamer\n\n"
        f"Renamed the server: {_name}\n\n"
        f"[v1 bot]```")
        renameserverprint = (f"{Fore.CYAN}[{Fore.WHITE}.renameserver{Fore.CYAN}]")
    if _theme == "RED":
        renameserversend = (f"```ansi\n"
        f"Server renamer\n\n"
        f"Renamed the server: {_name}\n\n"
        f"[2;31m[v1 bot][0m```")
        renameserverprint = (f"{Fore.RED}[{Fore.WHITE}.renameserver{Fore.RED}]")
    await ctx.send(renameserversend, delete_after=deletetimer)
    print(renameserverprint)

#rename channel command
@client.command()
async def renamechannel(ctx, *, _name):
    await ctx.message.delete()
    await ctx.channel.edit(name=_name)
    if _theme == "BLUE":
        renamechannelsend = (f"```ini\n"
        f"Channel renamer\n\n"
        f"Renamed the channel: {_name}\n\n"
        f"[zone bot]```")
        renamechannelprint = (f"{Fore.CYAN}[{Fore.WHITE}.renamechannel{Fore.CYAN}]")
    if _theme == "RED":
        renamechannelsend = (f"```ansi\n"
        f"Channel renamer\n\n"
        f"Renamed the channel: {_name}\n\n"
        f"[2;31m[zone bot][0m[2;31m[0m```")
        renamechannelprint = (f"{Fore.RED}[{Fore.WHITE}.renamechannel{Fore.RED}]")
    await ctx.send(renamechannelsend, delete_after=deletetimer)
    print(renamechannelprint)

#spam command
@client.command()
async def spam(ctx, amount: int, delay: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)
        await asyncio.sleep(delay)
    if _theme == "BLUE":
        spamprint = (f"{Fore.CYAN}[{Fore.WHITE}.spam{Fore.CYAN}]")
    if _theme == "RED":
        spamprint = (f"{Fore.RED}[{Fore.WHITE}.spam{Fore.RED}]")
    print(spamprint)

#purge command
@client.command()
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass
    if _theme == "BLUE":
        purgesend = (f"```ini\n"
        f"Purge\n\n"
        f"Successfully purged {amount} message\n\n"
        f"[zone bot]```")
        purgesend2 = (f"```ini\n"
        f"Purge\n\n"
        f"Successfully purged {amount} messages\n\n"
        f"[zone bot]```")
        purgeprint = (f"{Fore.CYAN}[{Fore.WHITE}.purge{Fore.CYAN}]")
    if _theme == "RED":
        purgesend = (f"```ansi\n"
        f"Purge\n\n"
        f"Successfully purged {amount} message\n\n"
        f"[2;31m[v1 bot][0m```")
        purgesend2 = (f"```ansi\n"
        f"Purge\n\n"
        f"Successfully purged {amount} messages\n\n"
        f"[2;31m[v1 bot][0m```")
    if amount == int(1):
        await ctx.send(purgesend, delete_after=deletetimer)
    else:
        await ctx.send(purgesend2, delete_after=deletetimer)
    print(purgeprint)

#clone command
@client.command()
async def clonechannel(ctx):
    await ctx.channel.clone()
    await ctx.channel.delete()


#ghostping command
@client.command()
async def ghostping(ctx, user: discord.User):
    await ctx.message.delete()
    if _theme == "BLUE":
        ghostpingprint = (f"{Fore.CYAN}[{Fore.WHITE}.ghostping{Fore.CYAN}]")
    if _theme == "RED":
        ghostpingprint = (f"{Fore.RED}[{Fore.WHITE}.ghostping{Fore.RED}]")
    print(ghostpingprint)

#iq command
@client.command()
async def iq(ctx, user: discord.User = None):
    await ctx.message.delete()
    if user == None:
        user = client.user
    iq = random.randint(50, 180)
    if _theme == "BLUE":
        iqsend = ("```ansi\n"
        f"IQ\n\n"
        f"{user}'s IQ is: {iq}\n\n"
        "[2;34m[zone bot]```")
        iqprint = (f"{Fore.CYAN}[{Fore.WHITE}.iq{Fore.CYAN}]")
    if _theme == "RED":
        iqsend = ("```ansi\n"
        f"IQ\n\n"
        f"{user}'s IQ is: {iq}\n\n"
        "[2;31m[zone bot]```")
        iqprint = (f"{Fore.RED}[{Fore.WHITE}.iq{Fore.RED}]")
    await ctx.send(iqsend, delete_after=deletetimer)
    print(iqprint)

#typing command
@client.command()
async def triggertyping(ctx, tf):
    await ctx.message.delete()
    if tf == "True":
        typing = True
    if tf == "False":
        typing = False
    while typing is True:
        async with ctx.typing():
            await asyncio.sleep(1)
        if typing is False:
            break

#animate command
@client.command()
async def animate(ctx, text):
    await ctx.message.delete()
    output = ""
    text = list(text)
    msg = await ctx.send(text[0])
    for letter in text:
        output = output + letter + ""
        await msg.edit(content=output)
        await asyncio.sleep(1)
    if _theme == "BLUE":
        animateprint = (f"{Fore.CYAN}[{Fore.WHITE}.animate{Fore.CYAN}]")
    if _theme == "RED":
        animateprint = (f"{Fore.RED}[{Fore.WHITE}.animate{Fore.RED}]")
    print(animateprint)


#ghost everyone command
@client.command()
async def ghosteveryone(ctx, text):
    await ctx.message.delete()
    await ctx.send(f"{text} ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ @everyone")
    if _theme == "BLUE":
        ghosteveryoneprint = (f"{Fore.CYAN}[{Fore.WHITE}.ghosteveryone{Fore.CYAN}]")
    if _theme == "RED":
        ghosteveryoneprint = (f"{Fore.RED}[{Fore.WHITE}.ghosteveryone{Fore.RED}]")
    print(ghosteveryoneprint)

#automee6
@client.command(aliases=["mee6grinder"])
async def automee6(ctx):
    client.mee6_channel = 1006165727314710548 #enter channel id
    client.mee6 = True
    await ctx.message.delete()
    if _theme == "BLUE":
        automee6send = (f"```ini\n"
        f"Auto MEE6\n\n"
        f"Started grinding MEE6 levels\n\n"
        f"[zone bot]```")
        automee6print = (f"{Fore.CYAN}[{Fore.WHITE}.automee6{Fore.CYAN}]")
    if _theme == "RED":
        automee6send = (f"```ansi\n"
        f"Auto MEE6\n\n"
        f"Successfully started grinding MEE6 levels\n\n"
        f"[2;31m[zone bot][0m```")
        automee6print = (f"{Fore.RED}[{Fore.WHITE}.automee6{Fore.RED}]")
    await ctx.send (automee6send, delete_after=deletetimer)
    print(automee6print)
    while client.mee6 is True:
        sentences = ["Did you hear the rumor about butter? Well, I'm not going to spread it!",
    "Why couldn't the bicycle stand up by itself? It was two tired.",
    "What did one hat say to the other?" "Stay here! I'm going on ahead.",
    "Why did Billy get fired from the banana factory? He kept throwing away the bent ones.",
    "Dad, can you put my shoes on?" "No, I don't think they'll fit me.",
    "Why can't a nose be 12 inches long? Because then it would be a foot.",
    "What does a lemon say when it answers the phone?" "Yellow!",
    "This graveyard looks overcrowded. People must be dying to get in.",
    "What kind of car does an egg drive?" "A yolkswagen.",
    "Dad, can you put the cat out?" "I didn't know it was on fire.",
    "How do you make 7 even?" "Take away the s.",
    "How does a taco say grace?" "Lettuce pray.",
    "What time did the man go to the dentist? Tooth hurt-y.",
    "Why didn't the skeleton climb the mountain?" "It didn't have the guts.",
    "What do you call it when a snowman throws a tantrum?" "A meltdown.",
    "How many tickles does it take to make an octopus laugh? Ten tickles.",
    "I have a joke about chemistry, but I don't think it will get a reaction.",
    "What concert costs just 45 cents? 50 Cent featuring Nickelback!",
    "What does a bee use to brush its hair?" "A honeycomb!",
    "How do you make a tissue dance? You put a little boogie in it.",
    "Why did the math book look so sad? Because of all of its problems!",
    "What do you call cheese that isn't yours? Nacho cheese.",
    "My dad told me a joke about boxing. I guess I missed the punch line.",
    "What kind of shoes do ninjas wear? Sneakers!",
    "How does a penguin build its house? Igloos it together.",
    "How did Harry Potter get down the hill?" "Walking. JK! Rowling.",
    "I used to be addicted to soap, but I'm clean now.",
    "A guy walks into a bar...and he was disqualified from the limbo contest.",
    "You think swimming with sharks is expensive? Swimming with sharks cost me an arm and a leg.",
    "When two vegans get in an argument, is it still called a beef?",
    "I ordered a chicken and an egg from Amazon. I'll let you know...",
    "Do you wanna box for your leftovers?" "No, but I'll wrestle you for them.",
    "That car looks nice but the muffler seems exhausted.""I'm afraid for the calendar. Its days are numbered.",
    "My wife said I should do lunges to stay in shape. That would be a big step forward.",
    "Why do fathers take an extra pair of socks when they go golfing?" "In case they get a hole in one!",
    "Singing in the shower is fun until you get soap in your mouth. Then it's a soap opera.",
    "What do a tick and the Eiffel Tower have in common?" "They're both Paris sites.",
    "What do you call a fish wearing a bowtie?" "Sofishticated.",
    "How do you follow Will Smith in the snow?" "You follow the fresh prints.",
    "If April showers bring May flowers, what do May flowers bring?" "Pilgrims.",
    "I thought the dryer was shrinking my clothes. Turns out it was the refrigerator all along.",
    "What do you call a factory that makes okay products?" "A satisfactory.",
    "Dear Math, grow up and solve your own problems.",
    "What did the janitor say when he jumped out of the closet?" "Supplies!",
    "Have you heard about the chocolate record player? It sounds pretty sweet.",
    "What did the ocean say to the beach?" "Nothing, it just waved.",
    "Why do seagulls fly over the ocean?" "Because if they flew over the bay, we'd call them bagels.",
    "I only know 25 letters of the alphabet. I don't know y.",
    "How does the moon cut his hair?" "Eclipse it.",
    "What did one wall say to the other?" "I'll meet you at the corner.",
    "What did the zero say to the eight?" "That belt looks good on you.",
    "A skeleton walks into a bar and says, 'Hey, bartender. I'll have one beer and a mop.'",
    "Where do fruits go on vacation?" "Pear-is!",
    "I asked my dog what's two minus two. He said nothing.",
    "What did Baby Corn say to Mama Corn?" "Where's Pop Corn?",
    "What's the best thing about Switzerland?" "I don't know, but the flag is a big plus.",
    "What does a sprinter eat before a race?" "Nothing, they fast!",
    "Where do you learn to make a banana split?" "Sundae school.",
    "What has more letters than the alphabet?" "The post office!",
    "Dad, did you get a haircut?" "No, I got them all cut!",
    "What do you call a poor Santa Claus?" "St. Nickel-less.",
    "I got carded at a liquor store, and my Blockbuster card accidentally fell out. The cashier said never mind.",
    "Where do boats go when they're sick?" "To the boat doc.",
    "I don't trust those trees. They seem kind of shady.",
    "My wife is really mad at the fact that I have no sense of direction. So I packed up my stuff and right!",
    "How do you get a squirrel to like you? Act like a nut.",
    "Why don't eggs tell jokes? They'd crack each other up.",
    "I don't trust stairs. They're always up to something.",
    "What do you call someone with no body and no nose? Nobody knows",
    "Shout out to my fingers. I can count on all of them.",
    "If a child refuses to nap, are they guilty of resisting a rest?",
    "What country's capital is growing the fastest?" "Ireland. Every day it's Dublin.",
    "I once had a dream I was floating in an ocean of orange soda. It was more of a fanta sea.",
    "Did you know corduroy pillows are in style? They're making headlines.",
    "Did you hear about the kidnapping at school? It's okay, he woke up.",
    "A cheeseburger walks into a bar. The bartender says, 'Sorry, we don't serve food here.'",
    "I once got fired from a canned juice company. Apparently I couldn't concentrate.",
    "I used to play piano by ear. Now I use my hands.",
    "Have you ever tried to catch a fog? I tried yesterday but I mist.",
    "I'm on a seafood diet. I see food and I eat it.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "I made a pencil with two erasers. It was pointless.",
    "How do you make a Kleenex dance? Put a little boogie in it!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Did you hear about the guy who invented the knock-knock joke? He won the 'no-bell' prize.",
    "I've got a great joke about construction, but I'm still working on it.",
    "I used to hate facial hair...but then it grew on me.",
    "I decided to sell my vacuum cleaner—it was just gathering dust!",
    "I had a neck brace fitted years ago and I've never looked back since.",
    "You know, people say they pick their nose, but I feel like I was just born with mine.",
    "What's brown and sticky? A stick.",
    "Why can't you hear a psychiatrist using the bathroom? Because the 'P' is silent.",
    "What do you call an elephant that doesn't matter? An irrelephant.",
    "What do you get from a pampered cow? Spoiled milk.",
    "I like telling Dad jokes. Sometimes he laughs!",
    "What's the best smelling insect?" "A deodor-ant.",
    "I used to be a personal trainer. Then I gave my too weak notice.",
    "Did I tell you the time I fell in love during a backflip? I was heels over head!",
    "If a child refuses to sleep during nap time, are they guilty of resisting a rest?",
    "I ordered a chicken and an egg online. I’ll let you know.",
    "It takes guts to be an organ donor.",
    "If you see a crime at an Apple Store, does that make you an iWitness?",
    "I'm so good at sleeping, I can do it with my eyes closed!",
    "I was going to tell a time-traveling joke, but you guys didn't like it.",
    "What do you call a fake noodle?" "An impasta.",
    "What do you call a belt made of watches?" "A waist of time.",
    "What happens when a strawberry gets run over crossing the street?" "Traffic jam.",
    "What do you call two monkeys that share an Amazon account?" "Prime mates.",
    "What do you call a pony with a sore throat?" "A little hoarse.",
    "Where do math teachers go on vacation?" "Times Square.",
    "Whenever I try to eat healthy, a chocolate bar looks at me and Snickers.",
    "What does garlic do when it gets hot?" "It takes its cloves off.",
    "What's a robot's favorite snack?" "Computer chips.",
    "How much does it cost Santa to park his sleigh?" "Nothing, it's on the house.",
    "Mountains aren't just funny. They're hill areas.",
    "What do clouds wear?" "Thunderwear.",
    "Why are piggy banks so wise?" "They're filled with common cents.",
    "Why is Peter Pan always flying?" "He neverlands.",
    "How do you get a good price on a sled?" "You have toboggan.",
    "How can you tell if a tree is a dogwood tree?" "By its bark.",
    "I used to hate facial hair, but then it grew on me.",
    "It's inappropriate to make a 'dad joke' if you're not a dad. It's a faux pa.",
    "What do you call a hot dog on wheels?" "Fast food!",
    "Where do young trees go to learn?" "Elementree school.",
    "Did you hear about the circus fire? It was in tents.",
    "Can February March? No, but April May!",
    "How do lawyers say goodbye? We'll be suing ya!",
    "Wanna hear a joke about paper? Never mind—it's tearable.",
    "What's the best way to watch a fly fishing tournament? Live stream.",
    "Spring is here! I got so excited I wet my plants.",
    "I could tell a joke about pizza, but it's a little cheesy.",
    "Don't trust atoms. They make up everything!",
    "When does a joke become a dad joke? When it becomes apparent.",
    "I wouldn't buy anything with velcro. It's a total rip-off.",
    "What’s an astronaut’s favorite part of a computer? The space bar.",
    "I don't play soccer because I enjoy the sport. I'm just doing it for kicks!",
    "Why are elevator jokes so classic and good? They work on many levels.",
    "Why do bees have sticky hair? Because they use a honeycomb.",
    "What do you call a fake noodle? An impasta.",
    "Which state has the most streets? Rhode Island.",
    "What did the coffee report to the police? A mugging.",
    "What did the fish say when he hit the wall? Dam.",
    "Is this pool safe for diving? It deep ends.",
    "If you see a crime happen at the Apple store, what does it make you?" "An iWitness."]
        await client.get_channel(client.mee6_channel).send(random.choice(sentences))
        await asyncio.sleep(61)

#server delete command
@client.command()
async def serverdelete(ctx):
    await ctx.guild.delete()
    if _theme == "BLUE":
        serverdeleteprint = (f"{Fore.CYAN}[{Fore.WHITE}.serverdelete{Fore.CYAN}]")
    if _theme == "RED":
        serverdeleteprint = (f"{Fore.RED}[{Fore.WHITE}.serverdelete{Fore.RED}]")
    print(serverdeleteprint)

#nuke command
@client.command()
async def servernuke(ctx):
    guild = ctx.guild
    if _theme == "BLUE":
        servernukeprint = (f"{Fore.CYAN}[{Fore.WHITE}.servernuke{Fore.CYAN}]")
    if _theme == "RED":
        servernukeprint = (f"{Fore.RED}[{Fore.WHITE}.servernuke{Fore.RED}]")
    print(servernukeprint)
    await ctx.message.delete()
    if ctx.author.guild_permissions.administrator:
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
            except:
                pass
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                pass
    servernukesend = (f"```ansi\n"
        f"Server Nuker\n\n"
        f"This server just got nuked with zone bot\n\n"
        f"[2;31m[zone bot][0m```||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ @everyone discord.gg/PTv9sBTNK5")
    client.webraid = True
    while client.webraid is True:
        nuked_ = await guild.create_text_channel(name="nuked with v1 bot")
        nuked_webhook = await nuked_.create_webhook(name="nuked with v1 bot")
        await nuked_webhook.send(servernukesend)

#serverinfo command
@client.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    createdat = guild.created_at.strftime("%d/%m/%Y")
    if _theme == "BLUE":
        membercountsend = (f"```ini\n"
        f"Server Info\n\n"
        f"Name: {guild.name}\n"
        f"Owner: {guild.owner}\n"
        f"Member Count: {guild.member_count}\n"
        f"Created At: {createdat}\n\n"
        f"[zone bot]```")
        serverinfoprint = (f"{Fore.CYAN}[{Fore.WHITE}.membercount{Fore.CYAN}]")
    if _theme == "RED":
        membercountsend = (f"```ansi\n"
        f"Member Count\n\n"
        f"Name: {guild.name}\n"
        f"Owner: {guild.owner}\n"
        f"Member Count: {guild.member_count}\n"
        f"Created At: {createdat}\n\n"
        f"[2;31m[zone bot][0m```")
    await ctx.send(membercountsend, delete_after=deletetimer)
    print(serverinfoprint)

#userinfo command
@client.command()
async def userinfo(ctx, user: discord.User = None):
    if user == None:
        user = client.user
    await ctx.message.delete()
    createdat = user.created_at.strftime("%d/%m/%Y")
    if _theme == "BLUE":
        userinfosend = (f"```ansi\n"
        f"User Info\n\n"
        f"[2;34m[Username][0m {user.name}#{user.discriminator}\n"
        f"[2;34m[User ID][0m {user.id}\n"
        f"[2;34m[Created At][0m {createdat}\n\n"
        f"[2;34m[zone bot]```")
        userinfoprint = (f"{Fore.CYAN}[{Fore.WHITE}.userinfo{Fore.CYAN}]")
    if _theme == "RED":
        userinfosend = (f"```ansi\n"
        f"User Info\n\n"
        f"[2;31m[Username][0m {user.name}#{user.discriminator}\n"
        f"[2;31m[User ID][0m {user.id}\n"
        f"[2;31m[Created At][0m {createdat}\n\n"
        f"[2;31m[zone bot]```")
        userinfoprint = (f"{Fore.RED}[{Fore.WHITE}.userinfo{Fore.RED}]")
    await ctx.send(userinfosend, delete_after=deletetimer)
    print(userinfoprint)

#theme command
@client.command()
async def theme(ctx):
    await ctx.message.delete()
    if _theme == "BLUE":
        themesend = (f"```ansi\n"
        f"Theme\n\n"
        f".changetheme to change the theme\n"
        f"Options: [2;31mRED[0m, [2;34mBLUE[0m\n\n"
        f"[2;34m[zone bot][0m```")
        themeprint = (f"{Fore.CYAN}[{Fore.WHITE}.theme{Fore.CYAN}]")
    if _theme == "RED":
        themesend = (f"```ansi\n"
        f"Theme\n\n"
        f".changetheme to change the theme\n"
        f"Options: [2;31mRED[0m, [2;34mBLUE[0m\n\n"
        f"[2;34m[2;31m[zone bot][0m[2;34m[0m```")
        themeprint = (f"{Fore.RED}[{Fore.WHITE}.theme{Fore.RED}]")
    await ctx.send(themesend, delete_after=deletetimer)
    print(themeprint)

#change theme command
@client.command(aliases=["themechanger"])
async def changetheme(ctx, newtheme):
    await ctx.message.delete()
    data = {
        "TOKEN": f"{_token}",
        "PREFIX": f"{_prefix}",
        "THEME": f"{newtheme}"
    }

    j = json.dumps(data)
    with open("config.json", "w") as f:
        f.write(json.dumps(data, indent=4))
        f.close()

    if newtheme == "RED":
        await ctx.send(f"```ansi\n"
        f"Theme changer\n\n"
        f"Successfully changed theme to [2;31mRED[0m restart v1 bot\n\n"
        f"[2;31m[v1 bot][0m```", delete_after=deletetimer)
        exit()
    
    if newtheme == "BLUE":
        await ctx.send("```ansi\n"
        f"Theme changer\n\n"
        f"Successfully changed theme to [2;31m[2;34mBLUE[0m[2;31m[0m restart v1 bot\n\n"
        f"[2;34m[v1 bot][0m```")
        exit()

#spam webhook command
@client.command(aliases=["webnuke"])
async def webhooknuker(ctx, amount: int, _webhook):
    await ctx.message.delete()
    webhookspam = Webhook(f"{_webhook}")
    if _theme == "BLUE":
        webhookspamsend = (f"```ini\n"
        f"Webhook nuker\n\n"
        f"This webhook just got fucked by v1 bot\n\n"
        f"[zone bot]```||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ @everyone https://discord.gg/PTv9sBTNK5")
        webhookspamprint = (f"{Fore.CYAN}[{Fore.WHITE}.webnuke{Fore.CYAN}]")
    if _theme == "RED":
        webhookspamsend = (f"```ansi\n"
        f"Webhook nuker\n\n"
        f"This webhook just got fucked by v1 bot\n\n"
        f"[2;31m[zone bot][0m```||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _ @everyone https://discord.gg/PTv9sBTNK5")
    for _i in range(amount):
        webhookspam.send(webhookspamsend)
    webhookspam.delete()
    print(webhookspamprint)

def get_random_user_agent():
        userAgents = ["Mozilla/5.0 (Windows NT 6.2;en-US) AppleWebKit/537.32.36 (KHTML, live Gecko) Chrome/56.0.3075.83 Safari/537.32", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 8.0; WOW64) AppleWebKit/536.24 (KHTML, like Gecko) Chrome/32.0.2019.89 Safari/536.24", "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.41 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2599.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.139 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.57 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/67.0.3387.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.0.9757 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3", "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/27.0.1453.0 Safari/537.35", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3359.181 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3057.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36 TC2", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3058.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3258.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2531.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2264.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2714.0 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Ubuntu; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1864.6 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Avast/70.0.917.102", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1615.0 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.14", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/6.0 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3608.0 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3251.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/54.2.133 Chrome/48.2.2564.133 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.61 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.45 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.104 Safari/537.36", "24.0.1284.0.0 (Windows NT 5.1) AppleWebKit/534.0 (KHTML, like Gecko) Chrome/24.0.1284.0.3.742.3 Safari/534.3", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko; Google Web Preview) Chrome/27.0.1453 Safari/537.36,gzip(gfe)", "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.29 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.45", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.150 Safari/537.36", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.102 Safari/537.36", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2419.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Chrome/36.0.1985.125 CrossBrowser/36.0.1985.138 Safari/537.36", "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1204.0 Safari/537.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16", "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.68 Safari/537.36", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2700.0 Safari/537.36#", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.114 Safari/537.36", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/538 (KHTML, like Gecko) Chrome/36 Safari/538", "Mozilla/5.0 (Windows; U; Windows 95) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.43 Safari/535.1", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (X11; Linux x86_64; 6.1) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/17.0.1410.63 Safari/537.31", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2583.0 Safari/537.36", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2151.2 Safari/537.36", "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.18 Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/536.36 (KHTML, like Gecko) Chrome/67.2.3.4 Safari/536.36", "Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.69 Safari/537.36", "Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.81 Safari/537.36", "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Safari/537.36 EdgA/41.0.0.1662", "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.1"]
        userAgent = random.choice(userAgents)
        return userAgent

#massping command
@client.command(aliases=["massmention", "massping", "rank"])
async def mm(ctx, amount:int=1, delay:int=0):
        await ctx.message.delete()
        bot = discum.Client(token=_token, log=False, user_agent=get_random_user_agent())

        def close_after_fetching(resp, guild_id):
            if bot.gateway.finishedMemberFetching(guild_id):
                members = bot.gateway.session.guild(guild_id).members
                bot.gateway.removeCommand({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.close()
                print(f"{Fore.CYAN}[{Fore.WHITE}MASS MENTION: {Fore.WHITE}Fetched a total of {Fore.CYAN}{len(members)} {Fore.WHITE}members.{Fore.CYAN}]")
                return members

        def get_members(guild_id, channel_id):
            print(f"{Fore.CYAN}[{Fore.WHITE}MASS MENTION: {Fore.WHITE}Fetching members...{Fore.CYAN}]")
            bot.gateway.fetchMembers(guild_id, channel_id, keep="all", wait=0)
            bot.gateway.command({'function': close_after_fetching, 'params': {'guild_id': guild_id}})
            bot.gateway.run()
            bot.gateway.resetSession()
            return bot.gateway.session.guild(guild_id).members

        members = get_members(str(ctx.guild.id), str(ctx.channel.id))
        messages = []
        message = ""

        for member in members:
            if len(message) < 1950:
                message += f"<@{member}> "
            else:
                messages.append(message)
                message = ""

        messages.append(message)

        for _ in range(amount):
            for message in messages:
                try:
                    await ctx.send(f"```ansi\n[2;31m🚨 🚨 🚨 RAIDED WITH V1 BOT 🚨 🚨 🚨[0m```||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| _ _ _ _ _ _" f"{message}")
                    await asyncio.sleep(delay)
                except:
                    pass
        
        input(f"\n{Fore.CYAN}[{Fore.WHITE}Press ENTER to continue...{Fore.CYAN}]")
        exit()

#cls command
@client.command(aliases=["clearscreen", "clear"])
async def cls(ctx):
    await ctx.message.delete()
    clear()
    
    await ctx.send(clssend, delete_after=deletetimer)
    print(clsprint)

client.run(_token, bot=False)
