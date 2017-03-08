#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int CountLines(string filename)
{
  string line;
  ifstream myFile;
  myFile.open(filename);
  int line_count = 0;

  if (myFile.is_open())
  {
    while ( getline (myFile, line) )
    {
      cout << line << '\n';
      line_count++;
    }
    myFile.close();
  }

  return line_count;
}

int ReadScores(string filename, string names[], float avg_scores[], int array_size)
{
  string line;
  ifstream myFile;
  myFile.open(filename);
  int record_index = 0;

  int record_counter;

  if (myFile.is_open())
  {
    while ( getline (myFile, line) )
    {
      string word = "";
      char letter;
      int word_index = 0;
      float average = 0.0;
      record_counter = 0;
      for (int j=0; j < line.length(); j++)
      {
        letter = line[j];
        if (letter != ',')
        {
          word += letter;
        }
        else if (letter == ',')
        {
          if (word_index == 0)
          {
            names[record_index] = word;
          }
          else
          {
            average += stof(word);
            record_counter++;
          }
          word = "";
          word_index++;
        }

        if (j == line.length()-1)
        {
          average += stof(word);
          record_counter++;
        }
      }
      avg_scores[record_index] = average/(record_counter*1.0);
      record_index++;
    }
    myFile.close();
  }

  return record_index;
}



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



void WriteGrades(string filename, string names[], float avg_scores[], int n_students)
{
  sortNames(names,avg_scores,n_students);
  
  ofstream outfile;
  outfile.open(filename);
  string name;
  float ave_score;
  char grade;

  if (outfile.is_open())
  {
    for (int i=0; i < n_students; i++)
    {
      name = names[i];
      ave_score = avg_scores[i];
      if (ave_score >= 90)
      {
        grade = 'A';
      }
      else if (ave_score >= 80)
      {
        grade = 'B';
      }
      else if (ave_score >= 70)
      {
        grade = 'C';
      }
      else if (ave_score >= 60)
      {
        grade = 'D';
      }
      else
      {
        grade = 'F';
      }
      outfile << name;
      outfile << ",";
      outfile << ave_score;
      outfile << ",";
      outfile << grade;
      outfile << "\n";
    }
  }

  return;
}
