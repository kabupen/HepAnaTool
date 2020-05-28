import ROOT as R

h_simu = R.TH1D("h_simu", "h_simu", 50, -5, 5)
h_data = R.TH1D("h_data", "h_data", 50, -5, 5)

h_simu.FillRandom("gaus", 10000)
h_data.FillRandom("gaus", 1000)

# Histogram
h_simu.Scale(1/h_simu.Integral())
h_data.Scale(1/h_data.Integral())

# gStyle
R.gStyle.SetOptStat(0)

c = R.TCanvas("c", "c", 700, 600)
h_simu.Draw("hist")
h_data.Draw("same p")
c.SaveAs("ana_before.pdf")

c = R.TCanvas("c", "c", 700, 600)

# Margin
R.gPad.SetTopMargin(0.1);
R.gPad.SetBottomMargin(0.15);
R.gPad.SetRightMargin(0.05);
R.gPad.SetLeftMargin(0.18);

## h_simu
h_simu.SetTitle("")
h_simu.GetXaxis().SetTitle("m_{X} [GeV]")
h_simu.GetYaxis().SetTitle("Entries")

h_simu.GetXaxis().SetLabelSize(0.05)
h_simu.GetYaxis().SetLabelSize(0.05)

h_simu.GetXaxis().SetTitleSize(0.05)
h_simu.GetXaxis().SetTitleOffset(1.1)

h_simu.GetYaxis().SetTitleSize(0.05)
h_simu.GetYaxis().SetTitleOffset(1.3)

h_simu.SetLineColor(R.kBlack)
h_simu.SetFillColor(R.kAzure-4)
h_simu.Draw("hist")

### Error mesh
h_error = h_simu.Clone()
h_error.SetFillStyle(3244)
h_error.SetFillColor(R.kGray+2)
h_error.SetMarkerStyle(8)
h_error.SetMarkerSize(0)
h_error.Draw("e2 same")

## h_data
h_data.SetLineColor(R.kBlack)
h_data.SetMarkerStyle(8)
h_data.SetMarkerSize(0.8)
h_data.Draw("same p")

# Range
h_simu.GetYaxis().SetRangeUser(0, 0.115)

# ATLAS Label
latex = R.TLatex()
latex.SetNDC(1)
latex.SetTextFont(72)
latex.DrawLatex(0.2, 0.83, "ATLAS")
latex.SetTextFont(42)
latex.DrawLatex(0.34, 0.83 , "Internal")
latex.SetTextSize(0.04)
latex.DrawLatex(0.21, 0.79, "pp #rightarrow XX #rightarrow yyzz")
latex.SetTextSize(0.035)
latex.DrawLatex(0.21, 0.74 , "X TeV, Y fb^{-1}")

# Legend
legend = R.TLegend(0.7, 0.75, 0.9, 0.85)
legend.SetBorderSize(0)
legend.SetFillStyle(0)
legend.AddEntry(h_data,  "data", "pl")
legend.AddEntry(h_simu,  "background", "f")
legend.AddEntry(h_error, "Uncertainty", "f")
legend.Draw()

c.SaveAs("ana_after.pdf")

