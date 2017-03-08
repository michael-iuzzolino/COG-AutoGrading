#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <string>
using namespace std;

//starts function for the first part of the assignment which count the number of lines in the file
int CountLines(string filename){

    //initializes the file as an out put which means you can only read from it
    ifstream outSample;
    outSample.open (filename.c_str());

    //checks if the file actually opens
    if(outSample.fail()){

        cout << "Error, file could not be open." << endl;
        return 0;
    }

    //declares all the variables needed if the file does open
    int lineCount = 0;
    string line;

    //starts loop to calculate the number of lines
    while (getline(outSample, line)){

        //increments the number of lines in the file by one
        lineCount++;
    }

    //closes the file and ends the function with a return value
    outSample.close();
    return lineCount;
}

//this function activates part two of the assignment which reads the file and cuts it up into piece to be stored later
int ReadScores(string filename, string names[], float avg_scores[], int array_size){

    //initializes the file as an out put which means you can only read from it
    ifstream outSample(filename.c_str());

    //checks if the file actually opens
    if(outSample.fail()){

        cout << "Error, file could not be open." << endl;
        return 0;
    }

    //declares all the variables used in this function
    char comma = ',';

    string line;

    int position = 0;

    //starts the loop in which fills the array in
    while (getline(outSample, line)){
        string name;
        string scores;
        string nameStore;
        string scoreStore;
        int getLineCount = 0;
        float scoreSum = 0;
        //sets the stream line which limits how far the get line can go
        istringstream ss(line);

        //gets the name of the student and stores it the name array
        getline(ss, name, comma);

        //gets rid of the commas
        nameStore = name.substr(0, name.find(name, ','));

        names[position] = nameStore;

        //gets the scores of the average scores of the student and stores it in the right array
        while (getline(ss, scores, comma)){

            //takes out the commas form the scores
            scoreStore = scores.substr(0, scores.find(scores, ','));

            // adds up the total sum of the scores
            scoreSum += stof(scoreStore);

            //increments the get line count which acts as a number tracker of the amount of scores used to find the avg
            getLineCount++;
        }

        //calculates the average score of the student and stores it in the array
        avg_scores[position]= scoreSum/getLineCount;

        //updates the position of the arrays
        position++;

    }

    return position;

}

//this section is for part three in which writes into the file the new sorted data
//this sorts the names of the names of the students
void sortNames(string names[], float avg_scores[], int size){

    //declares all the variables used in this function
    bool sorted = false;
    int position;
    float scoreStore;
    float highScore;
    float lowScore;
    string nameStore;
    string highName;
    string lowName;

    //starts the loop in which sorts the code
    while (!sorted){

        sorted = true;

        for( position = 1; position < size ; position ++){
            highName = names[position];
            lowName = names[position -1];
            highScore = avg_scores[position];
            lowScore = avg_scores[position -1];

            if (lowName[0] > highName[0]){

                //swaps the values around
                nameStore = highName;
                //highName = lowName;
                names[position] = lowName;
               // lowName = nameStore;
                names [position-1] = nameStore ;
                scoreStore = highScore;
                //lowScore = highScore;
                avg_scores[position] = lowScore;
                //highScore = scoreStore;
                avg_scores[position-1] = scoreStore;

                //repeats the while loop
                sorted = false;

            }
        }
    }
}

//this is the main function for part three of the assignment
void WriteGrades(string filename, string names[], float avg_scores[], int n_students){


    //declares all the variables used in this section
    string grades[n_students];

    //this function is called to sort the names of the students
    sortNames(names, avg_scores, n_students);

    //starts to write the file
    ofstream Fileout;
    Fileout.open(filename.c_str());

        //checks if the file failed to open
        if(Fileout.fail()){

            cout << "Error, file could not be open." << endl;
            return;
        }

    //starts writing into the file
    for(int filePosition = 0; filePosition <= n_students; filePosition++){

        //this sets letter grades to average scores
        float scorevalue;

            for(int position = 0; position < n_students; position++){

                scorevalue = avg_scores[position];

                if ((scorevalue >= 90) && (scorevalue <=100)){

                    grades[position] = 'A';
                }
                if ((scorevalue >=80) && (scorevalue <90)){

                    grades[position] = 'B';
                }
                if ((scorevalue >= 70) && (scorevalue <80)){

                    grades[position] = 'C';
                }
                if ((scorevalue >=60) && (scorevalue < 70)){

                    grades[position] = 'D';
                }
                if ((scorevalue >= 0 ) && (scorevalue < 60)){

                    grades[position] = 'F';
                }
            }

        //writes into the file
        Fileout << names[filePosition] << ", " << avg_scores[filePosition] << ", " << grades[filePosition] << endl;

        }
    Fileout.close();
}
