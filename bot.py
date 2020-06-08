#A partir de aquí escribe tu código
import discord
class MyClient(discord.Client):
	async def on_ready(self):
	    print('¡Logeado en {0}!'.format(self.user))
						     
	async def on_message(self, message):
		print('Mensaje de {0.author}: {0.content}'.format(message))
						     
client = MyClient()
client.run('NzE5NTk5OTY5MDYwOTEzMjg0.Xt54cw.FwjMANogHxYolsQsli7WC3bNiBc')