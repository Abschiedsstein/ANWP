import numpy as np
import random
from controller import Controller

class Server (object):
    def __init__(self, controller):
        if issubclass(controller.__class__, Controller):
            self.controller = controller

    def install(self,card):
        pass


class Remote (Server):
    def __init__(self, *args):
        super(Remote, self).__init__(*args)

class RnD (Server):
    def __init__(self, *args):
        super(RnD, self).__init__(*args)
        self.cardStack = []
    def draw(self, n=1):
        return [self.cardStack.pop() for _ in range(n)]
    def reveal(pos=0):
        return self.cardStack[pos]
    def shuffle(self):
        random.shuffle(self.cardStack)
    def addCard(self, card):
        self.cardStack.append(card)

class HQ (Server):
    def __init__(self, *args):
        super(HQ, self).__init__(*args)
        self.hand = []
        self.maximumHandSize = 5
    def add(self,card):
        self.hand.append(card)
    def remove(self,card):
        self.hand.remove(card)
    def reveal(self,position):
        return self.hand[position]
