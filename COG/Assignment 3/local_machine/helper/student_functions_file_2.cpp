#include <iostream>

using namespace std;

// Function declarations
double energyCalculator(double, double, double, double);
void printEnergy(double, double, double, double);
int calculateNumberHousesSupported(double, double);


/*
 * Function: main
 * --------------
 * The main function should ...
 */
int defunct1(void)
{
	// Declare variables for part A
	double panel_area, panel_efficiency, solar_radiation_ave, performance_ratio;
	double annual_energy_average;


	// Part A
	// -------

	// Obtain the user input
	cout << "Solar panel area (m^2), A: ";
	cin >> panel_area;

	cout << "Solar panel efficiency, r: ";
	cin >> panel_efficiency;

	cout << "Average Solar Radiation (kWh / m^2), H: ";
	cin >> solar_radiation_ave;

	cout << "Performance Ratio, PR: >> ";
	cin >> performance_ratio;


	// Pass user input to energyCalculator and assign returned valued into energy_generated_annually
	annual_energy_average = energyCalculator(panel_area, panel_efficiency, solar_radiation_ave, performance_ratio);

	// Print out result
	cout << "The average annual solar energy production is " << annual_energy_average << " kWh." << endl;


	// Part B
	// ------
	// Initialize panel efficiency and begin loop
	panel_efficiency = 0.10;
	while (panel_efficiency <= 0.35)
	{
		printEnergy(panel_area, panel_efficiency, solar_radiation_ave, performance_ratio);
		panel_efficiency += 0.05;
	}


	// Part C
	// ------
	double energy_consumption_per_house = 901;
	int number_houses_supported;

	// Obtain the user input
	cout << "Solar panel area (m^2), A: ";
	cin >> panel_area;

	cout << "Solar panel efficiency, r: ";
	cin >> panel_efficiency;

	cout << "Average Solar Radiation (kWh / m^2), H: ";
	cin >> solar_radiation_ave;

	cout << "Performance Ratio, PR: ";
	cin >> performance_ratio;

	// Pass user input to energyCalculator and assign returned valued into energy_generated_annually
	annual_energy_average = energyCalculator(panel_area, panel_efficiency, solar_radiation_ave, performance_ratio);

	// Pass energy calculation and energy consumption per house to calculateNumberHousesSupported
	// and obtain number of houses supported.
	number_houses_supported = calculateNumberHousesSupported(annual_energy_average, energy_consumption_per_house);

	// PRINT out the result of number houses supported
	cout << number_houses_supported << " houses can be supported." << endl;

	return 0;
}



/*
 * Function: energyCalculator
 * --------------------------
 * inputs: panel_area, panel_efficiency, solar_radiation_ave, performance_ratio
 * outputs: energy_average
 * function:
 *     1. Calculates average energy based upon inputs
 *     2. RETURNs the energy calculation to main
 */
double energyCalculator(double panel_area, double panel_efficiency, double solar_radiation_ave, double performance_ratio)
{
	// Declare variable to store energy calculation
	double annual_energy_ave;

	// Calculate energy
	annual_energy_ave = panel_area * panel_efficiency * solar_radiation_ave * performance_ratio;

	// RETURN energy calculation
	return annual_energy_ave;
}



/*
 * Function: printEnergy
 * ---------------------
 * inputs: panel_area, panel_efficiency, solar_radiation_ave, performance_ratio
 * outputs: void
 * function:
 *     1. Calculates average energy based upon inputs
 *     2. PRINTS the output
 *     3. return VOID
 */
void printEnergy(double panel_area, double panel_efficiency, double solar_radiation_ave, double performance_ratio)
{
	// Declare variable to store energy calculation
	double annual_energy_ave;

	// Calculate energy
	annual_energy_ave = panel_area * panel_efficiency * solar_radiation_ave * performance_ratio;

	// Print output
	cout << "The average annual solar energy for an efficiency of " << panel_efficiency
	     << " is " << annual_energy_ave << " kWh." << endl;

	return;
}


/*
 * Function: calculateNumberHousesSupported
 * ----------------------------------------
 * inputs: annual_energy_average, energy_consumption_per_house
 * outputs: houses_supported
 * function:
 *     1. Calculates average energy based upon inputs
 *     2. RETURNs the energy calculation to main
 */
int calculateNumberHousesSupported(double annual_energy_average, double energy_consumption_per_house)
{
	int houses_supported;
	houses_supported = annual_energy_average / energy_consumption_per_house;

	return houses_supported;
}
