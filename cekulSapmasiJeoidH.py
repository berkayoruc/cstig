
# aLat = Astronomic Latitude  **  eLat = Ellipsoidal Latitude
# aLong = Astronomic Longitude  **  eLong = Ellipsoidal Longitude
# aA = Astronomic Azimuth  **  eA = Ellipsoidal Azimuth
# geoH = Orthometric Heigth  **  ellH = Ellipsoidal Heigth


import math


def degreeConvert2(degree):
    degree1 = int(degree)
    minute = (degree - degree1)*60
    minute1 = int(minute)
    second = round((minute-minute1)*60, 4)
    print(degree1,"degree" ,minute1,"minute" ,second,"second")

def cekBilGeoHei(aLatDeg,aLatMin,aLatSec,aLongDeg,aLongMin,aLongSec,geoH,aADeg,aAMin,aASec,eLatDeg,eLatMin,eLatSec,eLongDeg,eLongMin,eLongSec,ellh,eADeg,eAMin,eASec):
    aLat = aLatDeg + aLatMin/60 + aLatSec/3600
    aLong =  aLongDeg + aLongMin/60 + aLongSec/3600
    aA = aADeg + aAMin / 60 + aASec / 3600
    eA = eADeg + eAMin / 60 + eASec / 3600
    eLat = eLatDeg + eLatMin/60 + eLatSec/3600
    eLong = eLongDeg + eLongMin/60 + eLongSec/3600
    sineLat = math.sin(math.radians(eLat))
    coseLat = math.cos(math.radians(eLat))
    coteLat = coseLat / sineLat

    kisi = aLat - eLat
    itaLamda = (aLong - eLong)*coseLat
    itaAlfa = (aA - eA)*coteLat
    undulation = ellh - geoH

    print("kısi")
    kisi1 = degreeConvert2(kisi)
    print("ita lamda")
    itaLamda1 = degreeConvert2(itaLamda)
    print("ita alfa")
    itaAlfa1 = degreeConvert2(itaAlfa)
    print("undulation: ", undulation, " m")

#cekBilGeoHei(40,27,21.6348,34,52,32.1786,587.218,74,32,56.4819,40,27,35.8741,34,52,23.6714,623.845,74,32,50.9614)