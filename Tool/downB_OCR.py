#!/usr/bin/python
# -*- Coding: utf-8 -*-
import pyocr
import pyocr.builders
import cv2
from PIL import Image


def main():
    test = "test.png"
    testPath = r"C:\Users\hoge\Documents\GitHub\ssbuInfomation\Tool\origin\3.jpg"
    im = cv2.imread(testPath)

    # 縦横比判定
    x1 = 600
    x2 = 770
    y1 = 133
    y2 = 250

    dst = im[x1:x2, y1:y2]

    cv2.imwrite(test, dst)
    print(OCR(test))


def OCR(imgPath):
    tools = pyocr.get_available_tools()
    if len(tools) == 0:
        print("No OCR tool found")
        return ""
        # sys.exit(1)
    # The tools are returned in the recommended order of usage
    tool = tools[0]

    lang = 'eng'
    txt = tool.image_to_string(
        # Image.open('bigTrimming.jpg'),
        Image.open(imgPath),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )
    return txt


if __name__ == '__main__':
    main()
