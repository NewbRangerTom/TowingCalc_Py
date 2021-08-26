**updated 8-26-21
**repo created 8-18-21  
**code refactored from C++ 5-21  

# TowingCalc_Py  

## python based towing calculator  

*!!** DISCLAIMER **!!*  
This is a learning project meant to give me a better understanding of Python and how Python works.  
This code is meant to change and grow as my knowledge and experience grows.  

TowingCalc_Py  
- This is the main source code file.
- Takes user input for variables
- Calls methods to calculate and output results

Truck class to handle truck variabls and specific functions.  
- The Truck class defines the required weights for the users specific vehicle.  
- The Truck class has four methods for calculating:  
  - towing capacity  
  - curb weight  
  - total payload without trailer  
  - total payload with trailer  

Trailer class to handle trailer variabls and specific functions.  
- The Trailer class defines the required weights for the users specific trailer.  
- The Trailer class has six methods for calculating:  
  - hitch weight  
  - fuel weight  
  - water weight  
  - gross estimated weight  
  - occupant and cargo carrying capacity  
  - gross combined weight rating  

REMOVED 8-26-2021 - Trailer class was sufficient so removed redundant class  
DC_Trailer class is a dataclass refactoring of the Trailer class.  
- Refactored from Tralier class 7-22-21  
- The DC_Trailer dataclass defines the required weights for the users specific trailer.  
  - The Trailer class has six methods for calculating:  
  - hitch weight  
  - fuel weight  
  - water weight  
  - gross estimated weight  
  - occupant and cargo carrying capacity  
  - gross combined weight rating  

REMOVED 8-26-2021 - went a different route for exception handling  
Validate class is an unfinished exception handler.  
** This will probably get refactored or rewritten as a basic function.  
- The Validate class has two methods for handling exceptions.  
  - dis-allow zero  
  - allow zero  
  
created 8-18-21
