import nltk
from IPython.display import display
# from nltk.parse.chart import TopDownChartParser, BottomUpChartParser
grammar = nltk.CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "Janice"  | "Bob" | Det N | Det N PP
    Det -> "a" | "an" | "the" | "my"|"his"
    N -> "dog" | "cat" | "telescope" | "park"| "Moon"| "terrace"
    P -> "in" | "on" | "by" | "with"| "from"
""")

def parse_sentence(sentence):
    tokens = sentence.split()
    print("Top Down parsing results: ")
    rd_parser = nltk.TopDownChartParser(grammar)
    for tree in rd_parser.parse(tokens):
        tree.pretty_print()
        tree.draw()
    print("Bottom Up parsing results: ")
    sr_parser = nltk.BottomUpChartParser(grammar)
    for tree in sr_parser.parse(tokens):
        tree.pretty_print()
        tree.draw()

user_input = input("Enter a sentence to parse: ")
parse_sentence(user_input)