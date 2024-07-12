from nltk.grammar import CFG
from nltk.parse.chart import TopDownChartParser, BottomUpChartParser

grammar = CFG.fromstring('''
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw"
    NP -> "I" |"rishabh" | "achal" | Det N | Det N PP
    Det -> "the" | "a" | "an"
    N -> "man" | "telescope"
    P -> "with"
''')

def parse_sentence(sentence):
    tokens = sentence.split()
    # Top Down Parsing
    top_down_parser = TopDownChartParser(grammar)
    print("Top Down parsing results: ")
    top_down_results = list(top_down_parser.parse(tokens))
    if top_down_results:
        for tree in top_down_results:
            print(tree)
            tree.draw()
    else:
        print("No parse tree found using top-down parsing")

    # Bottom Up Parsing
    bottom_up_parser = BottomUpChartParser(grammar)
    print("Bottom Up parsing results: ")
    bottom_up_results = list(bottom_up_parser.parse(tokens))
    if bottom_up_results:
        for tree in bottom_up_results:
            print(tree)
            tree.draw()
    else:
        print("No parse tree found using bottom-up parsing")

user_input = input("Enter a sentence to parse: ")
parse_sentence(user_input)