import numpy as np


class RnD : Server{
        draw()
        reveal(n)
        shuffle()
        pick()
        }

class Archive : Server{
        add(face)
        reveal(n)
        pick()
        }

class Hand{
    add()
    remove()
    reveal()
    }

class Server {
        create()
        install()
        }

class HQ : Server{
        }

class Remote : Server {
        }

class Rule : EventReader{
        target,
        checkConditions(),
        effect()
        neffect()
        }

class Blocker :Rule {
        }

class Player {
        turn,
        clicks,
        credits,
        }

class Event {
        registerAsEventReader()
        readersList
        }

class TimeEvent : Event {
        def init():
            super(Event,self)
        }

class PlayerActionEvent : Event {
        }

class EventReader {
        def triggerFunction ()
        Event.registerAsEventReader(triggerFunction)
        }

class EventHandler {
        }


def subjectToRules (func):
    def rulesChecker(*args, **kwargs):
        relevantRules = [rule in rules if rule.target is func]
        for rule in relevantRules:
            if rule.checkConditions(*args,**kwargs):
                if ruel is Blocker:
                    return
                rule.effect()
            else: 
                rule.neffect()
        return func(*args,**kwargs)
    return rulesChecker

class Test :
    def __init__(self):


