# refactoring from c++
# weight of gas 5.9 - 6.5 lbs/gallon
# weight of diesel fuel 7.25 - 7.5 lbs/gallon

from Truck import Truck
class Trailer():
    
    GVWR = 0
    UVW: int
    batteryWeight: int
    waterCapacaity = 0.0
    CargoWeight: int
    AddedFeatureWeight: int
    FuelCapacaity: float
    GenWeight: int
    tonguePercent: float
    fuelType: str

    def __init__(self, GVWR, UVW, batteryWeight, waterCapacity, CargoWeight, AddedFeatureWeight, FuelCapacity, fuelType, GenWeight, tonguePercent):
        self.GVWR = GVWR
        self.UVW = UVW
        self.batteryWeight = batteryWeight
        self.waterCapacity = waterCapacity
        self.CargoWeight = CargoWeight
        self.AddedFeatureWeight = AddedFeatureWeight
        self.FuelCapacity = FuelCapacity
        self.GenWeight = GenWeight
        self.tonguePercent = tonguePercent
        self.fuelType = fuelType
    
    def hitchWeight(self):
        tongueWeightPercent = float(self.tonguePercent)/100
        self.hitchWeight = float(self.GVWR) * tongueWeightPercent
        return self.hitchWeight

    def FuelWeight(self):
        #if fuelType == 'diesel' or fuelType == 'Diesel' or fuelType == 'DIESEL' or fuelType == 'D' or fuelType == 'd' :
        if fuelType == 'diesel' :
            self.FuelWeight = float(self.FuelCapacity) * 7.375
            return self.FuelWeight
        elif fuelType == "" or fuelType is None : 
            self.FuelWeight = 0
            return self.FuelWeight
        else :
            self.FuelWeight = float(self.FuelCapacity) * 6.2
            return self.FuelWeight

    def waterWeight(self):
        self.waterWeight = float(self.waterCapacity) * 8.34
        return self.waterWeight
        
    def GroEstWeight(self, passWeight):  # uvw, bettery water cargo feature genweight fuelweight
        self.GroEstWeight = int(self.UVW) + int(self.batteryWeight) + Trailer.waterWeight(self) + int(self.CargoWeight) + int(self.AddedFeatureWeight) + Trailer.FuelWeight(self) + int(passWeight) + int(self.GenWeight)
        return self.GroEstWeight

    """  Occupant and Cargo Carrying capacity  """
    def OCCC(self):
        self.OCCC = int(self.GVWR) - Trailer.GroEstWeight(self)
        return self.OCCC

    def GCWR(self):
        self.GCWR = int(self.UVW) + Trailer.waterWeight(self) + Trailer.FuelWeight(self)
        return self.GCWR