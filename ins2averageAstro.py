import math

def degreeConvert2(degree):
    degree1 = int(degree)
    minute = (degree - degree1) * 60
    minute1 = int(minute)
    second = round((minute - minute1) * 60, 4)
    print(degree1, "degree", minute1, "minute", second, "second")

def ins2averageAstro(LatDeg,LatMin,LatSec,LongDeg,LongMin,LongSec,ADeg,AMin,ASec,xp,yp):
    lati = LatDeg + LatMin/60 + LatSec/3600
    longi = LongDeg + LongMin/60 + LongSec/3600
    ai = ADeg + AMin / 60 + ASec / 3600

    xpDeg = xp/3600
    ypDeg = yp/3600

    lata = lati + ypDeg*math.sin(math.radians(longi)) - xpDeg*math.cos(math.radians(longi))
    longa = longi - (xpDeg*math.sin(math.radians(longi)) + ypDeg*math.cos(math.radians(longi)))*math.tan(math.radians(lati))
    aa = ai - (xpDeg*math.sin(math.radians(longi)) + ypDeg*math.cos(math.radians(longi)))*(1/math.cos(math.radians(lati)))

    print("Average Astronomic Latitude")
    degreeConvert2(lata)
    print("Average Astronomic Longitude")
    degreeConvert2(longa)
    print("Average Astronomic Azimuth")
    degreeConvert2(aa)