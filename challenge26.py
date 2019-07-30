import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def co2_gdp_plot():
    df_climate = pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    gdp_data = df_climate[df_climate['Series code'] == 'NY.GDP.MKTP.CD'].set_index('Country code')
    copy_data = df_climate[df_climate['Series code'] == 'NY.GDP.MKTP.CD']
    country_index = pd.DataFrame(copy_data['Country code'].values,index=[x for x in range(len(copy_data))],columns=['the_index'])

    gdp_data = gdp_data.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    gdp_data = gdp_data.replace({'..':pd.np.NaN})
    gdp_data = gdp_data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    gdp_data = gdp_data.fillna(0)
    gdp_result = gdp_data.sum(axis=1)
    gdp_form = (gdp_result - gdp_result.min())/(gdp_result.max()-gdp_result.min())
    
    co2_data = df_climate[df_climate['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    co2_data = co2_data.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    co2_data = co2_data.replace({'..':pd.np.NaN})
    co2_data = co2_data.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)
    co2_data = co2_data.fillna(0)
    co2_result = co2_data.sum(axis=1)
    co2_form = (co2_result - co2_result.min())/(co2_result.max()-co2_result.min())
    
    fig = plt.subplot() 
    fig.set_title("GDP-CO2")
    fig.set_xlabel("Countries")
    fig.set_ylabel("Values")
    fig.plot(list(np.arange(len(co2_form))), co2_form, label=r'$CO2-SUM$')
    fig.plot(list(np.arange(len(gdp_form))), gdp_form, label=r'$GDP-SUM$')
    country_code_list = ['CHN', 'USA', 'GBR', 'FRA','RUS']
    result_index = []
    for country_code in country_code_list:
        c = list(country_index[country_index['the_index'] == country_code].index)
        result_index += c
    plt.xticks(result_index, country_code_list, rotation=90)
    fig.legend()
    china = [round(float(co2_form[result_index[0]]), 3), round(float(gdp_form[result_index[0]]), 3)]
    return fig, china
    
        
if __name__ == '__main__':
    fig, china = co2_gdp_plot()
    print(china)
    plt.show()