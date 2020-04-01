from pdfminer.layout import *

def TiaoExtraction(PageLayout):
    Text = []

    for Box in PageLayout:
        if isinstance(Box, LTTextBoxHorizontal):
            for Line in Box:
                text = Line.get_text().replace(" ", "")
                if len(text) >= 1 and text[0] == '第':
                    TiaoLoc = text.find('条')
                    if TiaoLoc > 0:
                        text = text[1:TiaoLoc].replace(" ", "")
                        if text.isdigit():
                            Text.append(Line)
                        else:
                            Yes = True
                            for char in text:
                                if not char in ["十", "一", "二", "三", "四", "五", "六", "七", "八", "九", "百"]:
                                    Yes = False
                                    break
                            if Yes:
                                Text.append(Line)

    return Text