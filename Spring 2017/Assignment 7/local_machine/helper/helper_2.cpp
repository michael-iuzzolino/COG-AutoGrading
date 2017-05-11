#include <iostream>
#include <fstream>
#include "WordCounts.h"

using namespace std;





void Test_Common(WordCounts &counter, int n)
{
	int counts[100];
	string common[100];

	cout << "\tmostCommon(...," << n << "): \n";
	counter.mostCommon(common, counts, n);
	for (int i=0 ; i < n ; i++)
		cout << "\t\t[" << common[i] << "]: " << counts[i] << endl;
}


int Test_WordCounts()
{
	WordCounts  counter;

	cout << "Testing WordCounts Class:" << endl;
	cout << "\tgetCount(\"Jane\"): " << counter.getCount("Jane") << endl;

	// read file and count words
	cout << "\tReading file, counting words:" << endl;
	ifstream in("GOODALL.txt");
	if (in)
	{
		// read each line and count words
		int n_lines = 0;
		while ( !in.eof() )
		{
			string line;

			getline(in, line);
			if (line.length() < 1) continue;

			counter.countWords(line);

			n_lines++;
//			if (n_lines > 10) break;  // limit text for testing
		}
	}
	in.close();

	cout << endl;
	cout << "\tgetCount(\"Jane\"): " << counter.getCount("Jane") << endl;
	cout << "\tgetCount(\"jane\"): " << counter.getCount("jane") << endl;
	cout << "\tgetCount(\"in\"): " << counter.getCount("in") << endl;
	cout << "\tgetCount(\"She\"): " << counter.getCount("she") << endl;

	Test_Common(counter, 10);
	Test_Common(counter, 20);
	Test_Common(counter, 50);

	return 0;
}

int main()
{
	Test_WordCounts();
	return 0;
}
