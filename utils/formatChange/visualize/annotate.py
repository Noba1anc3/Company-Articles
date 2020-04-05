
from utils.formatChange.coordinateChange import *

import cv2

class PageVisualize():
    def __init__(self, Image, Layout):
        self.Image = Image
        self.Layout = Layout
        self.Text = []

    def annotate(self, LTType, LTLines):
        ImageLines = getLines(self.Layout, LTType, LTLines)
        self.drawBox(LTType, ImageLines)

    def show(self):
        height, width = self.Image.shape[:2]
        size = (int(height * 0.8), int(width * 1.2))
        PageImage = cv2.resize(self.Image, size)
        cv2.imshow('img', PageImage)
        cv2.waitKey(0)

    def drawBox(self, LTType, Lines):
        if LTType == LTTitle:
            typeText = 'subclause'
            color = (148, 238, 78)
        if LTType == LTTiao:
            typeText = 'clause'
            color = (238, 103, 122)
        elif LTType == LTZhang:
            color = (0, 140, 255)
            typeText = 'chapter'
        elif LTType == LTJie:
            color = (255, 206, 135)
            typeText = 'section'

        for Line in Lines:
            leftTop = (Line[0], Line[1])
            rightDown = (Line[2], Line[3])
            cv2.rectangle(self.Image, leftTop, rightDown, color, 3)
            cv2.putText(self.Image, typeText, leftTop, 0, 1.5, color, thickness=3)

            location = typeText
            for loc in Line:
                location += ' ' + str(loc)
            self.Text.append(location)
