import discord
import os
import requests
import json
import random
from replit import db

sad_words=["sad","depressed", "regret","hollow inside"
,"miserable","fuck me","save me from my self",
"broken","sorry", "lonely","empty"]

starter_encourage=["It's okay, sometimes i feel it too","There is always light at the end of the tunnel",
"Hang in there","Life is an expierence , aint it..",
"You will be alright",
"We all don't have to be great, just be urself..","Peace .."]

client =discord.Client()

def update (msg):
  if "encourage" in db.keys():
    encourage = db["encourage"]
    if msg not in encourage:
      #print("came in ")
      encourage.append(msg)
      db["encourage"]= encourage
  else:
    #encourage=[]
    db["encourage"]=[msg]

def delete (msg):
  if "encourage" in db.keys():
    encourage = db["encourage"]
    if msg in encourage:
      encourage.remove(msg)
      db["encourage"]=encourage
  else:
    pass        

  


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
  if "encourage" in db.keys():
    options = starter_encourage + db["encourage"]
  else:
    options =   starter_encourage
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))

  #update repotoire
  if (msg.startswith("$new")):
    encourage = msg.split("$new ",1)[1]
    update(encourage)
    await message.channel.send("Thanxx, i will remeber it !")
  #delete repotoire
  if (msg.startswith("$del")):
    encourage = msg.split("$del ",1)[1]
    delete(encourage)
    await message.channel.send("It's hard to forget things,but o.k.")  

client.run(os.getenv('TOKEN'))
