from math import sin, cos, sqrt, atan2, radians
import csv

def haversine(lat1, long1, lat2, long2):
    dlat = radians(lat2) - radians(lat1)
    dlon = radians(long2) - radians(long1)
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(abs(a)), sqrt(1 - abs(a)))
    distance = 6373.0 * c
    distance = distance * 0.621371
    return distance

UPSLAT = []
UPSLONG =[]
LOCLAT = []
LOCLONG = []

f = 0;
bl = False;


with open("UPS LL.csv") as UPS_LL:
    UPS_LL_reader = csv.reader(UPS_LL,delimiter=",")
    for row in UPS_LL_reader:
        UPSLAT.append(float(row[0]))
        UPSLONG.append(float(row[1]))

with open("Locations GPS.csv") as LOCLL:
    LOCLL_Reader = csv.reader(LOCLL,delimiter=",")
    for row in LOCLL_Reader:
        LOCLAT.append(float(row[0]))
        LOCLONG.append(float(row[1]))

csvFile1 = "Data.csv"
Data = open(csvFile1, "w")

for i in UPSLAT:
    for j in LOCLAT:
        w = UPSLAT[UPSLAT.index(i)]
        x = UPSLONG[UPSLAT.index(i)]
        y = LOCLAT[LOCLAT.index(j)]
        z = LOCLONG[LOCLAT.index(j)]
        f = haversine(w,x,y,z)
        print(f)
        if f < 5:
            bl = True
            break
            print("true")
    if bl:
        Data.write("Y\n")
        bl = False
    else:
        Data.write("N\n")

Data.close()