import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('art.csv')
new_df = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
hiv_average = (new_df['Estimated number of people living with HIV_min']+new_df['Estimated number of people living with HIV_min'])/2
d = new_df[['Country', 'WHO Region']].assign(hiv_mean=hiv_average).head()
print(d)
print(new_df['WHO Region'].drop_duplicates(keep='first', inplace=False))
plt.title('Average HIV infections in different countries')
plt.xlabel('COUNTRIES')
plt.ylabel('Average number of HIV infections')
x = d['Country']
y = d['hiv_mean']
plt.grid(True)
plt.bar(x, y)
plt.show()

print("\n")
print(new_df.head(10).to_string())

