
"""
The Controller keeps track of the game evolution and of global settings like the rules.
"""
class Controller (object):
    def __init__(self):
        rules = []
       # rules.append(


def subjectToRules (func):
    def rulesChecker(*args, **kwargs):
        relevantRules = [rule in self.controlle.rules if rule.target == func]
        for rule in relevantRules:
            if rule.checkConditions(*args,**kwargs):
                if ruel is Blocker:
                    return
                rule.effect()
            else: 
                rule.neffect()
        return func(*args,**kwargs)
    return rulesChecker

class Rule : #EventReader{
   def __init__(self):
        target = None
   def checkConditions():
       pass
   def effect():
       pass
   def neffect():
       pass

class Blocker (Rule):
    pass

class DoNotInstallOperation(Blocker):


