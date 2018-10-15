import math

def ellipsoidalCart2CIOCart(Xp,Yp,Zp,X0,Y0,Z0,ex,ey,ez,f0):

    rosec = (180*3600) / math.pi
    exx = ex/rosec
    eyy = ey/rosec
    ezz = ez/rosec

    X = X0 + (1+f0)*Xp + ezz*Yp - eyy*Zp
    Y = Y0 - ezz*Xp + (1+f0)*Yp + exx*Zp
    Z = Z0 + eyy*Xp - exx*Yp + (1+f0)*Zp

    print("X : ", X, " m")
    print("Y : ", Y, " m")
    print("Z : ", Z, " m")

ellipsoidalCart2CIOCart(3987577.612,2779005.035,4117452.563,135.768,81.345,113.928,-2.3,4.8,5.6,0.00000175)
