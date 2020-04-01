from pdfminer.layout import *

def TitleExtraction(PageLayout):
    Text = []

    for Box in PageLayout:
        if isinstance(Box, LTTextBoxHorizontal):
            for Line in Box:
                text = Line.get_text().replace(" ", "")

                if text[0] == "(":
                    r_kuohao = text.find(")")
                    if r_kuohao >= 0:
                        text = text[1:r_kuohao]
                        if text.isdigit():
                            Text.append(Line)
                            continue
                        else:
                            Yes = True
                            for char in text:
                                if not char in ["十", "一", "二", "三", "四", "五", "六", "七", "八", "九"]:
                                    Yes = False
                                    break
                            if Yes:
                                Text.append(Line)
                                continue

                elif text[0] == "（":
                    r_kuohao = text.find("）")
                    if r_kuohao >= 0:
                        text = text[1:r_kuohao]
                        if text.isdigit():
                            Text.append(Line)
                            continue
                        else:
                            Yes = True
                            for char in text:
                                if not char in ["十", "一", "二", "三", "四", "五", "六", "七", "八", "九"]:
                                    Yes = False
                                    break
                            if Yes:
                                Text.append(Line)
                                continue
                else:
                    dunhao = text.find("、")
                    if dunhao >= 0:
                        text = text[:dunhao]
                        if text.isdigit():
                            Text.append(Line)

    return Text