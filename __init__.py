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
    
    regexp = query.string.strip().replace(" ", ".*")

    items = []

    for batch in batches:
        for key in batch.keys():
            if re.search(regexp, key): 
                items.append(Item(
                    id=key,
                    icon=icon,
                    text=key,
                    actions=[TermAction(
                        text='Run a batch', 
                        script=' && '.join(batch[key]), 
                    )],
                ))

    return items
