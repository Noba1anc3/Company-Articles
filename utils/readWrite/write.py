import os
import cv2
import json
from utils.logging.syslog import Logger

def ImageWrite(ImageList, fileName, fileFolder):
    imgFolder = fileFolder + str(fileName) + '/'

    if not os.path.exists(imgFolder[:-1]):
        os.mkdir(imgFolder)

    for index in range(len(ImageList)):
        Image = ImageList[index]
        imgName = str(fileName) + '_' + str(index+1) + '.jpg'
        cv2.imwrite(imgFolder + imgName, Image)

    logging = Logger(__name__)
    Logger.get_log(logging).info('Image Saved')
    logging.logger.handlers.clear()


def JsonWrite(PagesText, fileName, fileFolder):
    pdf_folder = fileFolder + str(fileName) + '/'
    if not os.path.exists(pdf_folder):
        os.mkdir(pdf_folder)
    for index in range(len(PagesText)):
        Page = PagesText[index]
        txtPath = pdf_folder + str(fileName) + '_' + str(index+1) + '.txt'
        with open(txtPath, 'w') as f:
            for Line in Page:
                f.write(Line + '\n')

    logging = Logger(__name__)
    Logger.get_log(logging).info('JsonFile Saved')
    logging.logger.handlers.clear()