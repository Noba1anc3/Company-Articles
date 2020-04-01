
from semseg.text.textExtraction import TextExtraction

from utils.logging.syslog import Logger

class SemanticSegmentation():
    def __init__(self, conf, PagesImage, PagesLayout):
        self.configList = conf
        self.PagesImage = PagesImage
        self.PagesLayout = PagesLayout
        self.PgHeight = PagesLayout[0].height
        self.Page = len(PagesImage)
        self.Segmentation()

    def Segmentation(self):
        logging = Logger(__name__)
        Logger.get_log(logging).info('Segmentation Start')
        TextLevel = self.configList.text_level

        self.Text = TextExtraction(TextLevel, self.PagesLayout)

        Logger.get_log(logging).info('Segmentation Finished')
        logging.logger.handlers.clear()
