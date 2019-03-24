#!/usr/bin/python
# -*- Coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

"""
ガード硬直差計算、グラフ描画(リベンジ対応)
"""


def main():
    cols = ["横強", "上強", "下強", "横スマ", "上スマ", "下スマ", "空N", "空前", "空後", "空上", "空下"]
    # cols = ["横強", "上強", "下強", "横スマ", "上スマ", "下スマ"]
    # cols = ["空N", "空前", "空後", "空上", "空下", "DA"]
    # cols = ["NB1", "NB2", "NB3", "NB4"]
    rates = [1.0, 3.0]
    OP_RATE = 1.05
    SMASH_FULL_HOLD_RATE = 1.4
    df = pd.read_csv(r"data\frame.csv", index_col=0)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    for col in cols:
        frame = []
        for rate in rates:
            if "空" in col:
                frame.append(df.ix["着地隙", col] + df.ix["着地移行フレーム", col] - (int(df.ix["基礎ダメ", col] * 0.8 * df.ix["補正倍率", col] * rate * OP_RATE) + 2))
            else:
                frame.append(df.ix["全体フレーム", col] - df.ix["発生", col] - (int(df.ix["基礎ダメ", col] * 0.8 * df.ix["補正倍率", col] * rate * OP_RATE) + 2))
        ax.plot(rates, frame, label=col)
    ax.legend()
    plt.title("リベンジ状態の有利フレーム")
    ax.set_xlabel("リベンジ倍率")
    ax.set_ylabel("ガードした側の有利フレーム")
    plt.savefig("output.png")


if __name__ == '__main__':
    main()
