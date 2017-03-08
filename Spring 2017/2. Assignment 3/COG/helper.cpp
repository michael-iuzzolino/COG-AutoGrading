#include <iostream>
#include "student_functions_file_1.cpp"
#include "student_functions_file_2.cpp"


using namespace std;


int main(void)
{
	// Problem 1
	// Testcase 1
	madLibs();
	madLibs();
	madLibs();


	// Problem 2
	double A, r, H, PR;
	double energy_average;
	double energy_consumption_per_house;
	int number_houses_supported;


	// Testcases for energyCalculator
	// Testcase 1
	A = 20;
	r = 0.15;
	H = 1250;
	PR = 0.75;
	energy_average = energyCalculator(A, r, H, PR);
	cout << "The average annual solar energy production is " << energy_average << " kWh." << endl;

	// Testcase 2
	A = 10;
	r = 0.45;
	H = 4000;
	PR = 0.45;
	energy_average = energyCalculator(A, r, H, PR);
	cout << "The average annual solar energy production is " << energy_average << " kWh." << endl;

	// Testcase 3
	A = 40;
	r = 0.15;
	H = 3050;
	PR = 0.60;
	energy_average = energyCalculator(A, r, H, PR);
	cout << "The average annual solar energy production is " << energy_average << " kWh." << endl;


	// Testcases for printEnergy

	A = 20;
	H = 1250;
	PR = 0.75;

	// Testcase 4
	r = 0.10;
	printEnergy(A, r, H, PR);

	// Testcase 5
	r = 0.15;
	printEnergy(A, r, H, PR);

	// Testcase 6
	r = 0.20;
	printEnergy(A, r, H, PR);

	// Testcase 7
	r = 0.25;
	printEnergy(A, r, H, PR);

	// Testcase 8
	r = 0.30;
	printEnergy(A, r, H, PR);

	// Testcase 9
	r = 0.35;
	printEnergy(A, r, H, PR);



	// Testcases for calculateNumberHousesSupported
	// Testcase 10
	energy_average = 3000;
	energy_consumption_per_house = 901;
	number_houses_supported = calculateNumberHousesSupported(energy_average, energy_consumption_per_house);
	cout << number_houses_supported << " houses can be supported." << endl;

	// Testcase 11
	energy_average = 100;
	energy_consumption_per_house = 901;
	number_houses_supported = calculateNumberHousesSupported(energy_average, energy_consumption_per_house);
	cout << number_houses_supported << " houses can be supported." << endl;

	// Testcase 12
	energy_average = 50000;
	energy_consumption_per_house = 901;
	number_houses_supported = calculateNumberHousesSupported(energy_average, energy_consumption_per_house);
	cout << number_houses_supported << " houses can be supported." << endl;


	return 0;
}
