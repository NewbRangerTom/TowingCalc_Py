""" Punch List:
  1. add error check for invalid input to all input variables
"""
import Truck
import Trailer

myTruck = Truck
myTrailer = Trailer

print("Towing Calculator v3.7.29.2021 python")
print('update v8.25.2021')
print("User assumes all risk when using this program.\nIt is the USER's responsibility to verify all weight capacities\nand limits of vehicle and cargo before towing anything.\n")
##### !!!! BEGIN TRUCK INPUT !!!! #####

while True:
    myTruck.GVWR = input('\nEnter truck Gross Vehicle Weight Rating (GVWR): ')
    if myTruck.GVWR == '' or int(myTruck.GVWR) == 0 or int(myTruck.GVWR) < 0:
        print('GVWR can not be blank, less than 0, or 0.')
        continue
    elif int(myTruck.GVWR) > 0:
        break

#while True:
#    myTruck.GVWR = input('\nEnter truck gross Vehicle Weight Rating (GVWR): ')
#    try:
#        myTruck.GVWR = int(myTruck.GVWR) + 0
#    except:
#        print('GVWR can not be blank or non digit characters')
#        continue
#    if int(myTruck.GVWR) <= 0:
#        print('GVWR must be greater than 0.')
#        continue

while True:
    myTruck.GCWR = input("\nEnter truck Gross Combined Weight Rating (GCWR): ")
    if myTruck.GCWR == '' or int(myTruck.GCWR) == 0 or int(myTruck.GCWR) <0:
        print('GCWR can not be blank, less than 0, or 0.')
        continue
    elif int(myTruck.GCWR) > 0:
        break

while True:
    myTruck.payloadCapacity = input("\nEnter truck payload capacity: ")
    if myTruck.payloadCapacity == '' or int(myTruck.payloadCapacity) == 0 or int(myTruck.payloadCapacity) < 0:
        print('Payload Capacity can not be blank, less than 0, or 0.')
        continue
    elif int(myTruck.payloadCapacity) > 0:
        myTruck.payloadCapacity = int(myTruck.payloadCapacity)
        break

while True:
    myTruck.BedCargoWeight = input("\nHow much does the bed cargo weight (press ENTER for 0): ")
    if myTruck.BedCargoWeight == '':
        myTruck.BedCargoWeight = 0
        print('Value set to 0.')
        break
    elif int(myTruck.BedCargoWeight) < 0:
        print('Bed Cargo Weight can not be less than 0.')
        continue
    elif int(myTruck.BedCargoWeight) >= 0:
        break

while True:
    myTruck.passWeight = input("\nHow much do the driver and all passengers weight: ")
    if myTruck.passWeight == '' or int(myTruck.passWeight) == 0 or int(myTruck.passWeight) < 0:
        print('Passenger Weight includes driver and can not be blank, less than 0, or 0.')
        continue
    elif int(myTruck.passWeight) > 0:
        break

while True:
    myTruck.IntCargoWeight = input("\nHow much does the interior cargo weight: ")
    if myTruck.IntCargoWeight == '':
        myTruck.IntCargoWeight = 0
        print('Value set to 0.')
        break
    elif int(myTruck.IntCargoWeight) < 0:
        print('Interior cargo weight can not be less than 0.')
        continue
    elif int(myTruck.IntCargoWeight) >= 0:
        break

##### !!!! BEGIN TRAILER INPUT !!!! ####
print("\nTrailer info:")


while True:
    myTrailer.GVWR = input("\nEnter trailer GVWR (the maximum fully loaded weight of the trailer): ")
    if myTrailer.GVWR == '' or int(myTrailer.GVWR) == 0 or int(myTrailer.GVWR) < 0:
        print('GVWR can not be blank, less than 0, or 0.')
        continue
    elif int(myTrailer.GVWR) > 0:
        break

while True:
    myTrailer.UVW = input("\nEnter trailer Unloaded Vehicle Weight (UVW): ")
    if myTrailer.UVW == '' or int(myTrailer.UVW) == 0 or int(myTrailer.UVW) < 0:
        print('UVW can n ot be blank, less than 0, or 0.')
        continue
    elif int(myTrailer.UVW) > 0:
        break

while True:
    myTrailer.tonguePercent = input('\nEnter the tongue weight perecentage (if not available press "Enter" to use default value): ')
    if myTrailer.tonguePercent == '':
        myTrailer.tonguePercent = 12.5
        print('Default value 12.5 accepted')
        break
    elif float(myTrailer.tonguePercent) > 0.0:
        break
    elif int(myTrailer.tonguePercent) == 0:
        print('Percentage can not be 0')
        continue

while True:
    myTrailer.CargoWeight = input("\nEnter trailer cargo weight: ")
    if myTrailer.CargoWeight == '':
       myTrailer.CargoWeight = 0
       print('weight set to 0.')
       break
    elif int(myTrailer.CargoWeight) < 0:
        print('Cargo weight can not be less than 0.')
        continue
    elif int(myTrailer.CargoWeight) >= 0:
        break

while True:
    myTrailer.AddedFeatureWeight = input("\nEnter weight of any added features: ")
    if myTrailer.AddedFeatureWeight == '': 
        myTrailer.AddedFeatureWeight = 0
        print('weight set to 0.')
        break
    elif int(myTrailer.AddedFeatureWeight) < 0:
        print('Added features weight can not be less than 0.')
        continue
    elif int(myTrailer.AddedFeatureWeight) >= 0:
        break

while True:
    myTrailer.batteryWeight = input("\nEnter trailer battery weight (if equipped): ")
    if myTrailer.batteryWeight == '':
        myTrailer.batteryweight = 0
        print('weight set to 0.')
        break
    elif int(myTrailer.batteryWeight) < 0:
        print('Battery weight can not be less than 0.')
        continue
    elif int(myTrailer.batteryWeight) >= 0:
        break

while True:
    myTrailer.waterCapacity = input("\nEnter water capacity (of water heater and water tank) in gallons: ")
    if myTrailer.waterCapacity == '':
       myTrailer.waterCapacity = 0
       print('Capaity set to 0.')
       break
    elif int(myTrailer.waterCapacity) < 0:
        print('Water capacity can not be less than 0.')
        continue
    elif int(myTrailer.waterCapacity) >= 0:
        break

fuel_type = input('\nEnter 1 or 2 for fuel type: \n 1. Regular \n 2. Diesel \n')

if fuel_type == '1' :
    myTrailer.fuelType = 'regular'
if fuel_type == '2' :
    myTrailer.fuelType = 'diesel'

while True:
    myTrailer.FuelCapacity = input("\nEnter the trailer fuel capacity (cans and or generators): ")
    if myTrailer.FuelCapacity == '':
        myTrailer.FuelCapacity = 0
        print('Capacity set to 0.')
        break
    elif int(myTrailer.FuelCapacity) < 0:
        print('Fuel capacity can not be less than 0.')
        continue
    elif int(myTrailer.FuelCapacity) >= 0:
        break

while True:
    myTrailer.GenWeight = input("\nEnter the weight of generator(s) (if loaded on/in trailer): ")
    if myTrailer.GenWeight == '':
       myTrailer.GenWeight = 0
       print('Weight set to 0.')
       break
    elif int(myTrailer.GenWeight) < 0:
        print('Generator weight can not be blank or less than 0.')
        continue
    elif int(myTrailer.GenWeight) >= 0:
        break

##### !!!! BEGIN TRUCK OUTPUT !!!! #####
print("\n##!!  RESULTS  !!##")
print("The Towing Capacity is:",(myTruck.Truck.TowCap(Truck)),"lbs.")
print("The empty curb weight of the truck is (GVWR - payload capacity):",(myTruck.Truck.TrkCurbWeight(Truck)),"lbs.")
print("The total weight of passengers and cargo is:",(myTruck.Truck.TotPayLoadNoTrl(Truck)),"lbs.")
print("The loaded curb weight of the truck is:",(myTruck.Truck.TotCurbWeightNoTrl(Truck)),"lbs.")
if myTruck.payloadCapacity - (myTruck.Truck.TotPayLoadNoTrl(Truck) + myTrailer.Trailer.hitchWeight(Trailer)) > 0:
     print("The available payload of your truck is:",round(myTruck.payloadCapacity - (myTruck.Truck.TotPayLoadNoTrl(Truck) + myTrailer.Trailer.hitchWeight(Trailer)),2),"lbs.")
else :
    print("Your truck is overloaded by:",round(abs(myTruck.payloadCapacity - (myTruck.Truck.TotPayLoadNoTrl(Truck) + myTrailer.Trailer.hitchWeight(Trailer))),2),"lbs.")

##### !!!!! BEGIN TRAILER OUTPUT !!!!! #####
print("The hitch weight of the trailer is:", round(myTrailer.Trailer.hitchWeight(Trailer),2),"lbs.")
print("The gross estimated weight of the trailer is:", myTrailer.Trailer.GroEstWeight(Trailer, int(myTruck.passWeight)),"lbs.")

if (int(myTrailer.GVWR) - (myTrailer.Trailer.GroEstWeight(Trailer, int(myTruck.passWeight)))) > 0 :
    print("The trailer Occupant and Cargo Carrying capacity has", round(int(myTrailer.GVWR) - (myTrailer.Trailer.GroEstWeight(Trailer, int(myTruck.passWeight))), 2), "more lbs before it is overloaded.")
else :
    print("The OCCC is:",round(abs(int(myTrailer.GVWR) - (myTrailer.Trailer.GroEstWeight(Trailer, int(myTruck.passWeight)))), 2), "lbs overweight.")

print("\nThe truck payload with the trailer is:", (myTruck.Truck.TotPayLoadNoTrl(Truck) + myTrailer.Trailer.hitchWeight(Trailer)), "lbs.")
if (myTruck.Truck.TowCap(Truck) - myTruck.payloadCapacity) + myTrailer.Trailer.GroEstWeight(Trailer, int(myTruck.passWeight)) > 0 :
    print("The theorhetical Remaining Towing Capacity is:", (myTruck.Truck.TowCap(Truck) - myTruck.payloadCapacity) + myTrailer.Trailer.GroEstWeight(Trailer, int(Truck.passWeight)), "lbs.")
else :
    print("Your towing capacity is overloaded by:",(myTruck.Truck.TowCap(Truck) - myTruck.payloadCapacity) + myTrailer.Trailer.GroEstWeight(Trailer, int(Truck.passWeight)),"lbs.")

print("\nThe combined weight of the truck and trailer is:", (myTruck.Truck.TotCurbWeightNoTrl(Truck) + myTrailer.Trailer.GroEstWeight(Trailer, int(Truck.passWeight)) - int(myTruck.passWeight)),"lbs.")
print("\nEnd of results.\n")