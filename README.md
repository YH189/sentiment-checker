# Sentiment Checker

A command-line tool that labels English sentences as **positive**, **negative**, or **neutral** using a rule-based scoring system.

## Features

- Weighted word scores (for example, `love` = +2, `good` = +1, `hate` = -2)
- Negation handling: `not good` is scored as negative
- Punctuation and letter case are ignored
- Interactive command-line loop
- Unit tests with pytest

## Requirements

- Python 3.9 or newer
- pytest (for running tests)

## Installation

```bash
git clone https://github.com/<your-username>/sentiment-checker.git
cd sentiment-checker
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python3 main.py
```

Example session:

```
Enter a sentence (or 'quit'): I love this movie
positive (score: 2)

Enter a sentence (or 'quit'): this food is terrible
negative (score: -2)

Enter a sentence (or 'quit'): it is a bus
neutral (score: 0)

Enter a sentence (or 'quit'): quit
```

## How It Works

1. `clean()` removes punctuation, lowercases the sentence, and splits it into words.
2. `score()` adds up the value of each word found in the word dictionary. If the previous word is a negation (such as `not`), the value is flipped.
3. `label()` returns `positive`, `negative`, or `neutral` with the total score.

## Running Tests

```bash
pytest -v
```

## Project Structure

| File | Purpose |
|------|---------|
| `sentiment.py` | `SentimentChecker` class with scoring logic |
| `main.py` | Command-line interface |
| `test_sentiment.py` | Unit tests |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Files excluded from Git |

## Limitations

- Negation only checks the single word before a sentiment word, so `not very good` is still scored as positive.
- Sarcasm and context are not understood.
- The word list is small and fixed in the code.
