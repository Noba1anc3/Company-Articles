
from utils.formatChange.visualize.annotate import *
from utils.formatChange.visualize.Layout import *

def rst2image(conf, semseg, PagesImage, PagesLayout):
    TextLevel = conf.text_level
    ImageList = []
    TextList = []

    if TextLevel == 1:
        Text = semseg.Text.Text
    else:
        Tiao = semseg.Text.Tiao
        Zhang = semseg.Text.Zhang
        Jie = semseg.Text.Jie
        Title = semseg.Text.Title

    for index in range(len(PagesImage)):
        PageImage = PagesImage[index]
        PageLayout = PagesLayout[index]

        PV = PageVisualize(PageImage, PageLayout)

        if TextLevel == 1:
            PageVisualize.annotate(PV, LTText, Text[index])
        else:
            PageVisualize.annotate(PV, LTTiao, Tiao[index])
            PageVisualize.annotate(PV, LTZhang, Zhang[index])
            PageVisualize.annotate(PV, LTJie, Jie[index])
            #PageVisualize.annotate(PV, LTTitle, Title[index])

        ImageList.append(PV.Image)
        TextList.append(PV.Text)

    return ImageList, TextList