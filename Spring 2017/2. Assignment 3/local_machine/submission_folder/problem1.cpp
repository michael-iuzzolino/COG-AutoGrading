
#include <iostream>
#include <string>   // INCLUDE if you want to use GETLINE; See http://www.cplusplus.com/reference/string/string/getline/

using namespace std;


/*
 * Function name: prompt_user
 * --------------------------
 * input: void
 * output: user's response (type char)
 * function:
      1. Declare variables
      2. Prompts the user if they want to play the game.
      3. Check for valid input and reprompt until valid input
      4. Return valid user response to main
 */
char promptUser(void)
{
    // Declare variables
    char user_input;
    string prompt;

    // Initialize the prompt
    prompt = "Do you want to play the game (y) or (n)? ";

    // Prompt the user and obtain their response
    cout << prompt;
    cin >> user_input;

    // Check that their response is valid and reprompt while invalid
    while ((user_input != 'y') && (user_input != 'n'))
    {
        cout << prompt;
        cin >> user_input;
    }

    // Clears the input buffer - enables the user of getline(cin, <variable>)
    cin.ignore();
    cin.clear();

    // Returns the user's valid input to main
    return user_input;
}


/*
 *  Function name: madLibs
 *  ----------------------
 *  input: void
 *  output: void
 *  function:
       1. Declare variables
       2. Prompts user for parts of speech (i.e., nouns, adjectives, etc.)
       3. Construct madlib
       4. PRINT the madlib
 */
void madLibs(void)
{
    /*
     Template
     --------
     “In the book War of the <PLURAL NOUN>,
      the main character is an anonymous <OCCUPATION>
      who records the arrival of the <ANIMAL>s in <PLACE>.
      Needless to say, havoc reigns as the <ANIMAL>s
      continue to <VERB> everything in sight,
      until they are killed by the common <SINGULAR NOUN>.”
     */

    // Declaration of variables
    string plural_noun, singular_noun, occupation, animal, place, verb;
    string mab_lib;

    // Prompt the user for the parts of speech
    cout << "Enter a PLURAL NOUN: ";
    getline(cin, plural_noun);

    cout << "Enter a SINGULAR NOUN: ";
    getline(cin, singular_noun);

    cout << "Enter an OCCUPATION: ";
    getline(cin, occupation);

    cout << "Enter an ANIMAL name: ";
    getline(cin, animal);

    cout << "Enter the name of a PLACE: ";
    getline(cin, place);

    cout << "Enter a VERB: ";
    getline(cin, verb);

    // Construct the ablib
    mab_lib = "\nIn the book War of the " + plural_noun
            + ", the main character is an anonymous " + occupation + " "
            + "who records the arrival of the " + animal + "s in " + place + " -- "
            + "Needless to say, havoc reigns as the " + animal + "s "
            + "continue to " + verb + " everything in sight, "
            + "until they are killed by the common " + singular_noun + ".\n";

    // PRINT the mab_lib
    cout << mab_lib;


    // Return VOID to main. This return is optional (only when function output is void).
    return;
}


/*
 * Function: main
 * --------------
 * The main function should:
 *    1. Prompt the user if they'd like to play the game.
 *         - call prompt_play_game
 *    2. WHILE user wants to play, call madLibs
 *    3. Exits the program when user no longer wants to play
 *
 *    - Program should allow user to continually play the game
 *      without needing to reload the program. Think WHILE loops.
 */
int main(void)
{
    // Declare variables
    char user_input;

    // Prompt user to play the game
    user_input = promptUser();

    // Play madLibs until user no longer wishes to play
    while (user_input == 'y')
    {
        // Call madLibs
        madLibs();

        // Reprompt user to see if they would like to continue playing. Without this reprompt, infinite loop!
        user_input = promptUser();
    }

    // PRINT exit message
    cout << "Good bye!" << endl;

    // For this course (CSCI 1300) main MUST ALWAYS return 0
    return 0;
}
