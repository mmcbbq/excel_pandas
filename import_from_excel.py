import pandas as pd

df = pd.read_csv("teilnehmerdaten.csv")
dfexcel = pd.read_excel("teilnehmerdaten.xlsx", sheet_name=None)

print(dfexcel)
