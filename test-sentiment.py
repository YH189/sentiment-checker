from sentiment import SentimentChecker

checker = SentimentChecker()

def test_positive():
    assert checker.label("I love this movie")[0] == "positive"

def test_negative():
    assert checker.label("this food is terrible")[0] == "negative"

def test_negation_flips():
    assert checker.label("not good")[0] == "negative"

def test_punctuation_ignored():
    assert checker.label("Great!!!")[0] == "positive"

def test_neutral():
    assert checker.label("it is a bus")[0] == "neutral"