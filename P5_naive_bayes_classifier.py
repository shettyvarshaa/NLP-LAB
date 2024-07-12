from collections import defaultdict
import numpy as np

documents = [
    ("fun, couple, love, love", "comedy"),
    ("fast, furious, shoot", "action"),
    ("couple, fly, fast, fun, fun", "comedy"),
    ("furious, shoot, shoot, fun", "action"),
    ("fly, fast, shoot, love", "action")
]

new_doc = "fast, couple, shoot, fly"

def preprocess(doc):
    return doc.lower().split(", ")

def likelihood(word, label):
    return (word_counts[label][word] + 1) / (total_words[label] + vocab_size)

def compute_posterior(new_doc, label):
    words = preprocess(new_doc)
    posterior = np.log(priors[label])
    for word in words:
        posterior += np.log(likelihood(word, label))
    return posterior

word_counts = {'comedy': defaultdict(int), 'action': defaultdict(int)}
class_counts = {'comedy': 0, 'action': 0}
vocab = set()

for doc, label in documents:
    words = preprocess(doc)
    class_counts[label] += 1
    for word in words:
        word_counts[label][word] += 1
        vocab.add(word)

total_docs = sum(class_counts.values())
priors = {label: count / total_docs for label, count in class_counts.items()}
total_words = {label: sum(word_counts[label].values()) for label in word_counts}
vocab_size = len(vocab)

posteriors = {label: compute_posterior(new_doc, label) for label in priors}
predicted_class = max(posteriors, key=posteriors.get)

print(f"The most likely class for the new document - 'fast, couple, shoot, fly' is: {predicted_class}")
