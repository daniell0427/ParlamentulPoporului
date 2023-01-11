import pandas as pd
from database import introdu
data = pd.read_excel('input.xlsx')
tit=data['Denumire'].tolist()
pro1=data['Lectura 1'].tolist()
cont1=data['Unnamed: 2'].tolist()
neu1=data['Unnamed: 3'].tolist()
pro2=data['Lectura 2'].tolist()
cont2=data['Unnamed: 5'].tolist()
neu2=data['Unnamed: 6'].tolist()
len=len(tit)
for i in range(1, len-1 ):

    introdu(str(tit[i]),str(pro1[i]),str(cont1[i]),str(neu1[i]),str(pro2[i]),str(cont2[i]),str(neu2[i]))
