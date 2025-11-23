# summarizer.py -- simple frequency-based summarizer
import re
from collections import Counter

def sentences(text):
    return [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]

def words(text):
    return re.findall(r'\w+', text.lower())

def summarize(text, n_sentences=2):
    sents = sentences(text)
    if len(sents) <= n_sentences:
        return sents
    w = words(text)
    freq = Counter(w)
    scores = []
    for s in sents:
        score = sum(freq[w] for w in words(s))
        scores.append((score, s))
    scores.sort(reverse=True)
    top = [s for _, s in scores[:n_sentences]]
    top_sorted = [s for s in sents if s in top]
    return top_sorted

if __name__ == "__main__":
    sample = ("Natural language processing is a subfield of AI. "
              "It includes tasks like summarization, translation, and sentiment analysis. "
              "This is a tiny summarizer for demonstration.")
    print("\n".join(summarize(sample, 2)))
