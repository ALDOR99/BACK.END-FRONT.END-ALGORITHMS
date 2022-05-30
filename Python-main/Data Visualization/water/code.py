import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.style.use('dark_background')
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib.colors import ListedColormap
from scipy.stats import norm, boxcox
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from collections import Counter
from scipy import stats
from tqdm import tqdm_notebook

## Importing LuciferML
# from luciferml.supervised import classification as cls 
# from luciferml.preprocessing import Preprocess as prep

import warnings
warnings.simplefilter(action='ignore', category=Warning)


dataset = pd.read_csv("water_potability.csv")


print(dataset.columns)

# 'ph' = Ph = DSÖ standartları aralığında/ 6.52–6.83
# 'Hardness' = Sertlik = TDS için istenen sınır 500 mg/l ve maksimum limit içme amaçlı öngörülen 1000 mg/l'dir.
# 'Solids' = Katı maddeler
# 'Chloramines' = Kloraminler  4 parça (ppm)) içme suyunda güvenli olarak kabul edilir.
# 'Sulfate' = Sülfat
# 'Conductivity' = İletkenlik = WHO standartlarına göre, EC değeri 400 μS / cm'yi geçmemelidir. 
# 'Organic_carbon' = Organik karbon US EPA < göre arıtılmış / içme suyunda TOC olarak 2 mg / L ve arıtma için kullanılan kaynak suyunda 4 mg / Lit <.
# 'Trihalomethanes' = Trihalometanlar 80 ppm'e kadar olan THM seviyeleri içme suyunda güvenli olarak kabul edilir.
# 'Turbidity' = Bulanıklık DSÖ'nün önerdiği 5,00 NTU değerinden daha düşüktür.
# 'Potability = Potansiyellik  1 içilebilir ve 0 içilebilir değil anlamına gelir


a = (dataset.head())
print()
print(dataset.shape)
print()


aaa = (dataset.describe())

# aa = dataset.describe().T.style.bar(
#     subset=['mean'],
#     color='#606ff2').background_gradient(
#     subset=['std'], cmap='PuBu').background_gradient(subset=['50%'], cmap='PuBu')


# print(aa)



print()
print(dataset.isnull())


print()

print(dataset.isnull().values.any())

print()

plt.figure(figsize=(12,6))
sns.countplot(x="Potability",data=dataset,palette="husl")
plt.show()
#%%

cols = ['ph', 'Hardness',
        'Solids', 'Chloramines',
        'Sulfate', 'Conductivity',
       'Organic_carbon', 'Trihalomethanes', 
       'Turbidity']

def boxPlotter(dataset, columnName):
    """
    Parametre olarak verilen sütun için boxplots çiziyor
    """
    
    sns.catplot(x="Potability", y=columnName, data=dataset, kind="box");
for column in tqdm_notebook(cols, desc = "Your Charts are being ready"):
    boxPlotter(dataset, column)
        
print()

#%% Pie Chart 

def pieChartPlotter(dataset, columnName):
    """
    """
    values = dataset[columnName].value_counts()
    labels = dataset[columnName].unique()
    pie, ax = plt.subplots(figsize=[10, 6])

    patches, texts, autotexts = ax.pie(values, labels=labels, autopct='%1.2f%%', shadow=True, pctdistance=.5,explode=[0.06]*dataset[columnName].unique()
                                       )

    plt.legend(patches, labels, loc="best")
    plt.title(columnName, color='white', fontsize=14)
    plt.setp(texts, color='white', fontsize=20)
    plt.setp(autotexts, size=10, color='black')
    autotexts[1].set_color('black')
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

print(dataset.columns)

pieChartPlotter(dataset, 'Potability') 
print()
#%% 

a = np.array([[1, 2, 3, 4], [4, 1, 2, 3], [3, 4, 1, 2], [2, 3, 4, 1]])
print(np.triu(a))
print("-"*30)
print(np.triu(a, k=1))
print("-"*20)
print(np.triu(a, k=-1))

#%% Correlation Plot

plt.figure(figsize=(18,9))
matrix = np.triu(dataset.corr())
sns.heatmap(dataset.corr(),annot=True,linewidths=.8,mask=(matrix),cmap="rocket")

#%% Some Distribution Plots

def distributionPlot(dataset):
    """ 
    """
    fig = plt.figure(figsize=(15,9))
    for i in tqdm_notebook(range(0, len(dataset.columns)), desc = 'Your plots are being ready'):
        fig.add_subplot(np.ceil(len(dataset.columns)/3), 3, i+1)
        sns.distplot(
            dataset.iloc[:, i], color="lightcoral", rug=True)
        fig.tight_layout(pad=3.0)

plot_data = dataset.drop(["Potability"],axis=1)
distributionPlot(plot_data)

#%% Pairplots
sns.pairplot(dataset, hue="Potability", palette="husl")






















