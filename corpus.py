import os

class Corpus:
    def __init__(self, folderpath):
        self.folderpath = folderpath
        self.filesList = os.listdir(path=self.folderpath)
        self.initExtra()

    def initExtra(self):
        pass

    def email(self):
        for email in self.filesList:
            if email[0] != '!':
                with open(self.folderpath + "/" + email, encoding='utf-8') as file:
                    yield email, file.read()
                    


if __name__ == "__main__":
    

    '''
    mailCount = 0
    for email in a:
        print(email[0])
        print(email[1])
        mailCount += 1
    print(mailCount)'''
