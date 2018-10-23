Python code for getting the "Next Trip" time point detail for a "Route" to a "Stop" in a perticular "Direction"

Dependency: 
Python with requests module.

Command to execute :

python MetroTransit.py Route Stop Direction
  
Example :  python MetroTransit.py "METRO Blue Line" "Mall of America Station" "north"
  
  
NOTE : 

1. Time for next trip is exaclty given as from API response. For some cases it gives in min, else it gives the exact time of next trip. This could be converted in "min" if a current time stamp is available for perticular zone.
2. In case of wrong params, like wrong direction or route, or in case of no data or no available next trip. it will print "None", this could be given as proper messages if needed.
3. It works now with Substring of route or stop.
4. Case Insensitive matching implemented. 

