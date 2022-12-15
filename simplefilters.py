import corpus
import random
import quality
from basefilter import BaseFilter

from statistics import mean


class NaiveFilter(BaseFilter):
    def predict(self, mail):
        return "OK"

class ParanoidFilter(BaseFilter):
    def predict(self, mail):
        return "SPAM"

class RandomFilter(BaseFilter):
    def predict(self, mail):
        return random.choice(["OK", "SPAM"])


if __name__ == "__main__":
    naiveF = NaiveFilter()
    randomF = RandomFilter()
    ans = []
    for x in range(1000):
        randomF.test("./1")
        ans.append(quality.compute_quality_for_corpus("./1"))
        print(str(x) + ": DONE")

        
    print("Average: " + str(mean(ans)))
    print("Maximum: " + str(max(ans)))
    print("Minimum: " + str(min(ans)))