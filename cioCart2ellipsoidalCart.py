import math


def cioCart2ellipsoidalCart(X,Y,Z,X0,Y0,Z0,ex,ey,ez,f0):
    rosec = (180 * 3600) / math.pi
    exx = ex / rosec
    eyy = ey / rosec
    ezz = ez / rosec

    Xp = (1/(1+f0))*(X-X0) - ezz*(Y-Y0) + eyy*(Z-Z0)
    Yp = ezz*(X-X0) + (1/(1+f0))*(Y-Y0) - exx*(Z-Z0)
    Zp = -eyy*(X-X0) + exx*(Y-Y0) + (1/(1+f0))*(Z-Z0)
    print("Xp : ", Xp, " m")
    print("Yp : ", Yp, " m")
    print("Zp : ", Zp, " m")



#cioCart2ellipsoidalCart(3987699.9846, 2778937.0697, 4117697.4796, 135.768, 81.345, 113.928, -2.3, 4.8, 5.6, 0.00000175)