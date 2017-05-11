#include <iostream>
#include <fstream>

using namespace std;

#include "WordCounts.h"


void test_case_1()
{
	// 	Default constructor
	WordCounts counter1;
	int count;

	count = counter1.getCount("hello");
	cout << "Count: " << count << endl;

	int n = 2;
	string commonWords[200];
	int wordCounts[200];

	count = counter1.mostCommon(commonWords, wordCounts, n);
	cout << "Most common: " << count << endl;
}


void test_case_2()
{
	// 	void countWords(string sentence)
	// Single word sentence (check counts are 1)
	WordCounts counter2;
	int count;

	counter2.countWords("Hello");

	count = counter2.getCount("hello");
	cout << "Count: " << count << endl;

	counter2.countWords("World");

	count = counter2.getCount("world");
	cout << "Count: " << count << endl;

	counter2.countWords("Tile");

	count = counter2.getCount("tile");
	cout << "Count: " << count << endl;

}

void test_case_3()
{
	// 	void countWords(string sentence)
	// Single word sentence with punctuation (check counts are 1)
	WordCounts counter3;
	int count;

	counter3.countWords("Hello!");

	count = counter3.getCount("hello");
	cout << "Count: " << count << endl;

	counter3.countWords("?World");

	count = counter3.getCount("world");
	cout << "Count: " << count << endl;

	counter3.countWords("!There!");

	count = counter3.getCount("there");
	cout << "Count: " << count << endl;
}

void test_case_4()
{
	// 	void countWords(string sentence)
	// Single word sentence with mixed case (check counts are 1)
	WordCounts counter4;
	int count;

	counter4.countWords("HelLo");

	count = counter4.getCount("hello");
	cout << "Count: " << count << endl;
}

void test_case_5()
{
	// 	void countWords(string sentence)
	// Same single word sentence (counts are correct?)
	WordCounts counter5;
	int count;
  int repeat;
	string word, sentence;
	string words[3] = {"hello", "world", "there"};

	for (int j=0; j < 3; j++)
	{
		word = words[j];
		sentence = "";
		cin >> repeat;
		for (int i=0; i < repeat; i++)
		{
			sentence += word + " ";
		}
		counter5.countWords(sentence);

		count = counter5.getCount(word);
		cout << "Count: " << count << endl;
	}

	
}

void test_case_6()
{
	// 	void countWords(string sentence)
	// Multi-word sentences
	WordCounts counter6;
	int count;

	counter6.countWords("hello world");

	count = counter6.getCount("hello");
	cout << "Count: " << count << endl;

	count = counter6.getCount("world");
	cout << "Count: " << count << endl;

	counter6.countWords("the hell i am the walnut the");

	count = counter6.getCount("i");
	cout << "Count: " << count << endl;

	count = counter6.getCount("the");
	cout << "Count: " << count << endl;
}

void test_case_7()
{
	// 	void countWords(string sentence)
	// Multi-word, sentences with punctuation
	WordCounts counter7;
	int count;

	counter7.countWords("Hello, World!");

	count = counter7.getCount("hello");
	cout << "Count: " << count << endl;

	count = counter7.getCount("world");
	cout << "Count: " << count << endl;
}

void test_case_8()
{
	// 	void countWords(string sentence)
	// Multi-word,sentences with mixed case
	WordCounts counter8;
	int count;

	counter8.countWords("HellO wOrlD");

	count = counter8.getCount("hello");
	cout << "Count: " << count << endl;

	count = counter8.getCount("world");
	cout << "Count: " << count << endl;
}



int main()
{
	int test_case_number;
	cin >> test_case_number;

	switch (test_case_number)
	{
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

	}

	return 0;
}
