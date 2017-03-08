#include<iostream>
using namespace std;

/****************************************************************************************
	The calcSimilarity() function will take two arguments that are both strings.
	The function calculates the Hamming distance and returns the similarity score.
	This function should only calculate the similarity if the two strings are the
	same length, otherwise return 0.
*****************************************************************************************/
float calcSimilarity (string sequenceOne, string sequenceTwo)
{
	int hamming = 0;
	float score = 0.0;
	if (sequenceOne.length() != sequenceTwo.length())
    	return score;
	else
	{
		for (int i=0 ; i < sequenceOne.length() ; i++)
		{
			if (sequenceOne[i] != sequenceTwo[i])
				hamming = hamming + 1;
		}

		// Calculate the similarity score as defined in assignment
		// multiple by 1.0 to force it into floating point calculation
		score = 1.0 * (sequenceOne.length() - hamming) / sequenceOne.length();
	}

	return score;
}


/*****************************************************************************************

	The listCodonPositions() function will take three arguments,genomeSequence,genomeName and
	seq that are all string arguments and prints the genomeName followed by each of the positions
	where genomeSequence has an exact match to seq.

	The function will print genomeName followed by the locations of all exact matches separated by spaces.

*****************************************************************************************/


void listSequencePositions(string genomeSequence, string genomeName, string seq)
{
    bool match;
  	cout << genomeName << " match locations:";
    int check_length = (int)genomeSequence.length() - (int)seq.length();
    for (int i=0; i <= check_length; i++)
    {
        match = true;
        for (int j=0; j < seq.length(); j++)
        {
            if (genomeSequence[i+j] != seq[j])
            {
                match = false;
                break;
            }
        }
        if (match)
        {
            cout << " " << i+1;
        }
    }
}

/****************************************************************************************
	The compareDNA() function should take two arguments that are both strings.
	The function should calculate the similarity score for each substring of the
	dbSequence (substring should be same length as userSequence) and return the
	best similarity score found across all the possible substrings.
	Use the calcSimilarity() function described above.
*****************************************************************************************/
float compareDNA(string genome, string seq)
{
	float best = 0;

	// step through each of the positions in the dbSequence,
	//		cut out a substring,
	//		compare substring to userSequence
	//		remember best score

	for (int i = 0 ; i < genome.length() ; i++)
	{
		string substring;
		substring = genome.substr(i, seq.length());

		float score;
		score = calcSimilarity(substring, seq);
		if (score > best)
			best = score;
	}

	return best;
}

/****************************************************************************************
The compare3Genomes() function should take seven arguments that are all strings and print the
name of the genome with the best similarity score that can be found for that sequence in the genome.
In the case that multiple genomes have the same best similarity score, print the names of all of the
genomes with the same score.
*****************************************************************************************/

void compare3Genomes(string genome1, string name1, string genome2, string name2, string genome3, string name3, string seq)
{
  	// first score will automatically be the best
    float scoreGenome1 , scoreGenome2 , scoreGenome3;
		scoreGenome1 = compareDNA(genome1, seq);
    float best_score = scoreGenome1;
		// check to see if genome2 scores better

		scoreGenome2 = compareDNA(genome2, seq);
		if (scoreGenome2 > best_score)
		{
			best_score = scoreGenome2;
		}

		// check to see if genome3 scores better
		scoreGenome3 = compareDNA(genome3, seq);
		if (scoreGenome3 > best_score)
		{
			best_score = scoreGenome3;
		}

    if (best_score == scoreGenome1)
    {
			cout << "Best match: " << name1 << endl;
		}
    if (best_score == scoreGenome2)
    {
			cout << "Best match: " << name2 << endl;
		}
    if (best_score == scoreGenome3)
		{
			cout << "Best match: " << name3 << endl;
		}
}
