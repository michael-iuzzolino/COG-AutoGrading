#include <iostream>
#include <fstream>
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
  else { return filename.length(); }

  return line_count;
}

int main() {
  cout << "Count: " << CountLines("infile.txt") << endl;
}
