#!/usr/bin/python
# -*- Coding: utf-8 -*-
import pyocr
import pyocr.builders
import cv2
from PIL import Image
import glob
import sys
import pandas as pd

"""
呪文　コピペ用

イオ
イオナズン
ギラ
ベギラマ
ザキ
ザラキ
メガンテ
マダンテ
ラリホー
ホイミ
バイキルト
ピオリム
マホカンタ
アストロン
ルーラ
パルプンテ
かえん斬り
マヒャド斬り
まじん斬り
メタル斬り
ためる

bang
kaboom
sizz
sizzle
whack
thwack
kamikazee
magic burst
snooze
Heal
Oomph
acceleratle
bounce
kaclang
zoom
hocus pocus
Flame slash
kacrackle slash
hatchet man
metal slash
psyche Up

"""

def main():
    test = "test.png"
    testPath = r"C:\Users\hoge\Documents\GitHub\ssbuInfomation\Tool\origin\*.jpg"
    df = pd.DataFrame()
    # 縦横比判定
    x1 = 600
    x2 = 770
    y1 = 133
    y2 = 250
    cnt = 0

    for imgPath in glob.glob(testPath):
        savePath = str(cnt) + ".jpg"
        im = cv2.imread(imgPath)
        dst = im[x1:x2, y1:y2]

        cv2.imwrite(savePath, dst)
        magic = OCR(savePath)
        magicList = magic.split("\n")
        # 空文字は削除
        magicList = [i for i in magicList if i != ""]
        df = df.append(pd.Series(magicList), ignore_index=True)
        cnt += 1

    # df.to_csv("debug.csv")


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
