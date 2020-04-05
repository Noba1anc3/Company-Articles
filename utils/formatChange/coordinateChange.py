
from utils.formatChange.visualize.Layout import *

def coordinateChange(Layout, LTType, Box):

    x0Lock = False

    if LTType == LTZhang or LTType == LTJie:
        x0 = Box.x0
        x1 = Box.x1
        y0 = Box.y0
        y1 = Box.y1

    if LTType == LTTiao:
        x0 = 100000
        x1 = 0
        y0 = 100000
        y1 = 0
        for Line in Box:
            if Line.x0 < x0:
                x0 = Line.x0
            if Line.x1 > x1:
                x1 = Line.x1
            if Line.y0 < y0:
                y0 = Line.y0
            if Line.y1 > y1:
                y1 = Line.y1

    if LTType == LTTitle:
        Text = Box.get_text().replace(" ", "")
        if Text[0] == '(' or Text[0] == '（':
            for index in range(len(Box._objs)):
                char = Box._objs[index]
                text = char.get_text()
                if (text == '(' or text == '（') and not x0Lock:
                    x0 = char.x0
                    x0Lock = True
                if text == ')' or text == '）':
                    x1 = char.x1
                    break
        else:
            for index in range(len(Box._objs)):
                char = Box._objs[index]
                text = char.get_text()
                if text.isdigit() and not x0Lock:
                    x0 = char.x0
                    x0Lock = True
                if text == '、':
                    x1 = char.x1
                    break
        y0 = Box.y0
        y1 = Box.y1

    LayoutHeight = Layout.height
    XleftUp = int(x0 / 0.36)
    YleftUp = int((LayoutHeight - y1) / 0.36)
    XrightDown = int(x1 / 0.36)
    YrightDown = int((LayoutHeight - y0) / 0.36)

    location = [XleftUp, YleftUp, XrightDown, YrightDown]

    return location

def getLines(Layout, LTType, LTLines):
    Lines = []

    for index in range(len(LTLines)):
        Line = LTLines[index]
        location = coordinateChange(Layout, LTType, Line)
        Lines.append(location)

    return Lines