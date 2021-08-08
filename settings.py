import os
from os.path import join, dirname

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot_token = os.getenv('BOT_TOKEN')

footer_icon = "https://image.brandonly.me/avgl.png"
prefix = "a!"

archive_id = 863920071968555048
staff_id = 859963632879534090

copypasta = "Welcome to the playoffs quarterfinals! " \
            "You may reschedule the default time but not the date. " \
            "The match will be a Best-Of-3 unless a larger best-of is agreed" \
            " upon." \
            "\n\n" \
            "Please send a screenshot after your match so that it can be " \
            "updated on the brackets." \
            "\n\n" \
            "Message a <@&859963632879534090> if you have any questions!"
