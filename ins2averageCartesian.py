import math

def ins2average(Xi,Yi,Zi,xp,yp):
    xpRadyan = (xp/3600)/(180/math.pi)
    ypRadyan = (yp/3600)/(180/math.pi)

    Xa = Xi + xpRadyan*Zi
    Ya = Yi - ypRadyan*Zi
    Za = -xpRadyan*Xi + ypRadyan*Yi + Zi

    print("X (average): ", Xa, " m")
    print("Y (average): ", Ya, " m")
    print("Z (average): ", Za, " m")