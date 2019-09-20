from tkinter import *
from tkinter import filedialog
from math import sin, cos, sqrt, atan2, radians
import csv

root = Tk()
root.configure(background="#31394d")
hs = 0
root.title("Haversine Formula")

def haversine(lat1, long1, lat2, long2):
    dlat = radians(lat2) - radians(lat1)
    dlon = radians(long2) - radians(long1)
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(abs(a)), sqrt(1 - abs(a)))
    distance = 6373.0 * c
    distance = distance * 0.621371
    return distance

def browsefunc(path):
    filename = filedialog.askopenfilename()
    if path == "pathE1":
        pathE1.delete(0, END)
        pathE1.insert(0, filename)
        pathE1.xview(END)
        with open(filename) as FP:
            FP_reader = csv.reader(FP, delimiter=",")
            for row in FP_reader:
                FPLAT.append(float(row[0]))
                FPLONG.append(float(row[1]))
            print(FPLAT)
    elif path == "pathE2":
        pathE2.delete(0, END)
        pathE2.insert(0, filename)
        pathE2.xview(END)
        with open(filename) as SP:
            SP_Reader = csv.reader(SP, delimiter=",")
            for row in SP_Reader:
                SPLAT.append(float(row[0]))
                SPLONG.append(float(row[1]))


def DirPath():
    dirName = filedialog.askdirectory()
    pathE3.delete(0, END)
    pathE3.insert(0, dirName)
    pathE3.xview(END)


def Start_Application():
    csvFile1 = str(pathE3.get()) + "/" + str(ResultFileName.get()) + ".csv"
    bl = False
    Data = open(csvFile1, "w")
    for i in FPLAT:
        for j in SPLAT:
            w = FPLAT[FPLAT.index(i)]
            x = FPLONG[FPLAT.index(i)]
            y = SPLAT[SPLAT.index(j)]
            z = SPLONG[SPLAT.index(j)]
            hs = haversine(w,x,y,z)
            print(hs)
            dbhs=DistanceBox.get()
            if hs < float(dbhs):
                bl = True
                break
        if bl:
            Data.write("Y\n")
            bl = False
        else:
            Data.write("N\n")
    Data.close()


FPLAT = []
FPLONG =[]
SPLAT = []
SPLONG = []

Intro = Label(root, text="Lat/Long Distance Calculator", background="#31394d", font=("Helvetica", 32),
              foreground="white")
Intro.grid(row=0, column=0)

FL = Label(root, text="First Latitude & Longitude Point", background="#31394d", font=("Helvetica", 20),
           foreground="white")
FL.config()
FL.grid(row=1, column=0)

browsebutton = Button(root, text="Browse", highlightbackground="#31394d", command=lambda: browsefunc("pathE1"))
browsebutton.grid(row=2, column=1)

pathE1 = Entry(root)
pathE1.config(width=50)
pathE1.grid(row=2, column=0)

SL = Label(root, text="Second Latitude & Longitude Point", background="#31394d", font=("Helvetica", 20),
           foreground="white")
SL.grid(row=3, column=0)

browsebutton2 = Button(root, text="Browse", highlightbackground="#31394d", command=lambda: browsefunc("pathE2"))
browsebutton2.grid(row=4, column=1)

pathE2 = Entry(root)
pathE2.config(width=50)
pathE2.grid(row=4, column=0)

DT = Label(root, text="Distance Between the Points", background="#31394d", font=("Helvetica", 20), foreground="white")
DT.grid(row=5, column=0)

DistanceBox = Entry(root)
DistanceBox.config(width=10)
DistanceBox.grid(row=6, column=0)

#unit = Checkbutton(root, text="km?", background="#31394d", font=("Helvetica", 14), foreground="white")
#unit.grid(row=6, column=1)

Dir = Label(root, text="Where to Place the Results", background="#31394d", font=("Helvetica", 20), foreground="white")
Dir.grid(row=7, column=0)

pathE3 = Entry(root)
pathE3.config(width=50)
pathE3.grid(row=8, column=0)

browsebutton3 = Button(root, text="Browse", highlightbackground="#31394d", command=lambda: DirPath())
browsebutton3.grid(row=8, column=1)

ResultName = Label(root, text="Result File Name", background="#31394d", font=("Helvetica", 20), foreground="white")
ResultName.grid(row=9, column=0)

ResultFileName = Entry(root)
ResultFileName.config(width=30)
ResultFileName.grid(row=10, column=0)

Submit = Button(root, text="Submit", highlightbackground="#31394d", command=lambda :Start_Application())
Submit.grid(row=11, column=1)


root.mainloop()
