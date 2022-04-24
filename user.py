

class User():
    def __init__(self, discordid, name):
        self.discordid = discordid
        self.name = name
        self.coca = 0
        self.erva = 0
        self.opio = 0
        self.meta = 0

    def getDiscordid(self):
        return self.discordid

    def getName(self):
        return self.name

    def addCoca(self, amount):
        self.coca += amount
    
    def addErva(self, amount):
        self.erva += amount

    def addOpio(self, amount):
        self.opio += amount

    def addMeta(self, amount):
        self.meta += amount

    def getMeta(self):
        return self.meta
    
    def getCoca(self):
        return self.coca
    
    def getErva(self):
        return self.erva

    def getOpio(self):
        return self.opio

    def setCoca(self, amount):
        self.coca = amount

    def setErva(self, amount):
        self.erva = amount

    def setOpio(self, amount):
        self.opio = amount

    def setMeta(self, amount):
        self.meta = amount
        
