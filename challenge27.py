import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def climate_plot():
    df_climate = pd.read_excel("ClimateChange.xlsx", sheetname='Data')
    data1 = df_climate[df_climate['Series code'] == 'EN.ATM.CO2E.KT'].set_index('Country code')
    data1 = data1.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    data1 = data1.replace({'..':pd.np.NaN})
    data1 = data1.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)  
    
    data2 = df_climate[df_climate['Series code'] == 'EN.ATM.METH.KT.CE'].set_index('Country code')
    data2 = data2.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    data2 = data2.replace({'..':pd.np.NaN})
    data2 = data2.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)  
    
    data3 = df_climate[df_climate['Series code'] == 'EN.ATM.NOXE.KT.CE'].set_index('Country code')
    data3 = data3.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    data3 = data3.replace({'..':pd.np.NaN})
    data3 = data3.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)  
    
    data4 = df_climate[df_climate['Series code'] == 'EN.ATM.GHGO.KT.CE'].set_index('Country code')
    data4 = data4.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    data4 = data4.replace({'..':pd.np.NaN})
    data4 = data4.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1) 
    
    data5 = df_climate[df_climate['Series code'] == 'EN.CLC.GHGR.MT.CE'].set_index('Country code')
    data5 = data5.drop(['Country name','Series code','Series name','SCALE','Decimals'],axis=1)
    data5 = data5.replace({'..':pd.np.NaN})
    data5 = data5.fillna(method='ffill', axis=1).fillna(method='bfill', axis=1)  
    
    gas_data = data1 + data2 + data3 + data4 + data5    
    gas_result = gas_data.sum()
    gas_form = (gas_result - gas_result.min())/(gas_result.max()-gas_result.min())
    
    df_temperature = pd.read_excel("GlobalTemperature.xlsx", sheetname='GlobalTemperatures')
    land_average = pd.Series(df_temperature['Land Average Temperature'].values, index=pd.to_datetime(df_temperature['Date']))
    land_and_ocean_average =  pd.Series(df_temperature['Land And Ocean Average Temperature'].values, index=pd.to_datetime(df_temperature['Date']))
    
    new_land_average = land_average.resample('A').mean()
    new_land_average.index = new_land_average.index.year
    new_land_average_form = (new_land_average - new_land_average.min())/(new_land_average.max()-new_land_average.min())
    new_land_and_ocean_average = land_and_ocean_average.resample('A').mean()
    new_land_and_ocean_average.index = new_land_and_ocean_average.index.year
    new_land_and_ocean_average_form = (new_land_and_ocean_average - new_land_and_ocean_average.min())/(new_land_and_ocean_average.max()-new_land_and_ocean_average.min())
    
    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    xlabel_list = [x for x in range(1990, 2011)]
    ax1.plot(xlabel_list, gas_form[xlabel_list], label=r'$Total GHG$')
    ax1.plot(xlabel_list, new_land_average_form.loc[xlabel_list], label=r'$Land Average Temperature$')
    ax1.plot(xlabel_list, new_land_and_ocean_average_form.loc[xlabel_list], label=r'$Land And Ocean Average Temperature$')
    ax1.set_xlabel("Years")
    ax1.set_ylabel("Values")
    ax1.legend()

    ax2 = fig.add_subplot(2,2,2)
    xlabel_list = [x for x in range(1990, 2011)]
    ax2.bar(gas_form[xlabel_list].index - 4/15, gas_form[xlabel_list].values, width=4/15, label=r'$Total GHG$')
    ax2.bar(new_land_average_form.loc[xlabel_list].index, new_land_average_form.loc[xlabel_list].values, width=4/15, label=r'$Land Average Temperature$')
    ax2.bar(new_land_and_ocean_average_form.loc[xlabel_list].index + 4/15, new_land_and_ocean_average_form.loc[xlabel_list].values, width=4/15, label=r'$Land And Ocean Average Temperature$')
    ax2.set_xlabel("Years")
    ax2.set_ylabel("Values")
    ax2.legend()

    ax3 = fig.add_subplot(2,2,3)
    new2_land_average = land_average.resample('Q').mean()      
    new2_land_and_ocean_average = land_and_ocean_average.resample('Q').mean()   
    new2_land_average.plot(kind='area', label=r'$Land Average Temperature$', ax=ax3)
    new2_land_and_ocean_average.plot(kind='area', label=r'$Land And Ocean Average Temperature$', ax=ax3)
    ax3.set_xlabel("Quarters")
    ax3.set_ylabel("Temperature")
    ax3.legend()

    ax4 = fig.add_subplot(2,2,4)
    new3_land_average = land_average.resample('Q').mean()      
    new3_land_and_ocean_average = land_and_ocean_average.resample('Q').mean()   
    new3_land_average.plot(kind='kde', label=r'$Land Average Temperature$', ax=ax4)
    new3_land_and_ocean_average.plot(kind='kde', label=r'$Land And Ocean Average Temperature$', ax=ax4)
    ax4.set_xlabel("Values")
    ax4.set_ylabel("Values")
    ax4.legend()

    return fig

if __name__ == '__main__':
    fig = climate_plot()
    plt.show()
