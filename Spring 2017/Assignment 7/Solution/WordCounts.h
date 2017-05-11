#ifndef WORDCOUNTS_H
#define WORDCOUNTS_H

class WordCounts {
    public:
        WordCounts();
        void countWords(std::string sentence);
        int getCount(std::string);
        void resetCounts();
        int mostCommon(std::string words[], int counts[], int n);
        bool setBeginMarker(char begin);
        bool setEndMarker(char end);
        char getBeginMarker();
        char getEndMarker();
        

    private:
        const static int SIZE = 10000;

        int counts[SIZE];
        std::string words[SIZE];

        int numUnique;
        int wordcount;
        bool isUnique(std::string word);
        void addWord(std::string);
        void sort();
        char toLower(char l); 
        std::string extractWord(std::string word);
};

#endif
