# completed refactoring from c++
from dataclasses import dataclass

@dataclass
class Truck(object):

    passWeight = 0
    GVWR = 0
    GCWR: int
    payloadCapacity: int
    BedCargoWeight: int
    IntCargoWeight: int

    def __init__(self, gvwr, gcwr, payloadcapacity, passweight, bedcargoweight, intcargoweight):
        self.gvwr = gvwr
        self.gcwr = gcwr
        self.payloadcapacity = payloadcapacity
        self.bedcargoweight = bedcargoweight
        self.intcargoweight = intcargoweight

    def TowCap(self):
        self.towcap = int(self.GCWR) - int(self.GVWR)
        return self.towcap

    def TrkCurbWeight(self):
        self.TCW = int(self.GVWR) - self.payloadCapacity
        return self.TCW
    
    def TotPayLoadNoTrl(self):
        self.PayLoadNoTrl = self.passWeight + self.BedCargoWeight + self.IntCargoWeight
        return self.PayLoadNoTrl

    def TotCurbWeightNoTrl(self):
        self.CurbWeightNoTrl = Truck.TrkCurbWeight(self) + Truck.TotPayLoadNoTrl(self)
        return self.CurbWeightNoTrl
