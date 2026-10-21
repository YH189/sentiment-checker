from sentiment import SentimentChecker, score

checker = SentimentChecker()

while True:
    sentence = input('Enter a sentece (or  quit):')
    if sentence.lower() == 'quit':
        break
    label, score = checker.label(sentence)
    print(f"{label}(score: {score})")
    