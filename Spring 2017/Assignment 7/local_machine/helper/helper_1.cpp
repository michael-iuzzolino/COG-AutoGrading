#include <iostream>
#include <fstream>
#include "SpellChecker.h"

using namespace std;

int Test_SpellChecker()
{
	string name = "American";
	SpellChecker speller1(name);

	cout << "SpellChecker 1's language: " << speller1.language << endl;
	cout << "   # words in valid list: " << speller1.getNValidWords() << endl;
	cout << "   # corrected words    : " << speller1.getNMisspelled() << endl;

	name = "English";
	SpellChecker speller2(name);
	cout << "Loading A-K: " <<endl;
	speller2.loadValidWords("VALID_WORDS_A_K.txt");

	cout << "SpellChecker 2's language: " << speller2.language << endl;
	cout << "   # words in valid list: " << speller2.getNValidWords() << endl;
	cout << "   # corrected words    : " << speller2.getNMisspelled() << endl;

	cout << "Loading L-Z: " <<endl;
	speller2.loadValidWords("VALID_WORDS_L_Z.txt");
	cout << "   # words in valid list: " << speller2.getNValidWords() << endl;
	cout << "   # corrected words    : " << speller2.getNMisspelled() << endl;

	cout << "Loading Misspelled: " <<endl;
	speller2.loadCorrections("MISSPELLED.txt");
	cout << "   # words in valid list: " << speller2.getNValidWords() << endl;
	cout << "   # corrected words    : " << speller2.getNMisspelled() << endl;

	cout << "SpellChecker 1" << endl;
	cout << "   Lookup(\"teh\"): " << speller1.lookup("teh") << endl;
	cout << "   Lookup(\"according\"): " << speller1.lookup("according") << endl;

	cout << "SpellChecker 2" << endl;
	cout << "   Lookup(\"teh\"): " << speller2.lookup("teh") << endl;
	cout << "   Lookup(\"according\"): " << speller2.lookup("according") << endl;
	cout << "   Lookup(\"acubar\"): " << speller2.lookup("acubar") << endl;


	string sentence;
	name = "English";
	SpellChecker speller3(name);
	speller3.loadValidWords("VALID_WORDS_3000.txt");

	cout << "SpellChecker 3's language: " << speller3.language << endl;
	cout << "   # words in valid list: " << speller3.getNValidWords() << endl;
	cout << "   # corrected words    : " << speller3.getNMisspelled() << endl;

	cout << "Loading Misspelled: " <<endl;
	speller3.loadCorrections("MISSPELLED.txt");
	cout << "   # words in valid list: " << speller3.getNValidWords() << endl;
	cout << "   # corrected words    : " << speller3.getNMisspelled() << endl;

	cout << "SpellChecker 3" << endl;
	cout << "   fixUp(\"teh\"): " << speller3.fixUp("teh") << endl;
	cout << "   fixUp(\"according\"): " << speller3.fixUp("according to the world press") << endl;
	cout << "   fixUp(\"acubar\"): " << speller3.fixUp("Make mine an acubar punch.") << endl;

	sentence = "What we have got here is failure to communicate";
	cout << "   fixUp(...): " << speller3.fixUp(sentence) << endl;
	sentence = "There is no place like home";
	cout << "   fixUp(...): " << speller3.fixUp(sentence) << endl;

	sentence = "You can't handle the truth!";
	cout << "   fixUp(...): " << speller3.fixUp(sentence) << endl;
	return 0;
}



int main()
{
	Test_SpellChecker();
	return 0;
}
