#include <iostream>
// #include <fstream>
#include <sstream>
#include "WordCounts.h"

using namespace std;

WordCounts::WordCounts(){
  numUnique = 0;
  for (int i = 0; i < 10000; i++){
    words[i] = "";
    counts[i] = 0;
  }
}

int WordCounts::getCount(string word) {
    int count = 0;
    for(int i = 0; i < numUnique; i++) {
        if(words[i] == word) {
            count =  counts[i];
        }
    }
    return count;
}

void WordCounts::resetCounts() {
    for(int i = 0; i < numUnique; i++) {
        counts[i] = 0;
    }
    numUnique = 0;
    wordcount = 0;
}

bool WordCounts::isUnique(string word) {
    int idx = 0;
    bool isFound = true;
    while(idx < numUnique && isFound) {
        if(words[idx] == word) {
            isFound = false;
            counts[idx]++;
        }
        idx++;
    }
    return isFound;
}

void WordCounts::addWord(string word) {
    words[numUnique] = word;
    counts[numUnique] = 1;
    numUnique++;
}

char WordCounts::toLower(char l) {
    if(l <= 'Z' && l >= 'A') {
        return l - ('Z' - 'z');
    }
    return l;
}

void WordCounts::sort() {
    bool sorted = false;
    while(!sorted) {
        sorted = true;
        for(int i = 0; i < numUnique - 1; i++) {
            if (counts[i] < counts[i+1]) {
                // swap names
                string tempWord = words[i];
                words[i] = words[i+1];
                words[i+1] = tempWord;

                // swap scores
                int tempCount = counts[i];
                counts[i] = counts[i+1];
                counts[i+1] = tempCount;

                sorted = false;
            }
        }
    }

}
int WordCounts::mostCommon(string commonWords[], int wordCount[], int n){
    sort();

    int c = 0;
    for(int idx = 0; idx < n; idx++) {
        if(words[idx] == "") break;
        commonWords[idx] = words[idx];
        wordCount[idx] = counts[idx];
        c++;
    }

    return c;
}

string WordCounts::extractWord(string word) {
    string result = "";
    for(int i = 0; i < word.length(); i++) {
        if(word[i] != ',' && word[i] != '!' && word[i] != '.' && word[i] != '?') {
            result += toLower(word[i]);
        }
    }
    return result;
}

void WordCounts::countWords(string sentence) {
    string word;
    stringstream ss(sentence);

    while (getline(ss, word, ' ')) {
        wordcount++;
        word = extractWord(word);
        if(isUnique(word) == true) {
            // add words to list
            addWord(word);
        }
    }
}
