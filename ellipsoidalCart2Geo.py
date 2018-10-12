import math

def degreeConvert2(degree):
    degree1 = int(degree)
    minute = (degree - degree1) * 60
    minute1 = int(minute)
    second = round((minute - minute1) * 60, 4)
    print(degree1, "degree", minute1, "minute", second, "second")


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

def ellipsoidalCart2GeoDir(X,Y,Z):
    ro = 180/math.pi
    lamda = math.atan(Y/X)*ro
    p = math.sqrt(X**2 + Y**2)
    tanB = (a/b)*(Z/p)
    B = math.atan(tanB)*ro
    sinB = math.sin(math.radians(B))
    cosB = math.cos(math.radians(B))
    fiatanin = (Z+e21*b*(sinB**3))/(p-e2*a*(cosB**3))
    fi = math.atan(fiatanin)*ro
    cosfi = math.cos(math.radians(fi))
    V = math.sqrt(1 + e21 * (cosfi) ** 2)
    N = c / V
    height = (p/cosfi)-N

    print("Ellipsoidal Latitude")
    degreeConvert2(fi)
    print("Ellipsoidal Longitude")
    degreeConvert2(lamda)
    print("Ellipsoidal Height")
    print(height)

#ellipsoidalCart2GeoDir(3987577.612,2779005.035,4117452.563)

