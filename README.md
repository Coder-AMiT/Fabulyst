1. Python code for getting the "Next Trip" time point detail for a "Route" to a "Stop" in a perticular "Direction"

Dependency: Python with requests module.
Command to execute : 
python MetroTransit.py <Route> <Stop> <Direction>
Example :  python MetroTransit.py "METRO Blue Line" "Mall of America Station" "north"
  
  
NOTE : 
1. All the parameters are case senstive, directions are in small case, while route and stops are matching cases with API response. This could be improved by making all cases to lower.
2. Time for next trip is exaclty given as from API response. For some cases it gives in min, else it gives the exact time of next trip. This could be converted in "min" if a current time stamp is available for perticular zone.

