import datalab4 as dt4
import pandas as pd
import numpy as np


####Diccionario
currencies={"BTC/USDT":{"BITGET":dt4.bit_btc_tabla,"HUOBI":dt4.bitso_btc_tabla,"AAX":dt4.aax_btc_tabla},"DOGE/USDT":{"BITGET":dt4.bit_dog_tabla,"HUOBI":dt4.bitso_dog_tabla,"AAX":dt4.aax_dog_tabla},"SHIB/USDT":{"BITGET":dt4.bit_shiba_tabla,"HUOBI":dt4.bitso_shiba_tabla,"AAX":dt4.aax_shiba_tabla}}
currencies

### punto 2

punto_2=pd.concat([dt4.bitget_2,dt4.bitso_2,dt4.aax_2])
punto_2


efective_spread=(pd.DataFrame(punto_2,columns=(["datetime","symbol"]))).reset_index()
efective_spread=efective_spread.drop(["index"],axis=1)
efective_spread
close_prices=dt4.close_prices.reset_index()
close_prices=close_prices.drop(["index"],axis=1)
close_prices
efective_spread["close price"]=(close_prices.loc[:,"close price"])
efective_spread
spread_punto_3=dt4.spread_punto_3.reset_index()
spread_punto_3=spread_punto_3.drop(["index"],axis=1)
spread_punto_3
efective_spread["spread"]=spread_punto_3
efective_spread
efective_spread=(efective_spread.shift(periods=1)).fillna(0)
spreads_media=efective_spread["spread"].values
n=5
#calcular media móvil
spread_roll=pd.Series (spreads_media) .rolling (window = n) .mean (). iloc [n-1:]. values
spread_roll
spread_roll=pd.DataFrame(spread_roll,columns=["efective spread"])
spread_roll
efective_spread=(efective_spread.drop([0])).reset_index()
efective_spread
nuevas_filas=[0,0,0]
spread_roll=spread_roll.append(nuevas_filas,ignore_index=True)
spread_roll
spread_roll.loc[:,"efective spread"]

punto_3=efective_spread.join(spread_roll.loc[:,"efective spread"])




##delta_pt=np.array([efective_spread.iloc[:,2]])
#serie_resagada_5=np.array([resagada_5.iloc[:,2]])
#for i in serie_resagada_5:
    #delta_pt_1=serie_resagada_5.flat[:-1]-serie_resagada_5.flat[1:]
#delta_pt_1_cov=np.array([delta_pt_1])
#delta_pt_1_cov
#delta_pt=np.ediff1d(delta_pt)
#delta_pt_cov=np.array([delta_pt])
#delta_pt_cov
#delta_pt=pd.DataFrame(delta_pt)
#delta_pt_1=pd.DataFrame(delta_pt_1)
#cov=np.cov(delta_pt_cov,delta_pt_1_cov)
#efective_spread=efective_spread
#efective_spread["delta_pt"]=delta_pt.iloc[1:,0]
#efective_spread["delta pt -1"]=delta_pt_1
##efective_spread

