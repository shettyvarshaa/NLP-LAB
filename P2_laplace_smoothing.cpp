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

double laplaceSmoothing(const vector<string>& corpus, const string& sentence) {
    map<string, int> unigram;
    map<pair<string, string>, int> bigram;

    for (const auto& s : corpus) {
        vector<string> words = tokenize(s);
        for (size_t i = 0; i < words.size(); ++i) {
            unigram[words[i]]++;
            if (i > 0) bigram[{words[i-1], words[i]}]++;
        }
    }

    int vocab_size = unigram.size();
    vector<string> test_words = tokenize(sentence);
    double probability = 1.0;

    cout << "\nBigram Probabilities:" << endl;
    for (size_t i = 0; i < test_words.size() - 1; ++i) {
        string w1 = test_words[i], w2 = test_words[i + 1];
        int bigram_count = bigram[{w1, w2}], unigram_count = unigram[w1];
        double bigram_prob = static_cast<double>(bigram_count + 1) / (unigram_count + vocab_size);
        probability *= bigram_prob;
        cout << "(" << w1 << ", " << w2 << "): " << bigram_prob << endl;
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
    double probability = laplaceSmoothing(corpus, sentence);
    cout << "\nFinal Probability of the sentence \"" << sentence << "\": " << probability << endl;

    return 0;
}