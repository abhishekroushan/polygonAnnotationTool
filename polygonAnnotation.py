"""
Polygon annotation tool : customizable tool kit for annotating
polygons on the screen (given image or any canvas), along with
feature to store, annotate and load them
The applications of this annotation tool ranges from image processing,
annotation, segmenting, machine learning etc.
Author: Abhishek Roushan abhishek.roushan12@gmail.com
"""

import copy
import tkinter as tk
from PIL import ImageTk, Image
import json
from json import JSONEncoder

class Point2d(object):
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def data(self):
        return self.x, self.y
    def resetToOrigin(self):
        self.x = 0
        self.y = 0

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
            return o.__dict__

class Polygon(object):
    def __init__(self, listOfPoint2d):
        # listOfPoint2d : List[Point2d]
        self.points = listOfPoint2d
    def points(self):
        return self.points
    def addPoint(self, point2d):
        # point2d : Point2d
        self.points.append(point2d)
    def clear(self):
        self.points = []
    def isValid(self):
        if len(self.points)<3: return False
        return True
    def lastPoint(self):
        if len(self.points)==0: 
            print("no points in Polygon")
            return None
        return self.points[-1]
    def firstPoint(self):
        if len(self.points)==0: 
            print("no points in Polygon")
            return None
        return self.points[0]

def printPolygon(polygon):
    polygonStr = json.dumps(polygon, indent=4, cls=CustomEncoder)
    print("debug polygon str = ", polygonStr)
class TextWriter(object):
    def __init__(self, txtFileName:str):
        self.file = txtFileName
    def writePolygonToFile(self, polygon, file):
        # polygon: Polygon, file : File() ptr
        polygonStr = json.dumps(polygon, indent=4, cls=CustomEncoder)
        print("debug polygon str = ", polygonStr)
        file.write(polygonStr+",\n")
    def writePolygonsToFile(self, polygons):
        # polygons : List[Polygon]
        with open(self.file, "a+") as txtFile:
            for i in range(0, len(polygons)):
                self.writePolygonToFile(polygons[i], txtFile)


class Canvas:
    def __init__(self):
        self.C = None
        self.polys = []
        self.currPoly = Polygon([])
    def polygons(self):
        return self.polys
    def create(self):
        top = tk.Tk()
        self.C = tk.Canvas(top, bg="blue", height=400, width=550)
        filename = ImageTk.PhotoImage(Image.open("trees.png")) # using PIL
        image = self.C.create_image(20, 20, anchor="nw", image=filename)
        self.C.bind("<Button-1>", self.drawPolyLine)
        completePolyBtn = tk.Button(top, text='Complete Polygon', width=20,
                     height=5, bd='5', command=self.completePoly)
        completePolyBtn.place(x=10, y=300)

        writeAllPolyBtn = tk.Button(top, text='Write Polygons', width=20,
                                    height=5, bd='5', command=self.writePolygons)
        writeAllPolyBtn.place(x=250, y=300)
        
        self.C.pack()
        top.mainloop()
    def drawPolyLine(self, event):
        x,y = self.getCoordinate(event)
        lp = self.currPoly.lastPoint()
        if lp is not None:
            # add x,y to self.currPoly and create a line from last point
            lpx, lpy = lp.data()
            self.C.create_line(lpx, lpy, x, y, width=3)
        # create currPoly with new point from x,y
        self.currPoly.addPoint(Point2d(x,y))
    def completePoly(self):
        fp = self.currPoly.firstPoint()
        if fp is None:
            print("can't complete current Polygon. try adding more points")
        else:
            if not self.currPoly.isValid():
                print("can't complete current Polygon. try adding more points")
                return
            fpx, fpy = fp.data()
            lp = self.currPoly.lastPoint()
            lpx, lpy = lp.data() # directly query data since self.currPoly is valid
            self.C.create_line(lpx, lpy, fpx, fpy, width=3)
            self.polys.append(copy.deepcopy(self.currPoly))
            self.currPoly.clear()
            print("current Polygon completed, and added to Canvas polygons")
            print("total polygons = ", len(self.polygons()))
            printPolygon(self.polygons()[0])
    def getCoordinate(self, event):
        x = event.x
        y = event.y
        print("clicked at x=", x, ", y=", y)
        return x,y
    def writePolygons(self):
        polys = self.polygons()
        print("total polygons = ", len(self.polygons()))
        printPolygon(self.polygons()[0])
        txtFileName = "./data.txt"
        writer = TextWriter(txtFileName)
        writer.writePolygonsToFile(polys)
        print("Polygons written to file:", txtFileName)



