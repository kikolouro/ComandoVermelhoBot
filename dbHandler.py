from tkinter.filedialog import LoadFileDialog
from user import User
import json


class dbHandler():
    def __init__(self, file):
        self.file = file
        self.users = []
        self.loadFileData()

    def loadFileData(self):
        data = self.getFileData()
        for discordid, name in data.items():
            self.users.append(User(discordid, name['name']))
            self.users[-1].setCoca(name['coca'])
            self.users[-1].setErva(name['erva'])
            self.users[-1].setOpio(name['opio'])
            self.users[-1].setMeta(name['meta'])


    def removeUser(self, discordid):
        data = self.getFileData()
        if discordid in data:
            del data[discordid]
            with open(self.file, 'w') as f:
                json.dump(data, f)
            for user in self.users:
                if user.discordid == discordid:
                    self.users.remove(user)
                    return True
        return False

    def getUsers(self):
        return self.users

    def getFileData(self):
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
            return data
        except:
            pass
        with open(self.file, 'w') as f:
            json.dump({}, f)
        return {}

    def addFileData(self, discordid, name):
        data = self.getFileData()
        data[discordid] = {"name": name, "coca": 0,
                           "erva": 0, "opio": 0, "meta": 0}
        with open(self.file, 'w') as f:
            json.dump(data, f)

    def addUser(self, discordid, name):
        if not self.checkIfUserExists(discordid):
            self.addFileData(discordid, name)
            self.users.append(User(discordid, name))
            return True
        return False

    def checkIfUserExists(self, discordid):
        data = self.getFileData()
        for user in self.users:
            if user.discordid == discordid:
                return True
        return False

    def addDrugtoFile(self, discordid, drug, amount):
        data = self.getFileData()
        if str(discordid) in data:
            if drug == "coca":
                data[str(discordid)]["coca"] += amount
            elif drug == "erva":
                data[str(discordid)]["erva"] += amount
            elif drug == "opio":
                data[str(discordid)]["opio"] += amount
            elif drug == "meta":
                data[str(discordid)]["meta"] += amount
            with open(self.file, 'w') as f:
                json.dump(data, f)
            return True
        return False

    def addDrug(self, discordid, drug, amount):
        if drug == "coca":
            if self.addCoca(discordid, amount):
                return self.addDrugtoFile(discordid, drug, amount)
        elif drug == "erva":
            if self.addErva(discordid, amount):
                return self.addDrugtoFile(discordid, drug, amount)
        elif drug == "opio":
            if self.addOpio(discordid, amount):
                return self.addDrugtoFile(discordid, drug, amount)
        elif drug == "meta":
            if self.addMeta(discordid, amount):
                return self.addDrugtoFile(discordid, drug, amount)
        return False

    def checkUser(self, discordid):
        for user in self.users:
            if user.discordid == discordid:
                return user
        return False

    def addCoca(self, discordid, amount):

        for user in self.users:
            if user.getDiscordid() == str(discordid):
                user.addCoca(amount)

                return True
        return False

    def addOpio(self, discordid, amount):
        for user in self.users:
            if user.discordid == discordid:
                user.addOpio(amount)
                return True
        return False

    def addErva(self, discordid, amount):
        for user in self.users:
            if user.discordid == discordid:
                user.addErva(amount)
                return True
        return False

    def addMeta(self, discordid, amount):
        for user in self.users:
            if user.discordid == discordid:
                user.addMeta(amount)
                return True
        return False

    def getAllUserDrugs(self):
        data = {}
        for user in self.getUsers():
            data[user.getDiscordid()] = {"name": user.getName(), "coca": user.getCoca(),
                                    "erva": user.getErva(), "opio": user.getOpio(), "meta": user.getMeta()}
        return data
