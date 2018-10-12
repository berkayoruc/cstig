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
        e21 = float((a * a - b * b) / (b * b))
        print("******** \nCSTIG 2018\n********")
        break
    elif ellipsoid == 2:
        a = float(6378137)
        b = float(6356752.31424518)
        c = float((a * a) / b)
        e21 = float((a * a - b * b) / (b * b))
        print("******** \nCSTIG 2018\n********")
        break
    elif ellipsoid == 3:
        a = float(6378137)
        b = float(6356752.3141)
        c = float((a * a) / b)
        e21 = float((a * a - b * b) / (b * b))
        print("******** \nCSTIG 2018\n********")
        break
    else:
        print("Lütfen geçerli bir karakter giriniz...")
        print("******** \nCSTIG 2018\n********")


def ellipsoidalGeo2Cart(fideg,fimin,fisec,lamdadeg,lamdamin,lamdasec,height):

    fidegree = fideg + fimin/60 + fisec/3600
    lamdadegree = lamdadeg + lamdamin/60 + lamdasec/3600

    cosfidegree = math.cos(math.radians(fidegree))
    sinfidegree = math.sin(math.radians(fidegree))
    coslamdadegree = math.cos(math.radians(lamdadegree))
    sinlamdadegree = math.sin(math.radians(lamdadegree))

    if ellipsoid == 1:
        print("Hayford Elipsoidi Parametreleri")
    elif ellipsoid == 2:
        print("WGS84 Elipsoidi Parametreleri")
    elif ellipsoid == 3:
        print("GRS80 Elipsoidi Parametreleri")

    print("a =", a, "b =", b, "c =", c, "e2 =", e2, "e21 =", e21)
    print("******** \n\n********")

    V = math.sqrt(1 + e21 * (cosfidegree) ** 2)
    N = c / V

    X = (N+height)*cosfidegree*coslamdadegree
    Y = (N+height)*cosfidegree*sinlamdadegree
    Z = (((b/a)**2)*N+height)*sinfidegree

    print("X : ", X, " m")
    print("Y : ", Y, " m")
    print("Z : ", Z, " m")

#ellipsoidalGeo2Cart(40,27,35.8741,34,52,23.6714,623.845)