import pandas as pd
data = pd.read_excel('input.xlsx')
a=data['Denumire'].tolist()
print(a[1])