
"""
Created on Thu Nov  9 18:05:23 2023

@author: Aberah
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("Data2.csv",encoding='windows-1254')
print(df)


"""line_plot of cases in period of 2019 to 2021"""
ANG = df[df["Location"] == "Angola"]
BRU = df[df["Location"] == "Burundi"]
IND = df[df["Location"] == "India"]
PAN = df[df["Location"] == "Panama"]
INS = df[df["Location"] == "Indonesia"]

def lep():
#Angola

    fig, ax = plt.subplots(figsize=(12, 8))
    plt.plot(ANG['Period'].astype("str"),ANG["FactValueNumericHigh"],marker = 'o',
         label = "Angola")

    #Burundi

    #fig, ax = plt.subplots(figsize=(12, 8))
    plt.plot(BRU['Period'].astype("str"),BRU["FactValueNumericHigh"],marker = 'o',
         label = "Burundi")


    #India
    #fig, ax = plt.subplots(figsize=(12, 8))
    plt.plot(IND['Period'].astype("str"),IND["FactValueNumericHigh"],marker = 'o',
         label = "INDIA")
    #Panama

    plt.plot(PAN['Period'].astype("str"),PAN["FactValueNumericHigh"],marker = 'o',
         label = "Panama")


   #Indonesia


    plt.plot(INS['Period'].astype("str"),INS["FactValueNumericHigh"],marker = 'o',
         label = "Indonesia")
    plt.legend()
    plt.title("MAliera Cases from 2017 to 2021")
    ax.set(xlabel="Years", ylabel="Maleria cases in lac")
    plt.show()
    plt.savefig("Line_plot")

def pi():
    """pi_chart only in 2019"""

    CAS2019 = df[df["Period"] == 2019]

    #print(arr2020)
    arr2019 = np.array(CAS2019["FactValueNumericHigh"])
    plt.figure(figsize=(12,10))
    plt.pie(arr2019, labels=['Angola', 'Burundi', 'India', 'Panama', 
                         'Indonesia'])
    plt.legend()
    plt.show()
    plt.savefig("Pi_chart")

def bar():
    """Bar_Graph shows distribution of maleria cses """

    plt.figure(figsize=(12,10))
    plt.subplot(3,2,1)
    plt.hist(ANG["FactValueNumericHigh"], label = "Angola", density= True)
    plt.legend()
    plt.subplot(3,2,2)
    plt.hist(BRU["FactValueNumericHigh"], label = "Burundi", density= True)
    plt.legend()
    plt.subplot(3,2,3)
    plt.hist(IND["FactValueNumericHigh"], label = "India", density= True)
    plt.legend()
    plt.subplot(3,2,4)
    plt.hist(PAN["FactValueNumericHigh"], label = "Panama", density= True)
    plt.legend()
    plt.subplot(3,2,5)
    plt.hist(INS["FactValueNumericHigh"], label = "Indonesia", density= True)
    plt.legend()
    plt.show()
    plt.savefig("Bar_graph")
    
lep()
pi()
bar()



