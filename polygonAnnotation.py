"""
Polygon annotation tool : customizable tool kit for annotating
polygons on the screen (given image or any canvas), along with
feature to store, annotate and load them
The applications of this annotation tool ranges from image processing,
annotation, segmenting, machine learning etc.
Author: Abhishek Roushan abhishek.roushan12@gmail.com
"""

import os

class Point2d(object):
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
    def data(self):
        return x, y
    def resetToOrigin(self):
        self.x = 0
        self.y = 0

class Polygon(object):
    def __init__(self):
        self.points = [] # List[Point2d]
    def points(self):
        return self.points
    def addPoint(self, point2d):
        # point2d : Point2d
        self.points.append(point2d)
    def clear(self):
        self.points = []
    def setPoints(self, listOfPoint2d):
        # listOfPoint2d : List[Point2d]
        self.points = listOfPoint2d

class TextWriter(object):
    def __init__(self, txtFileName:str):
        self.file = txtFileName
    def writePolygonToFile(self, polygon):
        # polygon: Polygon
        pass
    def writePolygonsToFile(self, polygons):
        # polygons : List[Polygon]
        ## write "{\n"
        for i in range(0, len(polygons)):
            writePolygonToFile(polygons[i])
        ## write "}\n"



