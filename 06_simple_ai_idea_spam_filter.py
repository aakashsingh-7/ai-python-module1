"""Program 6: A tiny rule-based 'spam filter'.

This is NOT machine learning - the rules are written by hand. In real ML,
the computer would learn these patterns from thousands of labelled emails.
It's a nice way to see the difference between rules and learning.
"""

SPAM_WORDS = ["free", "winner", "prize", "urgent", "click here", "lottery"]


def spam_score(message):
    text = message.lower()
    return sum(1 for word in SPAM_WORDS if word in text)


def classify(message):
    return "SPAM" if spam_score(message) >= 2 else "NOT SPAM"


messages = [
    "Congratulations winner! Click here to claim your free prize",
    "Hi, are we still meeting for the project discussion tomorrow?",
    "URGENT: you won the lottery, click here now",
]

for msg in messages:
    print(f"[{classify(msg)}] {msg}")
