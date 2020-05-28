# CERN ROOT の使い方
C++かPythonのどちらかを使うことで、CERNが提供するお絵かきライブラリROOTを使用することができます。
高エネ実験でよく使用される実験データ・フォーマットはROOT形式だと思いますので、ROOTでの描画テクニックは至る所で必要になってくると思います。
ここでは必要最低限の描画テクニックをまとめて、たかがお絵かきに時間を掛けない研究ライフを送ることを目的とします。

## 見栄えを整える
見栄えを整える前（左）と、整えた後（右）。
ガウシアンで背景事象と実験値に見立てたデータを擬似的に生成、論文でよく見るような決めプロットみたいにするためのテクニックをまとめます。

<img width="30%" src="fig/ana_before.png" style="float: left;"/>
<img width="30%" src="fig/ana_after.png"/>

### 統計Boxを消す

```
R.gStyle.SetOptStat(0)
```

### マージン（余白）を調整する

```
R.gPad.SetTopMargin(0.1);
R.gPad.SetBottomMargin(0.15);
R.gPad.SetRightMargin(0.05);
R.gPad.SetLeftMargin(0.18);
```

### x軸、y軸のタイトルを調整する

```python
h_simu.SetTitle("")
h_simu.GetXaxis().SetTitle("m_{X} [GeV]")
h_simu.GetXaxis().SetTitleSize(0.05)
h_simu.GetXaxis().SetTitleOffset(1.1)

h_simu.GetYaxis().SetTitle("Entries")
h_simu.GetYaxis().SetTitleSize(0.05)
h_simu.GetYaxis().SetTitleOffset(1.3)
```

### x軸、y軸のラベルを調整する

```python
h_simu.GetXaxis().SetLabelSize(0.05)
h_simu.GetYaxis().SetLabelSize(0.05)

```

### ヒストグラムの見栄え

```python
h_simu.SetLineColor(R.kBlack)
h_simu.SetFillColor(R.kAzure-4)
```

### エラーをメッシュで表示する


## 統計処理を加える

