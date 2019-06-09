import discord
import config

class Client(discord.Client):
  async def on_ready(self):
    print("I am logged in bois")

  async def on_message(self, message):
    print('Message from {0.author}: {0.content}.'.format(message))

botClient = Client()
botClient.run(config.BOT_CONFIG['token'])