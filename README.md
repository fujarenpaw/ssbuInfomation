# スマブラ情報まとめGithub
スマブラSPに関する情報、特にガオガエンの情報についてまとめてます。

ガオガエン使いの情報共有まとめ場所になったらうれしいですが、多分ならないでしょう。

巨大にならない限りこのReadMEに情報を記載します。


## ガオガエン関係
- 掴み打撃可能回数

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/ガオガエン掴み打撃.png)
- 崖つかまり状態の敵にヒットするガオガエンの攻撃

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/崖つかまり攻撃1.jpg)

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/崖つかまり攻撃2.jpg)

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/崖つかまり攻撃3.jpg)

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/崖つかまり攻撃4.jpg)

- リベンジ倍率

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/リベンジ倍率.png)
```
リベンジ倍率 = 1 + (0.25 + 0.075 * 敵攻撃判定の基礎ダメージ)
```

- 下投げ上B復帰可能ライン
![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/上B復帰可能ライン.jpg)

- リベンジ状態でのガード硬直差

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/リベンジ状態のガード硬直差1.png)

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/リベンジ状態のガード硬直差2.png)

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/リベンジ状態のガード硬直差3.png)

***※NBのN段目の全体フレームをN+1段目の発生フレームとして計算***
```
空中攻撃以外の有利フレーム = 全体フレーム - 発生フレーム - ガード硬直
空中攻撃の有利フレーム = 着地移行フレーム + 着地隙 - ガード硬直
ガード硬直 = INT((ダメージ * 0.8 * 補正倍率) + 2) [F]
補正倍率
1.0：弱、強攻撃
0.725：スマッシュ攻撃
0.33：空中攻撃（空N・空前・空後・空上・空下）
0.29：飛び道具
※SJ補正なし、OP補正あり
```
## システム関係
- 着地隙が少ない攻撃、ガード硬直差

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/ガード硬直差1.png)

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/ガード硬直差2.png)

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/ガード硬直差3.png)

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/ガード硬直差4.png)


- 崖つかまり時の無敵時間

![](https://raw.githubusercontent.com/fujarenpaw/ssbuInfomation/master/picture/崖つかまり.jpg)
```
無敵時間 = INT((滞空時間 * 0.2 ＋ 44) - (蓄積% * 44 / 120))　[F]
　4 ≤ 無敵時間 ≤ 104 [F]
　0 ≤ 滞空時間 ≤ 300 [F]
　0 ≤   蓄積％  ≤ 120 [％]
```
