#!/usr/bin/python
# -*- Coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

"""
ガード硬直差を計算して描画
"""


def main():
    OP_RATE = 1.05
    GUARD_H = "ガード側の有利フレーム"
    GUARD_SJ_H = "ガード側の有利フレーム SJ"
    df = pd.read_csv(r"data\frame2.csv", index_col=0)
    rate = 12
    divNo = 4
    SJ_RATE = 0.85

    for col in df.columns.values:
        if "空" in col:
            df.ix[GUARD_H, col] = (df.ix["着地隙", col] + df.ix["着地移行フレーム", col] - (math.floor(df.ix["基礎ダメ", col] * 0.8 * df.ix["補正倍率", col] * OP_RATE) + 2))
            df.ix[GUARD_SJ_H, col] = (df.ix["着地隙", col] + df.ix["着地移行フレーム", col] - (math.floor(df.ix["基礎ダメ", col] * 0.8 * df.ix["補正倍率", col] * OP_RATE * SJ_RATE) + 2))
        else:
            df.ix[GUARD_H, col] = (df.ix["全体フレーム", col] - df.ix["発生", col] - (math.floor(df.ix["基礎ダメ", col] * 0.8 * df.ix["補正倍率", col] * OP_RATE) + 2))

    for i in range(divNo):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        if i == (divNo - 1):
            left = np.arange(len(df.ix[GUARD_H, i * rate:]))
            ax.barh(left, df.ix[GUARD_SJ_H, i * rate:], align="center")
            ax.barh(left, df.ix[GUARD_H, i * rate:], align="center", tick_label=list(df.columns[i * rate:]))
        else:
            left = np.arange(len(df.ix[GUARD_H, i * rate:(i + 1) * rate]))
            ax.barh(left, df.ix[GUARD_SJ_H, i * rate:(i + 1) * rate], align="center")
            ax.barh(left, df.ix[GUARD_H, i * rate:(i + 1) * rate], align="center", tick_label=list(df.columns[i * rate:(i + 1) * rate]))
        # plt.yticks(df.ix[GUARD_H, i * rate:(i + 1) * rate], list(df.columns[i * rate:(i + 1) * rate]))
        ax.set_xlabel('ガード側の最小有利フレーム')
        # ax.set_xlabel('フレーム')
        plt.tight_layout()
        plt.savefig("guard" + str(i) + ".png")


if __name__ == '__main__':
    main()
