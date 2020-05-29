# チートシート
ROOTインタープリター上、またマクロ内でのコマンド・メソッドの呼び出し方をまとめています。
簡略化を図るため、

```python
import ROOT as R

hist = R.TH1D("hist", "hist", 10, 0, 10) # 範囲、ビン幅は何でもok
```

が既に定義されていると想定して、表にまとめています。


||説明|
|:---|:---|
|`hist.Scale(1/hist.Integral())`|ヒストグラムを規格化する|
|```hist.GetYaxis().SetRangeUser(0, 1)```|y軸の範囲を変更する|
|R.gStyle.SetOptStat(0)                  |統計ボックスを消す|
