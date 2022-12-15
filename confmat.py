
class BinaryConfusionMatrix:

    def __init__(self, pos_tag, neg_tag):
        self.pos_tag = pos_tag
        self.neg_tag = neg_tag
        self.tp = 0
        self.fp = 0
        self.tn = 0
        self.fn = 0

    def as_dict(self):
        return {"tp":self.tp, "fp":self.fp, "tn":self.tn, "fn":self.fn}

    def update(self, truth, pred):
        if not pred in (self.pos_tag, self.neg_tag) or not truth in (self.pos_tag, self.neg_tag):
            exit("ValueError")
        if pred == self.pos_tag and truth == self.pos_tag:
            self.tp += 1
        if pred == self.pos_tag and truth == self.neg_tag:
            self.fp += 1
        if pred == self.neg_tag and truth == self.neg_tag:
            self.tn += 1
        if pred == self.neg_tag and truth == self.pos_tag:
            self.fn += 1


    def compute_from_dicts(self, truth_dict, pred_dict):
        for mailName in pred_dict.keys():
            self.update(truth_dict[mailName], pred_dict[mailName])

if __name__ == "__main__":
    a = BinaryConfusionMatrix("SPAM", "OK")
    a.update("OK", "OK")
    print(a.as_dict())
