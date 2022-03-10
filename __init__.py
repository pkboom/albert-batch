from albert import *
import re
from os import path
import json

__title__ = "Start"
__version__ = "0.4.0"
__triggers__ = "start "
__authors__ = "pkboom"

icon = "{}/icon.png".format(path.dirname(__file__))

dir = path.dirname(path.abspath(__file__))

commands = path.join(dir, 'commands.json')

file = open(commands)
commands = json.load(file)
file.close()



def handleQuery(query):
    if not query.isTriggered or not query.isValid:
        return
    
    items = []

    items.append(Item(
        id='start',
        icon=icon,
        text='start',
        actions=[TermAction(
            text='Start work', 
            script=' && '.join(commands), 
        )],
    ))

    return items
