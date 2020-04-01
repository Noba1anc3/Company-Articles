from semseg.text.level1.Leve1Extraction import Leve1Extraction
from semseg.text.level2.ZhangExtraction import ZhangExtraction
from semseg.text.level2.JieExtraction import JieExtraction
from semseg.text.level2.TiaoExtraction import TiaoExtraction
from semseg.text.level2.TitleExtraction import TitleExtraction
from utils.logging.syslog import Logger

class TextExtraction():
    def __init__(self, TextLevel, PagesLayout):
        self.Text = []
        self.Zhang = []
        self.Jie = []
        self.Tiao = []
        self.Title = []
        self.TextLevel = TextLevel
        self.PagesLayout = PagesLayout
        self.Segmentation()

    def Segmentation(self):
        for PageNo in range(len(self.PagesLayout)):
            PageLayout = self.PagesLayout[PageNo]

            if self.TextLevel == 1:
                Text = Leve1Extraction(PageLayout)
                self.Text.append(Text)

            elif self.TextLevel == 2:
                Zhang = ZhangExtraction(PageLayout)
                self.Zhang.append(Zhang)
                Jie = JieExtraction(PageLayout)
                self.Jie.append(Jie)
                Tiao = TiaoExtraction(PageLayout)
                self.Tiao.append(Tiao)
                Title = TitleExtraction(PageLayout)
                self.Title.append(Title)

        logging = Logger(__name__)
        Logger.get_log(logging).info('Text Segmentation Finished')
        logging.logger.handlers.clear()
