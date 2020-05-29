# RooStats, RooFit
CERN ROOTに付随する、より高度な統計処理を行うためのRooStats, RooFitと呼ばれるパッケージについての説明です。
個人的にヒストグラムを手軽に描画するときにはPyROOTを使っていますが、RooStats系を使うときにはC++を使っています（型、名前空間、引数の渡し方を明示したいので）。

## RooWorkspace
ガウス分布に従った乱数を振って、描画する方法です。

<img width="50%" src="fig/roostats/gauss.png">

```cpp
void gaussian()
{
    RooWorkspace ws("ws");
    ws.factory("Gaussian::gaus(x[-10,10], mean[0], sigma[1])");
    ws.factory("PROD::model(gaus)");

    RooDataSet* data = ws.pdf("model")->generate(*ws.var("x"), 1000);
    RooPlot *frame = ws.var("x")->frame();
    data           ->plotOn(frame);
    ws.pdf("model")->plotOn(frame);
    frame->Draw();
}
```
