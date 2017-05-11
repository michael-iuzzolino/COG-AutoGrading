#include <iostream>
#include <fstream>
#include <sstream>
#include "SpellChecker.h"

using namespace std;


SpellChecker::SpellChecker() {
    language = "English";
    numValid = 0;
    numCorrected = 0;
    begin_mark = '~';
    end_mark = '~';

}

SpellChecker::SpellChecker(string lang) {
    language = lang;
    numValid = 0;
    numCorrected = 0;
    begin_mark = '~';
    end_mark = '~';

}

SpellChecker::SpellChecker(string lang, string valid_words_filename, string misspelled_filename) {
    language = lang;
    numValid = 0;
    numCorrected = 0;
    begin_mark = '~';
    end_mark = '~';

    loadValidWords(valid_words_filename);
    loadMisspelledWords(misspelled_filename);


    // validWords = new string[10000];

    // for(int idx = 0; idx < SIZE; idx++) {
    //     correctedWords[idx][0] = "";
    //     correctedWords[idx][1] = "";
    //
    // }

}

// int SpellChecker::getNValidWords() {
//     return numValid;
// }
//
// int SpellChecker::getNMisspelled() {
//     return numCorrected;
// }

void SpellChecker::setBeginMarker(char begin){
    begin_mark = begin;

}

void SpellChecker::setEndMarker(char end){
    end_mark = end;

}

char SpellChecker::getBeginMarker(){
    return begin_mark;
}

char SpellChecker::getEndMarker(){
    return end_mark;
}


bool SpellChecker::loadValidWords(string filename){
    string line;
    bool isOpen = false;
    ifstream in(filename);

    if(in.is_open()) {
        isOpen = true;

        while(getline(in, line)) {
            // cout << line << endl;
            validWords[numValid] = line;
            numValid++;
            if(numValid == SIZE) {
                // cout << "SIZE exceeded" << endl;
                break;
            }
        }
    }

    return isOpen;
}

bool SpellChecker::loadMisspelledWords(string filename){
    string line;
    bool isOpen = false;
    ifstream in(filename);

    // cout << "function called" << endl;

    if(in.is_open()) {
        isOpen = true;

        while(getline(in, line)) {
            stringstream ss(line);
            string misspelled;
            string corrected;

            // cout << line << endl;

            getline(ss, misspelled, '\t');
            getline(ss, corrected, '\n');
            correctedWords[numCorrected][0] = misspelled;
            correctedWords[numCorrected][1] = corrected;

            numCorrected++;
            if(numCorrected == SIZE) {
                // cout << "correctedWords exceeded" << endl;
                break;
            }
            // cout << misspelled << "  " << corrected << endl;
        }
    }

    return isOpen;

}

bool SpellChecker::isValid(string word) {
    bool isWord = false;
    for(int idx = 0; idx < numValid; idx++) {
        if(validWords[idx] == word) {
            isWord = true;
            return true;
        }
    }
    return isWord;
}

string SpellChecker::extractWord(string word) {
    // string result = "";
    // for(int i = 0; i < word.length(); i++) {
    //     if(word[i] != ',' && word[i] != '!' && word[i] != '.') {
    //         result += toLower(word[i]);
    //     }
    // }


    // cout << "before -> " << word << endl;

    char begging_letter = word[0];

    // cout << "->" << last_letter << endl;
    //
    // if (last_letter == '!' || last_letter == '.') {
    //     word = word.substr(0, word.length() - 1);
    // }


    if (!(begging_letter  >= 'A' && begging_letter <= 'z')) {
        // cout << "true?" << endl;
        word = word.substr(1, word.length());
    }


    char last_letter = word[word.length() -1];


    if (!(last_letter  >= 'A' && last_letter <= 'z')) {
        // cout << "true?" << endl;
        word = word.substr(0, word.length() - 1);
    }


    string newWord = "";
    for(int i = 0; i < word.length(); i++) {
        newWord += tolower(word[i]);

    }

    // cout << "check -> " << newWord << endl;

    return newWord;
}

string SpellChecker::lookUp(string word) {
    bool isFound = false;
    int idx = 0;
    string correctedWord = "";

    while (idx < numCorrected && !isFound) {
        if(correctedWords[idx][0] == word) {
            correctedWord = correctedWords[idx][1];
            isFound = true;
        }
        idx++;
    }
    if(!isFound) {
        correctedWord = begin_mark + word + end_mark;
    }
    return correctedWord;
}

char SpellChecker::toLower(char l) {
    if(l <= 'Z' && l >= 'A') {
        return l - ('Z' - 'z');
    }
    return l;
}

string SpellChecker::fixUp(string sentence){
    stringstream ss(sentence);

    string word;
    string result = "";

    while (getline(ss, word, ' ')) {
        // cout << word << "<=" << endl;

        word = extractWord(word);
        // cout << word << "<-" << endl;
        if(isValid(word)) {
            result = result + word + " ";

        } else {
            string corrected = lookUp(word);
            result = result + corrected + " ";
        }
    }
    return result;
}








// end of SpellChecker
