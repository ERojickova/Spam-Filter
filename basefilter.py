from corpus import Corpus

class BaseFilter:
    def __init__(self, trainFolderPath, testFolderPath):
        trainCorpus = Corpus(trainFolderPath)
        corpus = Corpus(testFolderPath)

    def train(self):
        pass

    def test(self):
        with open(self.testFolderPath + "/!prediction.txt", "w", encoding='utf-8') as file:
            for mail in self.corpus.email():
                prediction = self.predict(mail)
                file.write(f"{mail[0]} {prediction}\n")

    def predict(self, mail):
        pass
