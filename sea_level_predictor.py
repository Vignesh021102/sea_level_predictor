import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
sns.set()

def draw_plot():
    data = pd.read_csv("./epa-sea-level.csv")
    data["CSIRO Adjusted Sea Level"] = data["CSIRO Adjusted Sea Level"].apply(lambda x: round(x,7))
  
    model1 = stats.linregress(data['Year'],data['CSIRO Adjusted Sea Level'])
    model2 = stats.linregress(data[data['Year']>=2000]['Year'],data[data['Year']>=2000]['CSIRO Adjusted Sea Level'])
    x1 = np.arange(1880,2051,1)
    yhat1 = (model1.slope*x1)+model1.intercept
    x2 = np.arange(2000,2051,1)
    yhat2 = (model2.slope*x2)+model2.intercept
    
    #plotting graph
    
    fig,ax = plt.subplots(1,1,figsize=(10,10))
    ax.scatter(data['Year'],data['CSIRO Adjusted Sea Level'])
    ax.plot(x1,yhat1,c='red')
    ax.plot(x2,yhat2,c='green')
    ax.set(title="Rise in Sea Level",ylabel='Sea Level (inches)',xlabel='Year')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()