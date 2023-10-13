import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('datas.csv')
sal = list(data.Salary)
yoe = list(data.YearsExperience)
xm = np.mean(yoe)
ym = np.mean(sal)
cov = np.cov(yoe,sal)[0][1]
varx = np.var(yoe)
m = cov/varx
c = ym-m*xm
x = np.linspace(0,10,1000)
y = m*x +c
plt.scatter(yoe,sal)
plt.plot(x,y)
plt.show()