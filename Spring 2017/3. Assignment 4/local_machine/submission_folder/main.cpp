#include <iostream>
#include "Assignment4.cpp"
using namespace std;

const string humanDNA   = "CGCAAATTTGCCGGATTTCCTTTGCTGTTCCTGCATGTAGTTTAAACGAGATTGCCAGCACCGGG"
						  "TATCATTCACCATTTTTCTTTTCGTTAACTTGCCGTCAGCCTTTTCTTTGACCTCTTCTTTCTGT"
						  "TCATGTGTATTTGCTGTCTCTTAGCCCAGACTTCCCGTGTCCTTTCCACCGGGCCTTTGAGAGGT"
						  "CACAGGGTCTTGATGCTGTGGTCTTCATCTGCAGGTGTCTGACTTCCAGCAACTGCTGGCCTGTG"
						  "CCAGGGTGCAGCTGAGCACTGGAGTGGAGTTTTCCTGTGGAGAGGAGCCATGCCTAGAGTGGGAT"
						  "GGGCCATTGTTCATG";
const string mouseDNA   = "CGCAATTTTTACTTAATTCTTTTTCTTTTAATTCATATATTTTTAATATGTTTACTATTAATGGTTATCATTCACCATTTAACTATTTGTTATTTTGACGTCATTTTTTTCTATTTCCTCTTTTTTCAATTCATGTTTATTTTCTGTATTTTTGTTAAGTTTTCACAAGTCTAATATAATTGTCCTTTGAGAGGTTATTTGGTCTATATTTTTTTTTCTTCATCTGTATTTTTATGATTTCATTTAATTGATTTTCATTGACAGGGTTCTGCTGTGTTCTGGATTGTATTTTTCTTGTGGAGAGGAACTATTTCTTGAGTGGGATGTACCTTTGTTCTTG";
const string unknownDNA = "CGCATTTTTGCCGGTTTTCCTTTGCTGTTTATTCATTTATTTTAAACGATATTTATATCATCGGGTTTCATTCACTATTTTTCTTTTCGATAAATTTTTGTCAGCATTTTCTTTTACCTCTTCTTTCTGTTTATGTTAATTTTCTGTTTCTTAACCCAGTCTTCTCGATTCTTATCTACCGGACCTATTATAGGTCACAGGGTCTTGATGCTTTGGTTTTCATCTGCAAGAGTCTGACTTCCTGCTAATGCTGTTCTGTGTCAGGGTGCATCTGAGCACTGATGTGGAGTTTTCTTGTGGATATGAGCCATTCATAGTGTGGGATGTGCCATAGTTCATG";

/****************************************************************************************

	Your program will ask the user for two sequences that will be used in calculating
	a Hamming distance.   Pass the two sequences to a function named calcSimilarity
	that returns a floating-point result (similarity score described above).

	Repeat until the sequence 1 given is a single character ‘*’.

	The output should correspond to the following:

		Enter sequence 1:
		CCGCCGCCGA
		Enter sequence 2:
		CCTCCTCCTA
		Hamming: 0.7
		Enter sequence 1:
		*

*****************************************************************************************/
void part1()
{
    cout<<"part1"<<endl;
	string seq1;
	string seq2;

	cout << "Enter sequence 1:" << endl;
	cin >> seq1;

	// loop until codon is "*" string
	while ( seq1 != "*" )
	{
		cout << "Enter sequence 2:" << endl;
		cin >> seq2;

		// calculate and print the similarity score
		float score;

		score = calcSimilarity(seq1, seq2);
		cout << "Similarity: " << score << endl;

		// get the next sequence pair
		cout << "Enter sequence 1:" << endl;
		cin >> seq1;
	}
}

/****************************************************************************************

	Your program will ask the user for a codon sequence (three characters).

	You will search each of the given species (human, mouse, unknown) to find all
	the locations that match that codon.

	Your program will pass each of the predefined sequences along with the codon to
	the listCodonPositions() function that does not return any value.   Repeat until
	the codon given is the empty string (no characters).

	The output should correspond to the following:
		Enter codon:
		CCG
		Human: 11 61 98 165 179
		Mouse:
		Unknown: 11 179
		Enter codon:

*****************************************************************************************/
void part2()
{
    cout<<"part2"<<endl;
	string codon;

	cout << "Enter codon:" << endl;
	cin >> codon;
//	cout << "Codon(" << codon << ")" << endl;

	// loop until codon is "*" string
	while ( codon != "*" )
	{
		// search for and print the match locations
		listSequencePositions(humanDNA,"Human", codon);
		cout << endl;

		listSequencePositions(mouseDNA,"Mouse" ,codon);
		cout << endl;

		listSequencePositions(unknownDNA,"Unknown", codon);
		cout << endl;

		// get next codon
		cout << "Enter codon:" << endl;
		cin >> codon;
//		cout << "Codon(" << codon << ")" << endl;
	}
}

/****************************************************************************************
	Your program will ask the user for a sequence that will be compared to each of the genomes (Human, Mouse, Unknown)
	to find which has the best match to the given sequence.  Your program will provide a function compareDNA() to find
	the best (Maximum) similarity score of the given sequence anywhere along the given genome. Your program will output
	 the name of the genome with the best match.  Have your main code repeat until the sequence given is a single
	 character ‘*’.

*****************************************************************************************/
void part3()
{
    cout<<"part3"<<endl;
	string seq;

	cout << "Enter user sequence:" << endl;
	cin >> seq;

	// loop until codon is "*" string
	while ( seq != "*" )
	{
	  compare3Genomes(humanDNA,"Human",mouseDNA,"Mouse",unknownDNA,"Unknown",seq);
		// get the next sequence pair
		cout << "Enter user sequence:" << endl;
		cin >> seq;
	}
}


/****************************************************************************************
	Main function will call each of the individual assignment parts.
*****************************************************************************************/
int main()
{
	part1();
	part2();
	part3();
	return 0;
}
