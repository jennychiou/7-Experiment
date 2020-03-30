"""
@author: Danyal

The following code plots a scatter plot for distribution 
of features against emotional classes (normalized values)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Emotion_features.csv')
feature = data.ix[:, 'tempo':]
labels = list(feature)
color = ['red' if l==1 else 'green' if l==2 else 'blue' if l==3 else 'orange' for l in data['label']]

plt.style.use('ggplot')
for label in feature:
    # Normalization (value-mean)/(max-min)
    feature[label] = np.abs(feature[label]-feature[label].mean())/(feature[label].max()-feature[label].min()).astype(np.float64)


    plt.figure(figsize=(12,12))
    plt.xlabel('Class')
    plt.ylabel(label)
    plt.title(label + ' Distribution')

    total = 0
    count = 0
    for row in data['label']:
      if (data['label'] == 1):
        plt.scatter(data['label'], feature[label], color=color)        
      total += row
      count += 1 
    average = total/count
    print(average)
    
    plt.savefig('Figure\\ScatterPlot\\Normalized\\' + label)
    plt.show()
    plt.clf()
    
