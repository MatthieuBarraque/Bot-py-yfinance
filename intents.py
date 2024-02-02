from discord import Intents

intents = Intents.default()
intents.all()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True
intents.reactions = True
intents.presences = True
intents.bans = True
intents.emojis = True
intents.integrations = True
intents.webhooks = True
intents.invites = True
intents.voice_states = True
intents.typing = True
