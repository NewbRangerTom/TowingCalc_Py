# completed refactoring from c++

class Truck():

    GVWR: int
    GCWR: int
    payloadCapacity: int
    passWeight: int
    BedCargoWeight: int
    IntCargoWeight: int

    def __init__(self, GVWR, GCWR, payloadCapacity, passWeight, BedCargoWeight, IntCargoWeight):
        self.GVWR = GVWR
        self.GCWR = GCWR
        self.payloadCapacity = payloadCapacity
        self.BedCargoWeight = BedCargoWeight
        self.IntCargoWeight = IntCargoWeight

    def TowCap(self):
        self.towcap = int(self.GCWR) - int(self.GVWR)
        return self.towcap

    def TrkCurbWeight(self):
        self.TCW = int(self.GVWR) - int(self.payloadCapacity)
        return self.TCW
    
    def TotPayLoadNoTrl(self):
        self.PayLoadNoTrl = int(self.passWeight) + int(self.BedCargoWeight) + int(self.IntCargoWeight)
        return self.PayLoadNoTrl

    def TotCurbWeightNoTrl(self):
        self.CurbWeightNoTrl = Truck.TrkCurbWeight(self) + Truck.TotPayLoadNoTrl(self)
        return self.CurbWeightNoTrl