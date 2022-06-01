import discord
import os
import json
import requests
import random

client = discord.Client()

global search_term_public 
global url
search_term_public = "your term here"

def tenor():
    global url
    # set the tenor apikey 
    apikey = (os.getenv("TENORAPIKEY"))

    # our test search
    search_term = search_term_public

    # get the GIFs for the search term
    r = requests.get("https://g.tenor.com/v1/search?q=%s&key=%s&contentfilter=high" % (search_term, apikey))

    if r.status_code == 200:
            # load the GIFs using the urls for the smaller GIF sizes
            top_8gifs = json.loads(r.content)
            g = len(top_8gifs['results'])
            i = random.randint(0,g)
            if(i == g):
                    i = g-1
            h = str(g)
            f = str(i)
            url = top_8gifs['results'][i]['media'][0]['gif']['url']
            print("The number picked is " + f +" out of " + h + ". Search Term : " + search_term + ". Url : " +url)
    else:
            top_8gifs = None
    return url

@client.event
async def on_ready():
        await client.change_presence(status = discord.Status.online, activity = discord.Game('A Game!'))
        print("Bot has successfully logged in as {0.user}".format(client))

@client.event
async def on_message(message):
        global search_term_public
        if message.author == client:
                return
        if message.content.startswith("!yourtermhere"):
                # put the search term into the public variable. split the content with space and the second or more than second word should be in a variable
                tokens = message.content.split(' ')
                if tokens.__contains__(""):
                        tokens.remove("!yourtermhere")
                        tokens.remove("")
                elif tokens.__contains__("#"):
                        token = token.replace("#", "%23")
                else :
                        tokens.remove("!yourtermhere")     
                search_term_public =  ("".join(tokens))
                if search_term_public == "":
                        search_term_public = "your term here"     
                url = tenor()
                await message.channel.send(url)


# YOUR DISCORD BOT'S TOKEN
client.run('TOKEN')
