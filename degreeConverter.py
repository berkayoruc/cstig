def degreeConvert(degree, minute, second):
    degree1 = degree + minute / 60 + second / 3600
    print(degree1, " degree")


def degreeConvert2(degree):
    degree1 = int(degree)
    minute = (degree - degree1) * 60
    minute1 = int(minute)
    second = round((minute - minute1) * 60, 4)
    print(degree1, "degree", minute1, "minute", second, "second")