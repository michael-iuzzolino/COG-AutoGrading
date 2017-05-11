#ifndef SPELLCHECKER_H
#define SPELLCHECKER_H

// #define N_WORDS 1000

class SpellChecker {
    public:
        std::string language;
        SpellChecker();
        SpellChecker(std::string);
        SpellChecker(std::string, std::string, std::string);
        // load valid words from a file
        bool loadValidWords(std::string filename);
        // load misspellings and corrected words from file
        bool loadMisspelledWords(std::string filename);
        void setBeginMarker(char begin);
        void setEndMarker(char end);
        char getBeginMarker();
        char getEndMarker();
        // int getNValidWords();
        // int getNMisspelled();
        // Fix all spelling errors in a string
        std::string fixUp(std::string sentence);

    private:
        char begin_mark;
        char end_mark;
        const static int SIZE = 10000;
        int numValid;
        int numCorrected;
        bool isValid(std::string word);
        char toLower(char l);
        std::string lookUp(std::string word);
        std::string extractWord(std::string word);
        std::string validWords[SIZE];
        std::string correctedWords[SIZE][2];

};


#endif // SPELLCHECKER_H
