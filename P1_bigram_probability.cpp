#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
using namespace std;

vector<string> tokenize(const string& sentence) {
    vector<string> tokens;
    stringstream ss(sentence);
    string word;
    while (ss >> word) tokens.push_back(word);
    return tokens;
}

double calculateBigramProbability(const vector<string>& corpus, const string& sentence) {
    map<pair<string, string>, int> bigramCounts;
    map<string, int> wordCounts;

    for (const string& s : corpus) {
        vector<string> tokens = tokenize("<s> " + s + " </s>");
        for (size_t i = 0; i < tokens.size() - 1; ++i) {
            bigramCounts[{tokens[i], tokens[i + 1]}]++;
            wordCounts[tokens[i]]++;
        }
        wordCounts[tokens.back()]++;
    }

    vector<string> targetTokens = tokenize("<s> " + sentence + " </s>");
    double probability = 1.0;
    cout << "\nBigram Probabilities for the test sentence:\n";
    for (size_t i = 0; i < targetTokens.size() - 1; ++i) {
        auto bigram = make_pair(targetTokens[i], targetTokens[i + 1]);
        if (bigramCounts.find(bigram) != bigramCounts.end()) {
            double bigramProbability = static_cast<double>(bigramCounts[bigram]) / wordCounts[bigram.first];
            cout << "P(" << bigram.second << " | " << bigram.first << ") = " << bigramProbability << endl;
            probability *= bigramProbability;
        } else {
            cout << "P(" << bigram.second << " | " << bigram.first << ") = 0 (Bigram not found in corpus)" << endl;
            return 0;
        }
    }

    return probability;
}

int main() {
    vector<string> corpus = {
        "There is a big garden",
        "Children play in a garden",
        "They play inside beautiful garden"
    };

    string sentence = "They play in a big garden";
    double probability = calculateBigramProbability(corpus, sentence);
    cout << "\nFinal Probability of the sentence \"" << sentence << "\": " << probability << endl;

    return 0;
}