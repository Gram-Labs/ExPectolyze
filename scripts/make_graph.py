import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression


data = pd.read_csv('/data/ruderferlab/sandbox/grahame/expecto/data/rarity2_data.tsv', delimiter='\t')
Y = data.iloc[:, 0].values.reshape(-1, 1)  # values converts it into a numpy array
X = data.iloc[:, 1].values.reshape(-1, 1)  # -1 means that calculate the dimension of rows, but have 1 column
linear_regressor = LinearRegression()  # create object for the class
linear_regressor.fit(X, Y)  # perform linear regression
Y_pred = linear_regressor.predict(X)  # make predictions

plt.scatter(X, Y)
plt.plot(X, Y_pred, color='red')
plt.gca().set(title='Rarity analysis (n=1200)', xlabel='gnomAD rarity minor allele frequency', ylabel='absvalue ExPecto predictions')
plt.show()
plt.savefig('example1.png')


#cmd = "awk '{ OFS=\"\t\"; print $1, $2, $3, $4, $5 }' %s > %s" % ('newName', finalName)

'''
import csv
output = csv.writer(open('/data/ruderferlab/sandbox/grahame/expecto/data/rarity2_data.tsv', 'w'), delimiter = '\t')

with open ('/data/ruderferlab/sandbox/grahame/expecto/data/rarity_data.tsv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for line in reader:
        expecto = line[0]
        if expecto[0] == '-':
            expecto = float(expecto) / -1
        value = float(line[1])
        if value > 0.5:
            value = 1 - value
            output.writerow([expecto] + [value])
        else:
            output.writerow([expecto] + [value])
'''




