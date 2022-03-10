from albert import *
import re
from os import path
import json

__title__ = "Batches"
__version__ = "0.4.0"
__triggers__ = "ba "
__authors__ = "pkboom"

icon = "{}/icon.png".format(path.dirname(__file__))

dir = path.dirname(path.abspath(__file__))

batches = path.join(dir, 'batches.json')

file = open(batches)
batches = json.load(file)
file.close()

def handleQuery(query):
    if not query.isTriggered or not query.isValid:
        return
    
    print(batches)
    
    items = []

    for batch in batches:
        for key in batch.keys():
            items.append(Item(
                id=key,
                icon=icon,
                text=key,
                actions=[TermAction(
                    text='Start work', 
                    script=' && '.join(batch[key]), 
                )],
            ))

    return items
