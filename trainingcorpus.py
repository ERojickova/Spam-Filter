import utils
from corpus import Corpus
from utils import read_classification_from_file

class TrainingCorpus(Corpus):
    def initExtra(self):
        self.truthDict = read_classification_from_file(self.folderpath + "/!truth.txt")

    def GetClass(self, emailName):
       return self.truthDict[emailName]

    def IsSpam(self, emailName):
        if self.truthDict[emailName] == "SPAM":
            return True
        return False

    def IsHam(self, emailName):
        if self.truthDict[emailName] == "OK":
            return True
        return False

    def Spams(self):
        for emailName in self.filesList:
            if emailName[0] != '!':
                with open(self.folderpath + "/" + emailName, encoding='utf-8') as file:
                    if self.truthDict[emailName] == "SPAM":
                        yield emailName, file.read()
    
    def Hams(self):
        for emailName in self.filesList:
            if emailName[0] != '!':
                with open(self.folderpath + "/" + emailName, encoding='utf-8') as file:
                    if self.truthDict[emailName] == "OK":
                        yield emailName, file.read()




if __name__ == "__main__":
    c = TrainingCorpus("./1")
    a = c.Spams()
    mailCount = 0
    for email in a:
        utils.PrintHeader("=",30,email[0])
        print()
        print(email[1])
        mailCount += 1
    print(mailCount)

