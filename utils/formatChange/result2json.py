
from utils.formatChange.coordinateChange import *

def rst2json(conf, fileName, semseg, PagesLayout):
    TextLevel = conf.text_level
    L1Text = None

    JsonDict = {}
    JsonDict['FileName'] = fileName
    JsonDict['Pages'] = []

    if TextLevel == 1:
        L1Text = semseg.Text.Text
    else:
        pass

    for page in range(semseg.Page):
        Layout = PagesLayout[page]

        LTPage = {}
        LTPage['PageNo'] = page + 1
        LTPage['PageLayout'] = []
        PageLayout = {}

        PageLayout['Text'] = []

        if 'Text' in PageLayout.keys():
            if TextLevel == 1:
                if not L1Text[page] == []:
                    TextItem = L1Text[page]
                    TextJson = L1TexT(Layout, 'L1Text', TextItem)
                    PageLayout['Text'].append(TextJson)
            else:
                pass

        LTPage['PageLayout'].append(PageLayout)
        JsonDict['Pages'].append(LTPage)

    return JsonDict

def L1TexT(PageLayout, LTType, L1Text):
    BBoxesList = NoteBBoxes(PageLayout, L1Text)
    TextBlock = []

    for index in range(len(L1Text)):
        L1TextBlock = L1Text[index]
        Text = {}

        Text['SemanticType'] = LTType
        Text['location'] = BBoxesList[index][0]
        Text['content'] = L1TextBlock.get_text().replace("\n", " ").replace("- ", "")[:-1]

        Text['TextLines'] = []
        for LineIndex in range(len(L1TextBlock)):
            L1TextLine = L1TextBlock._objs[LineIndex]
            TextLine = {}
            TextLine['content'] = L1TextLine.get_text().replace("-\n", "").replace("\n", "")
            TextLine['location'] = BBoxesList[index][LineIndex+1]
            Text['TextLines'].append(TextLine)

        TextBlock.append(Text)

    return TextBlock