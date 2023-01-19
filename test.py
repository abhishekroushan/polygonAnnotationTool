"""
Test file for Polygon annotation tool : customizable tool kit for annotating
polygons on the screen (given image or any canvas), along with
feature to store, annotate and load them
Author: Abhishek Roushan abhishek.roushan12@gmail.com
"""

from polygonAnnotation import *


def testPolygonsWrite():
    txtFileName = "./data.txt"
    writer = TextWriter(txtFileName)
    polygons = [Polygon([Point2d(0,0), Point2d(1,0), Point2d(0,1)]),
                Polygon([Point2d(-3.4,5), Point2d(5,7), Point2d(6.7,2.1), Point2d(4.33, 5.1)])]
    writer.writePolygonsToFile(polygons)


testPolygonsWrite()


