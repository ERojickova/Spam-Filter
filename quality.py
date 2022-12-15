import utils
import confmat


def quality_score(tp, tn, fp, fn):
    return (tp + tn) / (tp + tn + 10*fp + fn)

def compute_quality_for_corpus(corpus_dir):
    truthPath = corpus_dir + "/!truth.txt"
    truthDict = utils.read_classification_from_file(truthPath)
    predPath = corpus_dir + "/!prediction.txt"
    predDict = utils.read_classification_from_file(predPath)
    cm = confmat.BinaryConfusionMatrix("SPAM", "OK")
    cm.compute_from_dicts(truthDict, predDict)
    return quality_score(cm.tp, cm.tn, cm.fp, cm.fn)


if __name__ == "__main__":
    print(compute_quality_for_corpus("./1"))