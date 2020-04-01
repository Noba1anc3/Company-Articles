
from utils.formatChange.visualize.Layout import *

def coordinateChange(Layout, LTType, Line):

    x0Lock = False

    if LTType == LTZhang:
        for index in range(len(Line._objs)):
            char = Line._objs[index]
            text = char.get_text()
            if text == '第' and not x0Lock:
                x0 = char.x0
                x0Lock = True
            if text == '章':
                x1 = char.x1
                break

    if LTType == LTJie:
        for index in range(len(Line._objs)):
            char = Line._objs[index]
            text = char.get_text()
            if text == '第' and not x0Lock:
                x0 = char.x0
                x0Lock = True
            if text == '节':
                x1 = char.x1
                break

    if LTType == LTTiao:
        for index in range(len(Line._objs)):
            char = Line._objs[index]
            text = char.get_text()
            if text == '第' and not x0Lock:
                x0 = char.x0
                x0Lock = True
            if text == '条':
                x1 = char.x1
                break

    if LTType == LTTitle:
        Text = Line.get_text().replace(" ", "")
        if Text[0] == '(' or Text[0] == '（':
            for index in range(len(Line._objs)):
                char = Line._objs[index]
                text = char.get_text()
                if (text == '(' or text == '（') and not x0Lock:
                    x0 = char.x0
                    x0Lock = True
                if text == ')' or text == '）':
                    x1 = char.x1
                    break
        else:
            for index in range(len(Line._objs)):
                char = Line._objs[index]
                text = char.get_text()
                if text.isdigit() and not x0Lock:
                    x0 = char.x0
                    x0Lock = True
                if text == '、':
                    x1 = char.x1
                    break


    if not x0Lock:
        print(Line.get_text())

    LayoutHeight = Layout.height
    XleftUp = int(x0 / 0.36)
    YleftUp = int((LayoutHeight - Line.y1) / 0.36)
    XrightDown = int(x1 / 0.36)
    YrightDown = int((LayoutHeight - Line.y0) / 0.36)

    location = [XleftUp, YleftUp, XrightDown, YrightDown]

    return location

def getLines(Layout, LTType, LTLines):
    Lines = []

    for index in range(len(LTLines)):
        Line = LTLines[index]
        location = coordinateChange(Layout, LTType, Line)
        Lines.append(location)

    return Lines