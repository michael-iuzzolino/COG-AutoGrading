#include <iostream>
#include <string>

using namespace std;

void listSequencePositions (string genomeSequence, string genomeName, string seq)
{
    cout<<genomeName<<" match locations: ";
    string str="";
    for(int i=0; i<=genomeSequence.length(); i++){
        str=genomeSequence.substr(i,seq.length());
        if(seq==str)
            cout<< i+1<<"  ";
    }
    cout<<endl;

}

float calcSimilarity (string sequenceOne, string sequenceTwo)

{
  int hamming_distance=0;

    if(sequenceOne.length()!=sequenceTwo.length())
        return 0.0;

    for(int i =0; i <sequenceOne.length(); i++)
    {
        if(sequenceOne[i]!=sequenceTwo[i])
        {
          hamming_distance++;
        }
    }
    int numerator =(sequenceOne.length()-hamming_distance);
    int denominator = sequenceOne.length();
    float similarity_score=((float)numerator/(float)denominator);

    return similarity_score;
}

float compareDNA(string genome, string seq){
    float simscore=0.;
    float bestsim=0;
    for(int i =0; i <genome.length(); i++)
    {
           string purple= genome.substr(i, seq.length());
           simscore= calcSimilarity(purple, seq);

            if(simscore>bestsim)
                bestsim=simscore;

    }
    return bestsim;
}

void compare3Genomes(string genome1, string name1, string genome2,string name2, string genome3, string name3, string seq)
{
    float humanscore=compareDNA(genome1, seq);
    float mousescore=compareDNA(genome2, seq);
    float unknownscore=compareDNA(genome3, seq);
    /*cout<<"h" <<humanscore<<endl;
    cout<<"m "<<mousescore<<endl;
    cout<<"u "<<unknownscore<<endl;*/

    if(humanscore>mousescore&&humanscore>unknownscore)
        cout<<"Best match: Human"<<endl;
    if(mousescore>humanscore&&mousescore>unknownscore)
        cout<<"Best match: Mouse"<<endl;
    if(unknownscore>humanscore&&unknownscore>mousescore)
        cout<<"Best match: Unknown"<<endl;
    if(humanscore==mousescore&&humanscore>unknownscore)
    {
        cout<<"Best match: Human"<<endl;
        cout<<"Best match: Mouse"<<endl;
    }
    if(humanscore==unknownscore&&humanscore>mousescore)
    {
        cout<<"Best match: Human"<<endl;
        cout<<"Best match: Unknown"<<endl;
    }
    if(mousescore==unknownscore&&mousescore>unknownscore)
    {
        cout<<"Best match: Mouse"<<endl;
        cout<<"Best match: Unknown"<<endl;
    }


}
