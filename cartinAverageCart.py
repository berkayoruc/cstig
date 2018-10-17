#Cartesian Coordinates in The Average Earth Cartesian System
#A ---> Astronomic Azimuth
#B ---> Measured Zenith without Refraction Correction
#S ---> Spatial Oblique Length
#lat -> Astronomic Latitude
#kp --> Refraction Coefficient

import math

ellipsoidChoices = "Hayford Elipsoidi ---> 1  "  \
                   "WGS84 Elipsoidi ---> 2  "  \
                   "GRS80 Elipsoidi ---> 3  "

while True:
    print(ellipsoidChoices)
    ellipsoid = int(input("Lütfen bir elipsoid seçiniz: "))

    if ellipsoid == 1:
        a = float(6378388)
        b = float(6356911.9461)
        c = float((a * a) / b)
        e2 = float((a * a - b * b) / (a * a))
        e21 = float((a * a - b * b) / (b * b))
        print("******** \nCSTIG 2018\n********")
        break
    elif ellipsoid == 2:
        a = float(6378137)
        b = float(6356752.31424518)
        c = float((a * a) / b)
        e2 = float((a * a - b * b) / (a * a))
        e21 = float((a * a - b * b) / (b * b))
        print("******** \nCSTIG 2018\n********")
        break
    elif ellipsoid == 3:
        a = float(6378137)
        b = float(6356752.3141)
        c = float((a * a) / b)
        e2 = float((a * a - b * b) / (a * a))
        e21 = float((a * a - b * b) / (b * b))
        print("******** \nCSTIG 2018\n********")
        break
    else:
        print("Lütfen geçerli bir karakter giriniz...")
        print("******** \nCSTIG 2018\n********")

def cartinAverageCart(Adeg,Amin,Asec,Bdeg,Bmin,Bsec,S,latDeg,latMin,latSec,longDeg,longMin,longSec,kp,Xp,Yp,Zp,):
    lat = latDeg + latMin / 60 + latSec / 3600
    long = longDeg + longMin / 60 + longSec / 3600
    A = Adeg + Amin / 60 + Asec / 3600
    B = Bdeg + Bmin / 60 + Bsec / 3600
    cosLat = math.cos(math.radians(lat))
    V = math.sqrt(1 + e21 * (cosLat) ** 2)
    N = c / V
    M = c / (V ** 3)
    ro = 180 / math.pi

    sinA = math.sin(math.radians(A))
    cosA = math.cos(math.radians(A))

    Rpk = (M * N) / (N * (cosA ** 2) + M * (sinA ** 2))
    gamapk = (S * ro) / (2 * Rpk)
    deltapk = gamapk * kp
    Bpk = B + deltapk

    sinBpk = math.sin(math.radians(Bpk))
    cosBpk = math.cos(math.radians(Bpk))

    Xkussu = S * sinBpk * cosA
    Ykussu = S * sinBpk * sinA
    Zkussu = S * cosBpk

    print("Xkussu : ", Xkussu, " m")
    print("Ykussu : ", Ykussu, " m")
    print("Zkussu : ", Zkussu, " m")



    cosLat = math.cos(math.radians(lat))
    sinLat = math.sin(math.radians(lat))
    cosLong = math.cos(math.radians(long))
    sinLong = math.sin(math.radians(long))

    Xk = Xp - Xkussu*sinLat*cosLong - Ykussu*sinLong + Zkussu*cosLat*cosLong
    Yk = Yp - Xkussu*sinLat*sinLong + Ykussu*cosLong + Zkussu*cosLat*sinLong
    Zk = Zp + Xkussu*cosLat + Zkussu*sinLat

    print("Xk : ", Xk, " m")
    print("Yk : ", Yk, " m")
    print("Zk : ", Zk, " m")

cartinAverageCart(74,32,56.4819,88,53,25.6,13794.682,40,27,21.6348,34,52,32.1786,0.13,3987699.9846,2778937.0697,4117697.4796)