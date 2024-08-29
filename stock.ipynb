import pandas as pd
import matplotlib.pyplot as plt


trades_df = pd.read_csv('trades.csv')


trades_df.rename(columns={'P/L ': 'P/L'}, inplace=True)


trades_df_clean = trades_df.dropna(subset=['P/L', 'Entry date'])


trades_df_clean['Entry date'] = pd.to_datetime(trades_df_clean['Entry date'], format='%d-%b-%y')


trades_df_clean = trades_df_clean.sort_values(by='Entry date')


trades_df_clean['Cumulative P/L'] = trades_df_clean['P/L'].cumsum()


plt.figure(figsize=(10, 6))
plt.plot(trades_df_clean['Entry date'], trades_df_clean['Cumulative P/L'], marker='o', linestyle='-', color='blue')
plt.title('Equity Curve')
plt.xlabel('Entry Date')
plt.ylabel('Cumulative P/L')
plt.grid(True)
plt.show()
