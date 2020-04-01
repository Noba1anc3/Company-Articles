from pdfminer.layout import *

def JieExtraction(PageLayout):
    Text = []

    for Box in PageLayout:
        if isinstance(Box, LTTextBoxHorizontal):
            for Line in Box:
                text = Line.get_text().replace(" ", "")
                if len(text) >= 4 and text[0] == '第' and (text[2] == '节' or text[3] == '节'):
                    Text.append(Line)

    return Text