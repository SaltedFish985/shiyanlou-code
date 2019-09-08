import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

def Temperature():
    GST = pd.read_csv("GlobalSurfaceTemperature.csv").set_index('Year')
    GG = pd.read_csv("GreenhouseGas.csv").set_index('Year')
    CO2 = pd.read_csv("CO2ppm.csv").set_index('Year')
    data = pd.concat([GST, GG, CO2], axis=1)
    
    feature = data.iloc[:, 3:7].fillna(method='ffill').fillna(method='bfill')    
    feature_train = feature.loc[1970:2010]
    feature_target = feature.loc[2011:2017]

    Median_target = data.iloc[:, 0]
    Median_train = Median_target.loc[1970:2010]
    model1 = LinearRegression()
    model1.fit(feature_train, Median_train)
    Median_data = list(model1.predict(feature_target))

    Upper_target = data.iloc[:, 1]
    Upper_train = Upper_target.loc[1970:2010]
    model2 = LinearRegression()
    model2.fit(feature_train, Upper_train)
    Upper_data = list(model2.predict(feature_target))

    Lower_target = data.iloc[:, 2]
    Lower_train = Upper_target.loc[1970:2010]
    model3 = LinearRegression()
    model3.fit(feature_train, Lower_train)
    Lower_data = list(model3.predict(feature_target))
   
    return Upper_data, Median_data, Lower_data

if __name__ == '__main__':
    print(Temperature())
