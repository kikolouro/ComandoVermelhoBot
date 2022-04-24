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
            self.users.append(User(discordid, name))

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
        data[discordid] = name
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
