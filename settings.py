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

copypasta = "Hi, you both are captains for your team. Please use this " \
            "chat for this week to set up a time to play if you are not " \
            "planning on playing the default time. You have until Saturday @ " \
            "1 pm PST to reschedule the match (if needed). " \
            "Remember, both teams must agree to a time if a reschedule is to" \
            " happen" \
            "\n\n" \
            "Reminder: It's important to record the round win losses in game" \
            " while score reporting. (ie: if your team goes 13 - 6 in game, " \
            "report that under the kill section) " \
            "\n\n" \
            "Message a <@&859963632879534090> if you have any questions!"
