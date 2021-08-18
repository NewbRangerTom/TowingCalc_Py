
"""  This Class has been depricated by DC_Trailer.py.  Either class file can be used.  """

# refactoring from c++
# weight of gas 5.9 - 6.5 lbs/gallon
# weight of diesel fuel 7.25 - 7.5 lbs/gallon

from Truck import Truck
class Trailer():
    fuelType: str

    def __init__(self, GVWR, UVW, batteryWeight, waterCapacity, CargoWeight, AddedFeatureWeight, FuelCapacity, fueldType, GenWeight, tonguePercent):
        self.GVWR = int(GVWR)
        self.UVW = int(UVW)
        self.batteryWeight = int(batteryWeight)
        self.waterCapacity = float(waterCapacity)
        self.CargoWeight = int(CargoWeight)
        self.AddedFeatureWeight = int(AddedFeatureWeight)
        self.FuelCapacity = float(FuelCapacity)
        self.GenWeight = int(GenWeight)
        self.tonguePercent = float(tonguePercent)
        self.fuelType = fuelType
    
    def hitchWeight(self):
        tongueWeightPercent = self.tonguePercent/100
        self.hitchWeight = (self.GVWR * tongueWeightPercent)
        return self.hitchWeight

    def FuelWeight(self):
        if fuelType == 'diesel' or fuelType == 'Diesel' or fuelType == 'DIESEL' or fuelType == 'D' or fuelType == 'd' :
            self.FuelWeight = self.FuelCapacity * 7.375
            return self.FuelWeight
        elif fuelType == "" or fuelType is None : 
            self.FuelWeight = 0
            return self.FuelWeight
        else :
            self.FuelWeight = self.FuelCapacity * 6.2
            return self.FuelWeight

    def waterWeight(self):
        self.waterWeight = self.waterCapacity * 8.34
        return self.waterWeight
        
    def GroEstWeight(self, passWeight):  # uvw, bettery water cargo feature genweight fuelweight
        self.GroEstWeight = self.UVW + self.batteryWeight + Trailer.waterWeight(self) + self.CargoWeight + self.AddedFeatureWeight + Trailer.FuelWeight(self) + Truck.passWeight + self.GenWeight
        return self.GroEstWeight

    """  Occupant and Cargo Carrying capacity  """
    def OCCC(self):
        self.OCCC = self.GVWR - Trailer.GroEstWeight(self)
        return self.OCCC

    def GCWR(self):
        self.GCWR = self.UVW + self.waterWeight(self) + self.FuelWeight(self)
        return self.GCWR