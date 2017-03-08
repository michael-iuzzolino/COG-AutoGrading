
import math
import numpy as np

# Solution in Python
class SiP(object):

    def __init__(self):
        pass

    def generate_random_parameter_values(self):
        self.A = np.random.randint(1, 50)
        self.r = np.random.uniform()
        self.H = np.random.randint(300, 5000)
        self.PR = np.random.uniform()
        self.energy_consumption_per_house = np.random.randint(100, 2000)



    # Problem 2 - Part A
    def energyCalculator(self):
        self.generate_random_parameter_values()
        return self.A * self.r * self.H * self.PR

    # Problem 2 - Part B
    def printEnergy(self):
        annual_energy_ave = self.energyCalculator()
        return self.r, annual_energy_ave

    # Problem 2 - Part C
    def calculateNumberHousesSupported(self):
        annual_energy_average = self.energyCalculator()
        houses_supported = math.floor(annual_energy_average / self.energy_consumption_per_house)
        return houses_supported;
