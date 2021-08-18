# refactored from c++ 5/21
# refactored to dataclass 7/22/21
# weight of gas 5.9 - 6.5 lbs/gallon
# weight of diesel fuel 7.25 - 7.5 lbs/gallon

from dataclasses import dataclass
import Truck

@dataclass
class DC_Trailer(object):
    
    GVWR: int
    UVW: int
    batteryWeight: int
    waterCapacaity: float
    CargoWeight: int
    AddedFeatureWeight: int
    FuelCapacaity: float
    GenWeight: int
    tonguePercent: str
    fuelType: str
    
    def hitchWeight(self):
        tongueWeightPercent = float(self.tonguePercent)/100.0
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
        self.GroEstWeight = self.UVW + self.batteryWeight + DC_Trailer.waterWeight(self) + self.CargoWeight + self.AddedFeatureWeight + DC_Trailer.FuelWeight(self) + Truck.passWeight + self.GenWeight
        return self.GroEstWeight

    """  Occupant and Cargo Carrying capacity  """
    def OCCC(self):
        self.OCCC = self.GVWR - DC_Trailer.GroEstWeight(self)
        return self.OCCC

    def GCWR(self):
        self.GCWR = self.UVW + DC_Trailer.waterWeight(self) + DC_Trailer.FuelWeight(self)
        return self.GCWR
