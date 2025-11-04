from operator import index

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from fiona.env import local
from sqlalchemy.sql.roles import TruncatedLabelRole

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


df = pd.read_csv("employees.csv",index_col=0)
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


df.drop(columns=["Taxed Salary"],inplace=True) # drop la coloana
df.drop(index=[1],inplace=True) #drop la rand

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
#df["Gross Salary"].fillna(df["Gross Salary"].mean(),inplace=True)



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

#Standardizarea unei variabile
df["Salary centered"] = df["Gross Salary"] - df["Gross Salary"].mean()

df["Salary standerdized"] = (df["Gross Salary"] - df["Gross Salary"].mean()) / df["Gross Salary"].std()
#Xi - X medie


#mean median mode std var corr


#Normalizarea datelor - aducerea datelor intr-un interval [0:1] sau [-1:1]


# Se realizeaza dupa formula


#x` = xi - xmin / xmax - xmin

#la nivel de impact asupra datelor
#std se aseamana cu o redimensionare si translatare a distributiei
# iar normalizarea modifica distributia datelor, ceea ce inseamna ca reprezentarea grafica se modifica

#Scalarea datelor - aducerea valorilor de pe coloane la un ordin de marime comparabil
#impartirea la standard deviation

#std date
print("Medie",df["Gross Salary"].mean())
print("Mediana",df["Gross Salary"].median())
print("Mod",df["Gross Salary"].mode())

print("Stddev: ",df["Gross Salary"].std())
print("Dispersie: ",df["Gross Salary"].var())

#coef de corelatie
print(df[["Gross Salary","Age"]].corr())

#valorile sunt intre -1 si 1
#cand valoarea e pozitiva,atunci variabilele se afla in legatura directa
#cand val e negativa, atunci variabilele se afla in legatura inversa

#
# print(df["Gross Salary"])
#
# df["Gross Salary"].hist(bins=15)
#
# plt.show()

#cobminarea datelor separate

df1 = pd.DataFrame({
    "ID":[5,6,7],
    "Name":["Eva","Frank","Grace"]
})

df2 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alice","Bob","Carol"]
})


df3 = pd.DataFrame({
    "ID":[1,2,3],
    "Departament":["IT","HR","Finance"]
})

merged = df2.merge  (df3,on="ID")
print(merged)


concat = pd.concat([df1,df2])
print(concat)


#mergeurile functioneaza ca join urile din SQL
#left -> tot ce e comun + tabela din stanga
#inner -> Doar ce e comun
#right -> tot ce e comun + tabela din dreapta
#outer -> Totul dintre cele 2 tabele




employees = pd.read_csv("employees.csv")
departments = pd.read_csv("departments.csv")

#left join

left = employees.merge(departments,left_on="DepartmentID",right_on="DepartmentID",how="left")
print(left)


right = employees.merge(departments,left_on="DepartmentID",right_on="DepartmentID",how="right")
print(right)


inner = employees.merge(departments,left_on="DepartmentID",right_on="DepartmentID",how="inner")
print(inner)


outer = employees.merge(departments,left_on="DepartmentID",right_on="DepartmentID",how="outer")
print(outer)


#Exercitiu siruta


tabel_etnii = pd.read_csv("Ethnicity.csv",index_col=0)

#nan_replace()

variabile_etnii = list(tabel_etnii.columns)[1:]

#Calcul populatie pe etnii la nivelde judet

localitati = pd.read_excel("CoduriRomania.xlsx",index_col=0)


print(tabel_etnii.head())

print(localitati.head())

#In conditiile in care criteriul de merge e index si nu o coloana se foloseste

t1 = tabel_etnii.merge(right=localitati,right_index=True,left_index=True)

g1 = t1[variabile_etnii + ["County"]].groupby(by="County").sum()


# g1.to_csv("outputEtniiJudete.csv")
# print(g1)


judete = pd.read_excel("CoduriRomania.xlsx",index_col=0,sheet_name="Judete")

t2 = g1.merge(right=judete,right_index=True,left_index=True)

g2 = t2[variabile_etnii+["Regiune"]].groupby(by="Regiune").sum()

print(g2)

#g2.to_csv("outputRegiuni.csv")





regiuni = pd.read_excel("CoduriRomania.xlsx",index_col=0,sheet_name="Regiuni")

t3 = g2.merge(right=regiuni,right_index=True,left_index=True)

g3 = t3[variabile_etnii+["Macroregiuni"]].groupby(by="Macroregiuni").sum()

print(g3)

#g3.to_csv("outputMacroRegiuni.csv")

