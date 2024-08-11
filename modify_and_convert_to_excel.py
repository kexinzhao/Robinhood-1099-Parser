import pandas as pd

df = pd.read_csv('./files/TD_Ameritrade_Kexin_1099_v3.csv')
print(len(df))
print(df)

#print(df.loc[len(df) - 1, :])
#print(type(df["sold_date"][0]))
#print(type(df["quantity"][0]))
#print(type(df["proceeds"][0]))
#print(type(df["acquired_date"][0]))
#print(type(df["cost"][0]))
#print(type(df["wash_sales_loss"][0]))
#print(type(df["gain_loss"][0]))

df.loc[len(df)] = ["UNITED STATES TREASURY BILLS BILL / CUSIP: 912796CQ0 / Symbol:", "08/29/23", "20,000.000", "19,952.20", "06/12/23", "19,739.64", "NaN", "212.56"]
print(len(df))
print(df)

df.to_excel('./files/TD_Ameritrade_Kexin_1099_v0.xlsx', index=True)
df.to_excel('./files/TD_Ameritrade_Kexin_1099.xlsx', index=False)
