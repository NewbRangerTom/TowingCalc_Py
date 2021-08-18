""" Punch List:
  1. add error check for invalid input to all input variables
"""
import validate
import Truck
import DC_Trailer  # a dataclass version of the Trailer class
"""  Trailer.py Class has been depricated by DC_Trailer.py.  Either class file can be used.  """
#import Trailer    # to use Trailer class, be sure to change all instances of DC_Trailer to Trailer

myTruck = Truck
myTrailer = DC_Trailer

print("Towing Calculator v3.7.29.2021 python")
print("User assumes all risk when using this program.\nIt is the USER's responsibility to verify all weight capacities\nand limits of vehicle and cargo before towing anything.\n")
##### !!!! BEGIN TRUCK INPUT !!!! #####

while True:
    myTruck.GVWR = input('\nEnter truck Gross Vehicle Weight Rating (GVWR): ')
    if myTruck.GVWR == '':
        print('GVWR can not be blank')
        continue
    elif int(myTruck.GVWR) == 0:
        print('GVWR can not be 0')
        continue
    elif int(myTruck.GVWR) > 0:
        break

while True:
    myTruck.GCWR = input("\nEnter truck Gross Combined Weight Rating (GCWR): ")
    if myTruck.GCWR == '':
        print('GCWR can not be blank')
        continue
    elif int(myTruck.GCWR) == 0:
        print('GCWR can not be 0')
        continue
    elif int(myTruck.GCWR) > 0:
        break

myTruck.payloadCapacity = int(input("\nEnter truck payload capacity: "))

myTruck.BedCargoWeight = int(input("\nHow much does the bed cargo weight: "))

myTruck.passWeight = int(input("\nHow much do the driver and all passengers weight: "))

myTruck.IntCargoWeight = int(input("\nHow much does the interior cargo weight: "))

##### !!!! BEGIN TRAILER INPUT !!!! ####
print("\nTrailer info:")

myTrailer.GVWR = int(input("\nEnter trailer GVWR (the maximum fully loaded weight of the trailer): "))

myTrailer.UVW = int(input("\nEnter trailer Unloaded Vehicle Weight (UVW): "))

while True:
    myTrailer.tonguePercent = input("\nEnter the tongue weight perecentage (if not available use 12.5): ")
    if myTrailer.tonguePercent == '':
        print('Default value 12.5 accepted')
        myTrailer.tonguePercent = 12.5
        float(myTrailer.tonguePercent)
        break
    elif float(myTrailer.tonguePercent) > 0.0:
        float(myTrailer.tonguePercent)
        break
    elif int(myTrailer.tonguePercent) == 0:
        print('Percentage can not be 0')
        continue

myTrailer.CargoWeight = int(input("\nEnter trailer cargo weight: "))

myTrailer.AddedFeatureWeight = int(input("\nEnter weight of any added features: "))

myTrailer.batteryWeight = int(input("\nEnter trailer battery weight (if equipped): "))

myTrailer.waterCapacity = int(input("\nEnter water capacity (of water heater and water tank) in gallons: "))

myTrailer.fuelType = input("\nEnter the type of fuel (diesel or regular): ")

myTrailer.FuelCapacity = int(input("\nEnter the trailer fuel capacity (cans and or generators): "))

myTrailer.GenWeight = int(input("\nEnter the weight of generator(s) (if loaded on/in trailer): "))

##### !!!! BEGIN TRUCK OUTPUT !!!! #####
print("\n##!!  RESULTS  !!##")
print("The Towing Capacity is:",(myTruck.Truck.TowCap(Truck)),"lbs.")
print("The empty curb weight of the truck is (GVWR - payload capacity):",(myTruck.Truck.TrkCurbWeight(Truck)),"lbs.")
print("The total weight of passengers and cargo is:",(myTruck.Truck.TotPayLoadNoTrl(Truck)),"lbs.")
print("The loaded curb weight of the truck is:",(myTruck.Truck.TotCurbWeightNoTrl(Truck)),"lbs.")
if ((myTruck.payloadCapacity) - (myTruck.Truck.TotPayLoadNoTrl(Truck) + myTrailer.DC_Trailer.hitchWeight(DC_Trailer))) > 0:
     print("The available payload of your truck is:",round(((myTruck.payloadCapacity) - (myTruck.Truck.TotPayLoadNoTrl(Truck) + myTrailer.DC_Trailer.hitchWeight(DC_Trailer))),2),"lbs.")
else :
    print("Your truck is overloaded by:",round(abs((myTruck.payloadCapacity) - (myTruck.Truck.TotPayLoadNoTrl(Truck) + myTrailer.DC_Trailer.hitchWeight(DC_Trailer))),2),"lbs.")

##### !!!!! BEGIN TRAILER OUTPUT !!!!! #####
print("The hitch weight of the trailer is:", round(myTrailer.DC_Trailer.hitchWeight(DC_Trailer),2),"lbs.")
print("The gross estimated weight of the trailer is:", myTrailer.DC_Trailer.GroEstWeight(DC_Trailer, myTruck.Truck.passWeight),"lbs.")

if ((myTrailer.GVWR) - (myTrailer.DC_Trailer.GroEstWeight(DC_Trailer, Truck.passWeight))) > 0 :
    print("The trailer Occupant and Cargo Carrying capacity has", round((myTrailer.GVWR) - (myTrailer.DC_Trailer.GroEstWeight(DC_Trailer, Truck.passWeight)), 2), "more lbs before it is overloaded.")
else :
    print("The OCCC is:",round(abs((myTrailer.GVWR) - (myTrailer.DC_Trailer.GroEstWeight(DC_Trailer, Truck.passWeight))), 2), "lbs overweight.")

print("\nThe truck payload with the trailer is:", (myTruck.Truck.TotPayLoadNoTrl(Truck) + myTrailer.DC_Trailer.hitchWeight(DC_Trailer)), "lbs.")
if (myTruck.Truck.TowCap(Truck) - myTruck.payloadCapacity) + (myTrailer.DC_Trailer.GroEstWeight(DC_Trailer, Truck.passWeight)) > 0 :
    print("The theorhetical Remaining Towing Capacity is:", (myTruck.Truck.TowCap(Truck) - myTruck.payloadCapacity) + (myTrailer.DC_Trailer.GroEstWeight(DC_Trailer, Truck.passWeight)), "lbs.")
else :
    print("Your towing capacity is overloaded by:",(myTruck.Truck.TowCap(Truck) - myTruck.payloadCapacity) + (myTrailer.DC_Trailer.GroEstWeight(DC_Trailer, Truck.passWeight)),"lbs.")

print("\nThe combined weight of the truck and trailer is:", (myTruck.Truck.TotCurbWeightNoTrl(Truck) + myTrailer.DC_Trailer.GroEstWeight(DC_Trailer, Truck.passWeight) - myTruck.passWeight),"lbs.")
print("\nEnd of results.\n")