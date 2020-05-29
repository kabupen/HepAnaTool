# チートシート
ROOTインタープリター上、またマクロ内でのコマンド・メソッドの呼び出し方をまとめています。
簡略化を図るため、

```python
import ROOT as R

hist = R.TH1D("hist", "hist", 10, 0, 10) # 範囲、ビン幅は何でもok
```

が既に定義されていると想定して、表にまとめています。


|コマンド|説明|
|:---|:---|
|`hist.Scale(1/hist.Integral())`              |ヒストグラムを規格化する|
|`hist.GetYaxis().SetRangeUser(0, 1)`         |y軸の範囲を変更する|
|`hist.GetXaxis().SetTitle("x軸のタイトル")`  |x軸のタイトルを設定する|
|`hist.GetXaxis().SetTitleSize()`             |x軸のタイトルの文字サイズを設定する|
|`hist.GetXaxis().SetTitleOffset()`           |x軸のタイトルのオフセットを設定する|
|`hist.GetXaxis().SetLabelSize()`             |x軸ラベルの文字サイズを設定する|
|`hist.GetXaxis().SetLabelOffset()`           |x軸ラベルのオフセットを設定する|
|`R.gStyle.SetOptStat(0)`                     |統計ボックスを消す|
|`hist.Draw("hist")`                          |ヒストグラムとして出力する|
|`hist.Draw("p")`                             |ポイントとして出力する|
