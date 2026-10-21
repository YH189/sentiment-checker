import string

class SentimentChecker:
    def __init__(self):
        self.word_scores = {
            "love": 2, "great": 2, "amazing": 2, "excellent": 2,
            "good": 1, "nice": 1, "happy": 1, "fun": 1, "like": 1,
            "bad": -1, "boring": -1, "sad": -1, "poor": -1, "dislike": -1,
            "hate": -2, "terrible": -2, "awful": -2, "worst": -2,
        }
        self.negations = {"not", "no", "never", "dont", "isnt"}

def clean(self, sentence):
    no_punct = sentence.translate(str.maketrans("","",string.punctuation))
    return no_punct.lower().split()