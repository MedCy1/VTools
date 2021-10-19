from discord_webhooks import DiscordWebhooks

# Webhook URL for your Discord channel.
WEBHOOK_URL = 'https://discord.com/api/webhooks/815631613005922355/cWdYXqjRSztZ_1LafIM7vxsyVNguUORII_8dYS5jZMsBSwSHadu8oZBZT1M0lzmrg2IJ'

webhook = DiscordWebhooks(WEBHOOK_URL)

webhook.set_content(content='The best cat ever is...', title='Montezuma!', description='Seriously!', \
  url='http://github.com/JamesIves', color=0xF58CBA, timestamp='2018-11-09T04:10:42.039Z')

# Attaches an image
webhook.set_image(url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

# Attaches a thumbnail
webhook.set_thumbnail(url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

# Attaches an author
webhook.set_author(name='James Ives', url='https://jamesiv.es', icon_url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

# Attaches a footer
webhook.set_footer(text='Footer', icon_url='https://avatars1.githubusercontent.com/u/10888441?s=460&v=4')

# Appends a field
webhook.add_field(name='Field', value='Value!')

webhook.send()