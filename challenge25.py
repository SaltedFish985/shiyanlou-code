import pandas as pd
import numpy as np
def co2():  
    df_climate = pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    df_country = pd.read_excel("ClimateChange.xlsx", sheetname='Country')
    df_climate = df_climate[df_climate['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country name')
    df_climate = df_climate.drop(['Country code','Series code','Series name','SCALE','Decimals'],axis=1)
    df_climate = df_climate.replace({'..':pd.np.NaN})    
    df_climate = df_climate.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)    
    df_country = df_country.drop(['Country code','Capital city','Region','Lending category'],axis=1).set_index('Country name')      
    new_data = pd.concat([df_climate, df_country], axis=1)
    new_data = new_data.dropna(thresh=2)   
    group_list = ['High income: OECD', 'High income: nonOECD', 'Low income', 'Lower middle income', 'Upper middle income']
    sum_emissions = []
    highest_emission_country = []
    highest_emissions = []
    lowest_emission_country = []
    lowest_emissions = []
    for group in group_list:
        hcountry = new_data[new_data['Income group'] == group][[x for x in range(1990, 2012)]].sum(axis=1).argmax()
        hcountry_emission = new_data[new_data['Income group'] == group][[x for x in range(1990, 2012)]].sum(axis=1).max()
        lcountry = new_data[new_data['Income group'] == group][[x for x in range(1990, 2012)]].sum(axis=1).argmin()
        lcountry_emission = new_data[new_data['Income group'] == group][[x for x in range(1990, 2012)]].sum(axis=1).min()
        sum_emission =  new_data[new_data['Income group'] == group][[x for x in range(1990, 2012)]].sum().sum()
        sum_emissions.append(sum_emission)
        highest_emission_country.append(hcountry)
        highest_emissions.append(hcountry_emission)
        lowest_emission_country.append(lcountry)
        lowest_emissions.append(lcountry_emission)
    result_dict = {'Sum emissions':sum_emissions, 'Highest emission country':highest_emission_country, 'Highest emissions':highest_emissions, 'Lowest emission country':lowest_emission_country, 'Lowest emissions':lowest_emissions}
    results = pd.DataFrame(result_dict, index=group_list)
    results.index.name = 'Income group'
    return results

if __name__ == '__main__':
    print(co2())
