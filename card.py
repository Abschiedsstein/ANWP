"""
This class shall model cards that are used in the game.
"""

from enum import Enum, unique

class Card(object):
    maxId = 0 
    @unique
    class Type(Enum):
        asset = 1
        ice = 2
        agenda = 3
        operation = 4
        identity = 5

    def __init__(self,cardtype):
        self.id = Card.maxId
        if not issubclass(cardtype.__class__,Card.Type):
            raise ValueError("cardtype has to be of class Type")
        self.type = cardtype
        Card.maxId += 1
