from pdfminer.layout import *

def TiaoExtraction(PageLayout):
    Text = []

    for Box in PageLayout:
        if isinstance(Box, LTTextBoxHorizontal):
            for Line in Box:
                text = Line.get_text().replace(" ", "")
                TiaoLoc = text.find('条')

                if TiaoLoc > 0 and text[0] == '第':
                    text = text[1:TiaoLoc].replace(" ", "")
                    if text.isdigit():
                        Text.append([Line])
                    else:
                        Yes = True
                        for char in text:
                            if not char in ["十", "一", "二", "三", "四", "五", "六", "七", "八", "九", "百"]:
                                Yes = False
                                break
                        if Yes:
                            Text.append([Line])
                else:
                    if text.split('\n')[0].isdigit():
                        continue

                    if (not (len(text) >= 4 and text[0] == '第' and (text[2] == '章' or text[3] == '章')))\
                        and (not (len(text) >= 4 and text[0] == '第' and (text[2] == '节' or text[3] == '节'))):
                        if len(Text) == 0:
                            if not Line.x0 * 4 > PageLayout.x1:
                                Text.append([Line])
                        else:
                            Text[len(Text) - 1].append(Line)

    return Text