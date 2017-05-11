#include <iostream>
#include <fstream>

using namespace std;

#include "SpellChecker.h"


void test_case_0()
{
	// 	Default constructor
	// 	i. 		Check name is valid string (print name without crash)
	// 	ii. 	Check name is string data type
	//  iii. 	Set the begin, end markers
	// 	iv. 	Check the begin, end markers
	SpellChecker speller1;

}


void test_case_1()
{
	// 	Default constructor
	// 	i. 		Check name is valid string (print name without crash)
	// 	ii. 	Check name is string data type
	//  iii. 	Set the begin, end markers
	// 	iv. 	Check the begin, end markers
	SpellChecker speller1;

	char begin_marker, end_marker;

	// iii. Set the begin and end markers
	speller1.setBeginMarker('[');
	speller1.setEndMarker(']');

	// iv. Check the begin, end markers
	begin_marker = speller1.getBeginMarker();
	end_marker = speller1.getEndMarker();
	cout << "Begin marker: " << begin_marker << endl;
	cout << "End marker: " << end_marker << endl;

	speller1.setBeginMarker('*');
	speller1.setEndMarker('@');

	// iv. Check the begin, end markers
	begin_marker = speller1.getBeginMarker();
	end_marker = speller1.getEndMarker();
	cout << "Begin marker: " << begin_marker << endl;
	cout << "End marker: " << end_marker << endl;
}


void test_case_2()
{
	// Single param constructor
	string name = "American";
	SpellChecker speller2(name);


	// i. Check name is a valid string
	cout << "Language: " << speller2.language << endl;

	// ii. Check name is string data type ??

	// iii. Set the begin and end markers
	speller2.setBeginMarker('[');
	speller2.setEndMarker(']');

	// iv. Check the begin, end markers
	char begin_marker = speller2.getBeginMarker();
	char end_marker = speller2.getEndMarker();
	cout << "Begin marker: " << begin_marker << endl;
	cout << "End marker: " << end_marker << endl;

}


void test_case_3()
{
	// Three param constructor
	string name = "English";

	string valid_words_filename;
	string misspelled_filename;

	cin >> valid_words_filename;
	cin >> misspelled_filename;

	SpellChecker speller3(name, valid_words_filename, misspelled_filename);

	// i. Check name is a valid string
	cout << "Language: " << speller3.language << endl;

}





void test_case_4()
{
	// Method: bool loadValidWords(string filename)
	// i. 		Invalid filename returns false
	// ii. 		Valid filename loads words (check for items in the file, check for items not the file, use fixUp(word) to verify.
	// iii 		Add second filename (all words still there from before, new words can be found)
	string fixed_string;
	string name = "English";
	bool correctly_loaded;

	SpellChecker speller4(name);

	speller4.setBeginMarker('[');
	speller4.setEndMarker(']');

	// i. Invalid filename returns false
	correctly_loaded = speller4.loadValidWords("234235s3.txt");
	cout << "Correctly loaded: " << correctly_loaded << endl;

	fixed_string = speller4.fixUp("today");
	cout << "Fixed string: " << fixed_string << endl;

	// ii. Valid filename loads words
	correctly_loaded = speller4.loadValidWords("VALID_WORDS_3000.txt");
	cout << "Correctly loaded: " << correctly_loaded << endl;

	// iii. add second filename
	correctly_loaded = speller4.loadValidWords("VALID_WORDS_3000.txt");
	cout << "Correctly loaded: " << correctly_loaded << endl;

	fixed_string = speller4.fixUp("today");
	cout << "Fixed string: " << fixed_string << endl;

}


void test_case_5()
{
	// Method: bool loadMisspelledWords(string filename)
	// i. 		Invalid filename returns false
	// ii. 		Valid filename loads words (check for items in the file, check for items not the file, use fixUp(word) to verify.
	// iii. 	Add second filename (all words still there from before, new words can be found)

	string fixed_string;
	string name = "English";
	bool correctly_loaded;

	SpellChecker speller5(name);

	// i. Invalid filename returns false
	correctly_loaded = speller5.loadValidWords("234235s3.txt");
	cout << "Correctly loaded: " << correctly_loaded << endl;


	// ii. Valid filename loads words
	correctly_loaded = speller5.loadMisspelledWords("MISSPELLED.txt");
	cout << "Correctly loaded: " << correctly_loaded << endl;

	// iii. Valid filename loads words a second time
	correctly_loaded = speller5.loadMisspelledWords("TEXT_2_ENGLISH.txt");
	cout << "Correctly loaded: " << correctly_loaded << endl;

	fixed_string = speller5.fixUp("todayy");
	cout << "Fixed string: " << fixed_string << endl;

}


void test_case_6()
{
	// Method: string fixUp(string sentence)
	// i. single words (CORRECT, misspelled, unknown)


	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller6(name);

	speller6.setBeginMarker('*');
	speller6.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller6.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller6.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller6.fixUp("today");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller6.fixUp("cake");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller6.fixUp("climb");
	cout << "Fixed string: " << fixed_string << endl;

}


void test_case_7()
{
	// Method: string fixUp(string sentence)
	// i. single words (correct, MISSPELLED, unknown)


	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller7(name);

	speller7.setBeginMarker('*');
	speller7.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller7.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller7.loadMisspelledWords("MISSPELLED.txt");
	correctly_loaded = speller7.loadMisspelledWords("TEXT_2_ENGLISH.txt");

	fixed_string = speller7.fixUp("todayy");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller7.fixUp("bnr");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller7.fixUp("h8r");
	cout << "Fixed string: " << fixed_string << endl;
}

void test_case_8()
{
	// Method: string fixUp(string sentence)
	// i. single words (correct, misspelled, UNKNOWN)


	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller8(name);

	speller8.setBeginMarker('*');
	speller8.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller8.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller8.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller8.fixUp("toodayy");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller8.fixUp("hmewrkk");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller8.fixUp("instulatikon");
	cout << "Fixed string: " << fixed_string << endl;
}



void test_case_9()
{
	// Method: string fixUp(string sentence)
	// ii. Multiword replacement of misspelled words

	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller9(name);

	speller9.setBeginMarker('*');
	speller9.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller9.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller9.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller9.fixUp("abouy clock todayy");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller9.fixUp("clearly todayy intelejent");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller9.fixUp("necesser clock today");
	cout << "Fixed string: " << fixed_string << endl;

}


void test_case_10()
{
	// Method: string fixUp(string sentence)
	// iii. Single words with punctuation (punctuation removed from CORRECT, misspelled, unknown)

	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller10(name);

	speller10.setBeginMarker('*');
	speller10.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller10.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller10.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller10.fixUp("today,");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller10.fixUp(".today,");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller10.fixUp("!today.");
	cout << "Fixed string: " << fixed_string << endl;

}


void test_case_11()
{
	// Method: string fixUp(string sentence)
	// iii. Single words with punctuation (punctuation removed from correct, MISSPELLED, unknown)

	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller11(name);

	speller11.setBeginMarker('*');
	speller11.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller11.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller11.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller11.fixUp("todayy,");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller11.fixUp("!todayy,");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller11.fixUp(".todayy");
	cout << "Fixed string: " << fixed_string << endl;

}

void test_case_12()
{
	// Method: string fixUp(string sentence)
	// iii. Single words with punctuation (punctuation removed from correct, misspelled, UNKWOWN)

	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller12(name);

	speller12.setBeginMarker('*');
	speller12.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller12.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller12.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller12.fixUp("toodayy,");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller12.fixUp(".toodayy,");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller12.fixUp("!toodayy");
	cout << "Fixed string: " << fixed_string << endl;

}


void test_case_13()
{
	// Method: string fixUp(string sentence)
	// iv. Sentences
	// 		** All correct
	// 		All misspelled (single word replacement)
	// 		All misspelled (multi-word replacement)
	// 		All unknown
	// 		Multi-case words
	// 		Punctuation in words

	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller13(name);

	speller13.setBeginMarker('*');
	speller13.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller13.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller13.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller13.fixUp("hello world");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller13.fixUp("comedy world");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller13.fixUp("hello emotional");
	cout << "Fixed string: " << fixed_string << endl;

}


void test_case_14()
{
	// Method: string fixUp(string sentence)
	// iv. Sentences
	// 		All correct
	// 		** One misspelled (single word replacement)
	// 		All misspelled (multi-word replacement)
	// 		All unknown
	// 		Multi-case words
	// 		Punctuation in words

	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller14(name);

	speller14.setBeginMarker('*');
	speller14.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller14.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller14.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller14.fixUp("hello todayy");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller14.fixUp("mosaik world");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller14.fixUp("hello neighbour");
	cout << "Fixed string: " << fixed_string << endl;

}


void test_case_15()
{
	// Method: string fixUp(string sentence)
	// iv. Sentences
	// 		All correct
	// 		All misspelled (single word replacement)
	// 		** All misspelled (multi-word replacement)
	// 		All unknown
	// 		Multi-case words
	// 		Punctuation in words

	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller15(name);

	speller15.setBeginMarker('*');
	speller15.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller15.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller15.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller15.fixUp("abouy todayy");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller15.fixUp("permissable abouy todayy fone");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller15.fixUp("abouy funetik todayy");
	cout << "Fixed string: " << fixed_string << endl;

}


void test_case_16()
{
	// Method: string fixUp(string sentence)
	// iv. Sentences
	// 		All correct
	// 		All misspelled (single word replacement)
	// 		All misspelled (multi-word replacement)
	// 		** All unknown
	// 		Multi-case words
	// 		Punctuation in words

	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller16(name);

	speller16.setBeginMarker('*');
	speller16.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller16.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller16.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller16.fixUp("abouuy toodayy");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller16.fixUp("permisssable abbouy toddayy foone");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller16.fixUp("hielo thiiis inini pudabi");
	cout << "Fixed string: " << fixed_string << endl;

}


void test_case_17()
{
	// Method: string fixUp(string sentence)
	// iv. Sentences
	// 		All correct
	// 		All misspelled (single word replacement)
	// 		All misspelled (multi-word replacement)
	// 		All unknown
	// 		** Multi-case words
	// 		Punctuation in words

	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller17(name);

	speller17.setBeginMarker('*');
	speller17.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller17.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller17.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller17.fixUp("toDaY");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller17.fixUp("HeLlO");
	cout << "Fixed string: " << fixed_string << endl;


}


void test_case_18()
{
	// Method: string fixUp(string sentence)
	// iv. Sentences
	// 		All correct
	// 		All misspelled (single word replacement)
	// 		All misspelled (multi-word replacement)
	// 		All unknown
	// 		Multi-case words
	// 		** Punctuation in words

	string name = "English";
	string fixed_string;

	bool correctly_loaded;

	SpellChecker speller18(name);

	speller18.setBeginMarker('*');
	speller18.setEndMarker('*');
	// ii. Valid filename loads words
	correctly_loaded = speller18.loadValidWords("VALID_WORDS_3000.txt");
	correctly_loaded = speller18.loadMisspelledWords("MISSPELLED.txt");

	fixed_string = speller18.fixUp("tod!ay");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller18.fixUp("t?od!ay");
	cout << "Fixed string: " << fixed_string << endl;

	fixed_string = speller18.fixUp("t?oday");
	cout << "Fixed string: " << fixed_string << endl;

}






int main()
{
	int test_case_number;
	cin >> test_case_number;

	switch (test_case_number)
	{
		case 0:
			test_case_0();
			break;

		case 1:
			test_case_1();
			break;

		case 2:
			test_case_2();
			break;

		case 3:
			test_case_3();
			break;

		case 4:
			test_case_4();
			break;

		case 5:
			test_case_5();
			break;

		case 6:
			test_case_6();
			break;

		case 7:
			test_case_7();
			break;

		case 8:
			test_case_8();
			break;

		case 9:
			test_case_9();
			break;

		case 10:
			test_case_10();
			break;

		case 11:
			test_case_11();
			break;

		case 12:
			test_case_12();
			break;

		case 13:
			test_case_13();
			break;

		case 14:
			test_case_14();
			break;

		case 15:
			test_case_15();
			break;

		case 16:
			test_case_16();
			break;

		case 17:
			test_case_17();
			break;

		case 18:
			test_case_18();
			break;

	}


	return 0;
}
