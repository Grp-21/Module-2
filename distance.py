#pip install haversine
import haversine as hs
from haversine import Unit

# loc1 and loc2 are the two tuple containing geocordinates
# Example
# loc1=(28.426846,77.088834)
# loc2=(28.394231,77.050308)

def DistanceMeters(loc1,loc2):
    return hs.haversine(loc1,loc2,unit=Unit.METERS)

loc1=(28.426846,77.088834)
loc2=(28.394231,77.050308)

#Function calling example
eg= DistanceMeters(loc1, loc2)

print(eg)