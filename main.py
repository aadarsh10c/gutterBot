import discord
import os
import requests
import json
import random

sad_words=["sad","depressed", "regret","hollow inside"
,"miserable","fuck me","save me from my self",
"broken","sorry", "lonely","empty"]

starter_encourage=["It's okay, sometimes i feel it too","There is always light at the end of the tunnel",
"Hang in there","Life is an expierence , aint it..",
"You will be alright",
"We all don't have to be great, just be urself..","Peace .."]

client =discord.Client()

def get_quotes():
  response = requests.get("https://zenquotes.io/api/random")
  data = json.loads(response.text)
  quote = data[0]['q'] + " -"+ data[0]['a']
  return quote

@client.event
async def on_ready():
  print("We have logged in as {0.user}"
  .format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  msg=message.content  
  if msg.startswith("$hey"):
    await message.channel.send("Hello!!")

  if (msg.startswith("$inspire") or msg.startswith("$motivate")):
    quote = get_quotes()
    await message.channel.send(quote)
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encourage))


client.run(os.getenv('TOKEN'))
