import math

def average2ins(Xa,Ya,Za,xp,yp):
    xpRadyan = (xp / 3600) / (180 / math.pi)
    ypRadyan = (yp / 3600) / (180 / math.pi)

    Xi = Xa - xpRadyan * Za
    Yi = Ya + ypRadyan * Za
    Zi = xpRadyan * Xa - ypRadyan * Ya + Za

    print("X (instantaneous): ", Xi, " m")
    print("Y (instantaneous): ", Yi, " m")
    print("Z (instantaneous): ", Zi, " m")