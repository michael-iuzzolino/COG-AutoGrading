#include <iostream>

using namespace std;


/*
		Function: calculatePopulation
		-----------------------------
		input: void
		output: void
		operations: Calculates a projected population
 */
void calculatePopulation(void)
{
	// Declaration of variables
	int currentPop;
	int secondsPerYear;
	int secondsPerBirth;
	int secondsPerDeath;
	int secondsPerImmigration;
	int annualBirthRate;
	int annualDeathRate;
	int annualImmigrantRate;
	int annualPop;
	int projectedPop;

	// Initialize constants
	currentPop = 318933342;
	secondsPerYear = 31536000;       ///  (60s/min) * (60min/hr) * (24hr/day) * (365days/yr)
	secondsPerBirth = 2;
	secondsPerDeath = 7;
	secondsPerImmigration = 24;

	// DO calculations
	annualBirthRate = secondsPerYear / secondsPerBirth;
	annualDeathRate = secondsPerYear / secondsPerDeath;
	annualImmigrantRate = secondsPerYear / secondsPerImmigration;
	annualPop = annualBirthRate - annualDeathRate + annualImmigrantRate;
	projectedPop = annualPop + currentPop;

	cout << "The population is " << projectedPop << ".";

	return;
}


/*
		Function: secondsToTime
		-----------------------------
		input: void
		output: void
		operations: converts user-entered seconds to 24-hr time
 */
void secondsToTime(void)
{
	// Declaration of variables
	int total_seconds;
	int hours;
	int minutes;
	int seconds;

	// Get user input
	cout << "Give a number of seconds in a day, ranging from 0 to 86400: ";
	cin >> total_seconds;

  // Do calculations
	hours = total_seconds/(60*60);
	minutes = (total_seconds%(60*60))/60;
	seconds = (total_seconds%60)%60;

	// Print output
	cout << "The time is " << hours << " hours, " << minutes << " minutes, and " << seconds << " seconds." << endl;

	return;
}


/*
		Function: celsiusToFahrenheit
		-----------------------------
		input: void
		output: void
		operations: converts user-entered Fahrenheit value to Celsius
 */
void celsiusToFahrenheit(void)
{
	// Declaration of variables
	float celsius;
	float fahrenheit;

	cout << "Enter a temperature in Celsius: ";
	cin >> celsius;

	fahrenheit = (celsius * 9 / 5.0) + 32;


	cout << celsius << " degrees Celsius is " << fahrenheit << " degrees Fahrenheit.";
	return;
}

int defunct(void)
{
	// Problem 1
	calculatePopulation();

	// Problem 2
	secondsToTime();

	// Problem 3
	celsiusToFahrenheit();

	return 0;
}
