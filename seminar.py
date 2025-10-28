from operator import index

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#pandas e construita peste numpy
# Exista 2 mari categorii
# Pandas Series
# Pandas DataFrame
# Series - seturi de date unidimensionale (o singura coloana)
# DF - seturi de date multidimensionale


s = pd.Series([10,20,30])


df = pd.DataFrame(
    {
        'Name':['Alice','Bob','Carol'],
        'Age':[35,38,40],
        'Salary':[5000,6000,7200]
    }
)


df = pd.read_csv("res/employees.csv",index_col=0)
#

print(df.head()) # primele 5 randuri

print(df.tail()) # last 5

print(df.info()) # structura, tipuri de date

print(df.describe()) # descrie dpdv statistic variabilele numerice: min max medie mediana mod stddev

print(df.shape) #randuri x coloane

print(df.columns) # lista cu denumirea coloanelor

print(df.index) # denumirea randurilor / instantelor

#data acces


ages = df["Age"]
subset = df[["Name","Age","Salary"]]
print(subset)

#acces folosind iloc
fr = df.iloc[0] #primul rand - iloc -> index location
ftr = df.iloc[0:3]
#acces folosind loc
sr = df.loc[1]
ors = df.loc[1:3,["Name","Salary"]]

#filtrare pe baza de conditii boolean

fc = df[df["Age"] > 30]
sc = df[(df["Salary"]>6000) & (df["Age"]<40)]
print(fc)
print(sc)

#modificare de valori

df["Taxed Salary"] = df["Salary"] * 0.9 # adaugare de coloana suplimentara

df["Higher taxed"] = df["Salary"].apply(lambda x: 1 if x > 6000 else 0)

df.rename(columns={"Salary":"Gross Salary"},inplace=True)
#cand inplace = True se modifica obicetul cu totul, altfel se intoarce o copie cu datele modificate

print(df)


df.drop(columns=["TaxedSalary"],inplace=True) # drop la coloana
df.drop(index=[0],inplace=True) #drop la rand

#gestionarea valorilor lipsa / data sanitization

# vrem sa tratam de fiecare data scenariile cu date lipsa
# Abordarile uzuale
# 2 scenarii
# 1. FDate numerice: facem drop la randuri / coloana
# 2. Date categorice: Modul ( cea mai des intalnita valoare) sau o valoarea convenabil aleasa care sa nu influenteze semnificativ operatiile

#detectia NaN
count =  df.isna().sum()

print(count)

df.dropna() # da drop la randurile care au valori lipsa
df.dropna(axis=1) # drop la coloanele care au valori lipsa

df.fillna(0)
df["Salary"].fillna(df["Salary"].mean(),inplace=True)



#data transformation
#Vectorized

df["AgeInMonth"] = df["Age"] * 12

# apply
# def returnBracket(x):
#     if x > 6000:
#         return "High"
#     else:
#         return "Low"
# df["IncomeBracket"] = df["Gross Salary"].apply(lambda x: returnBracket(x))

df["IncomeBracket"] = df["Gross Salary"].apply(lambda x: "High" if  x > 6000 else "Low")


df["Name"] = df["Name"].str.upper()



#statistica
#centrarea datelor - transalatarea in jurul valorii 0
#Xi - X medie


#mean median mode std var corr



#Scalarea datelor - aducerea valorilor de pe coloane la un ordin de marime comparabil
#impartirea la standard deviation

#std date







