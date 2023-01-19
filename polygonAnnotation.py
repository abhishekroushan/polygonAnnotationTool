"""
Polygon annotation tool : customizable tool kit for annotating
polygons on the screen (given image or any canvas), along with
feature to store, annotate and load them
The applications of this annotation tool ranges from image processing,
annotation, segmenting, machine learning etc.
Author: Abhishek Roushan abhishek.roushan12@gmail.com
"""

import json
from json import JSONEncoder

class Point2d(object):
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def data(self):
        return x, y
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

class TextWriter(object):
    def __init__(self, txtFileName:str):
        self.file = txtFileName
    def writePolygonToFile(self, polygon, file):
        # polygon: Polygon, file : File() ptr
        polygonStr = json.dumps(polygon, indent=4, cls=CustomEncoder)
        file.write(polygonStr+",\n")
    def writePolygonsToFile(self, polygons):
        # polygons : List[Polygon]
        with open(self.file, "a+") as txtFile:
            for i in range(0, len(polygons)):
                self.writePolygonToFile(polygons[i], txtFile)



