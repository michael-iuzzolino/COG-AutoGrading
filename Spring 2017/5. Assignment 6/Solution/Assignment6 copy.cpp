#include <fstream>
#include <iostream>
#include <fstream>
#include <sstream>
#include<cstdlib>
using namespace std;


/**************************************************************************
The CountLines() function will take in a single argument, i.e. the filename.
You should pass the name of your file from you main function to this function.
The function will count the number of lines in the file and return the count.
**************************************************************************/


int CountLines(string filename)
{
   //Open the file to read the contents of the file.
   ifstream infile;
   infile.open(filename.c_str());

   string datum;
   int count =0;

   //Count the number of lines in the file.
   while (infile >> datum) {
     count++;
    }
   infile.close();

   return count;
}

/****************************************************************************
The ReadScores() function will take in four arguments, i.e. the filename, the
array of names , the array of average scores and the size of the array.The file
will have data in the following format : Name1, Score1, Score2, Score3 … ScoreK,
where K is an arbitrary number.The function will store the names of the students
in the names array and will calculate the average score of each student and store
it in the avg_scores array. It will return the number of lines in the file.
*******************************************************************************/

int ReadScores( string filename, string names[], float avg_scores[],int array_size){

    //Open the file to read the contents of the file.
    ifstream infile;
    infile.open(filename.c_str());

    string nam;
    int i=0;
    float sum = 0.0;
    int numOfScores = 0;
    string token;
    int count = 0;


    //Store the names in the names array and corresponding average score of the student in the avg_scores array
    while(!infile.eof())
    {
        //Maintain the count of the number of lines in the file.
        if(getline(infile,nam))
            count = count + 1;

        istringstream ss(nam);
        getline(ss, token, ',');
        names[i]=token;
        numOfScores = 0;
        sum = 0.0;

        //Calculate the sum of scores of the student and maintain a count of the number of scores.
        while(getline(ss, token, ',')) {
          sum = sum + atof(token.c_str());
          numOfScores++;
       }
       //Store the average score in the avg_scores array.
       avg_scores[i] = sum/numOfScores;
       i++;
    }

    return count;

}

/******************************************************************************
The sortNames() function is a helper function to sort the names of the students.
It will take in three arguments, i.e. the array of names , the array of average
scores and the size of the array.The function will sort the names of the students
in the names array and will also change the order of the avg_scores so that it
corresponds to the correct name in the names array. The function does not return
any value.
********************************************************************************/

void sortNames(string names[],float avg_scores[],int size){
    //Bubble sort to sort the names in the names array in ascending order.
    int n = size;
    while(n!=0){
        for(int j =0;j<n-1;j++){
            if(names[j]>names[j+1]){
                string name = names[j];
                names[j] = names[j+1];
                names[j+1] = name;

                float temp = avg_scores[j];
                avg_scores[j] = avg_scores[j+1];
                avg_scores[j+1] = temp;
            }
        }
        n=n-1;
    }

}

/**************************************************************************
The WriteGrades() function will take in four arguments, i.e. the filename, the
array of names , the array of average scores and the number of students.
The function will first sort the names in the names array in ascending order.
It will then write the names, average scores and grades of the student in the
file in the following format :<Name> , <average score>, <grade>
**************************************************************************/

void WriteGrades( string filename, string names[], float avg_scores[], int n_students)
{
    //Sorting the names in ascending alphabetical order

    sortNames(names,avg_scores,n_students);

    //Open the file to write contents into the file.
    ofstream myfile;
    myfile.open (filename.c_str());
    //Calculate grade of the student
    for(int  i=0 ; i<n_students;i++){
        char grade;
        if(avg_scores[i] >=90)
          grade = 'A';
        else if(avg_scores[i]>=80  && avg_scores[i]<90)
          grade ='B';
        else if(avg_scores[i]>=70  && avg_scores[i] <80)
          grade ='C';
        else if(avg_scores[i]>=60  && avg_scores[i] <70)
          grade ='D';
        else
          grade = 'F';

        //Write the content to the file.
        myfile<<names[i]<<","<<avg_scores[i]<<","<<grade<<"\n";
    }
    myfile.close();


}
