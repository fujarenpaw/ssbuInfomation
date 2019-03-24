#!/usr/bin/python
# -*- Coding: utf-8 -*-
import matplotlib.pyplot as plt

"""
リベンジ倍率を描画
"""


def main():
    damages = [0, 23.33]
    rate = []

    for damage in damages:
        rate.append(1 + (0.25 + 0.075 * damage))

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(rate, damages)
    plt.title("ダメージとリベンジ倍率")
    ax.set_xlabel("リベンジ倍率")
    ax.set_ylabel("ダメージ")
    plt.savefig("revenge.png")


if __name__ == '__main__':
    main()
