import ccxt
import pandas as pd 
import numpy as np
import plotly.graph_objects as go


bitget = ccxt.bitget()
bitso=ccxt.huobi()
aax=ccxt.aax()
####BITCOIN

bitcoin_ob_bitget=bitget.fetch_order_book("BTC/USDT",limit=50)
bitcoin_ob_bitget
bi_btc_ob_ask = pd.DataFrame(bitcoin_ob_bitget['asks'], columns = ['price ask','quantity ask'])
bi_btc_ob_bid = pd.DataFrame(bitcoin_ob_bitget['bids'], columns = ['price bid','quantity bid'])
bitcoin_obdatetime_bitget=pd.DataFrame(bitcoin_ob_bitget)
bitcoin_obdatetime_bitget
bitcoin_close_bitget=pd.DataFrame(bitget.fetch_ohlcv("BTC/USDT",timeframe="1m",limit=50),columns=["time","open","high","low","close","volume"])
bitcoin_close_bitget
datetimes=pd.DataFrame(bitcoin_obdatetime_bitget["datetime"])
bit_btc_tabla=datetimes.join(bi_btc_ob_bid).join(bi_btc_ob_ask)
bit_btc_tabla["spread"]=bit_btc_tabla.loc[:,"price ask"]-bit_btc_tabla.loc[:,"price bid"]
bit_btc_tabla["close price"]=bitcoin_close_bitget.loc[:,"close"]
bit_btc_tabla
bit_btc_tabla["symbol"]=bitcoin_obdatetime_bitget.loc[:,"symbol"]
bit_btc_tabla

bitcoin_ob_bitget=bitso.fetch_order_book("BTC/USDT",limit=20)
bitcoin_ob_bitget
bitso_btc_ob_ask = pd.DataFrame(bitcoin_ob_bitget['asks'], columns = ['price ask','quantity ask'])
bitso_btc_ob_bid = pd.DataFrame(bitcoin_ob_bitget['bids'], columns = ['price bid','quantity bid'])
bitcoin_obdatetime_bitso=pd.DataFrame(bitcoin_ob_bitget)
bitcoin_obdatetime_bitso
bitcoin_close_bitso=pd.DataFrame(bitso.fetch_ohlcv("BTC/USDT",timeframe="1m",limit=20),columns=["time","open","high","low","close","volume"])
bitcoin_close_bitso
datetimes=pd.DataFrame(bitcoin_obdatetime_bitso["datetime"])
bitso_btc_tabla=datetimes.join(bitso_btc_ob_bid).join(bitso_btc_ob_ask)
bitso_btc_tabla["spread"]=bitso_btc_tabla.loc[:,"price ask"]-bitso_btc_tabla.loc[:,"price bid"]
bitso_btc_tabla["close price"]=bitcoin_close_bitso.loc[:,"close"]
bitso_btc_tabla["symbol"]=bitcoin_obdatetime_bitso.loc[:,"symbol"]
bitso_btc_tabla

bitcoin_ob_bitget=aax.fetch_order_book("BTC/USDT",limit=50)
bitcoin_ob_bitget
aax_btc_ob_ask = pd.DataFrame(bitcoin_ob_bitget['asks'], columns = ['price ask','quantity ask'])
aax_btc_ob_bid = pd.DataFrame(bitcoin_ob_bitget['bids'], columns = ['price bid','quantity bid'])
bitcoin_obdatetime_aax=pd.DataFrame(bitcoin_ob_bitget)
bitcoin_obdatetime_aax
bitcoin_close_aax=pd.DataFrame(aax.fetch_ohlcv("BTC/USDT",timeframe="1m",limit=50),columns=["time","open","high","low","close","volume"])
bitcoin_close_aax
datetimes=pd.DataFrame(bitcoin_obdatetime_aax["datetime"])
datetimes
aax_btc_tabla=datetimes.join(aax_btc_ob_bid).join(aax_btc_ob_ask)
aax_btc_tabla
aax_btc_tabla["spread"]=aax_btc_tabla.loc[:,"price ask"]-aax_btc_tabla.loc[:,"price bid"]
aax_btc_tabla["close price"]=bitcoin_close_aax.loc[:,"close"]
aax_btc_tabla["symbol"]=bitcoin_obdatetime_aax.loc[:,"symbol"]
aax_btc_tabla

####DOGE

doge_ob_bitget=bitget.fetch_order_book("DOGE/USDT",limit=50)
doge_ob_bitget
bi_dog_ob_ask = pd.DataFrame(doge_ob_bitget['asks'], columns = ['price ask','quantity ask'])
bi_dog_ob_bid = pd.DataFrame(doge_ob_bitget['bids'], columns = ['price bid','quantity bid'])
doge_obdatetime_bitget=pd.DataFrame(doge_ob_bitget)
doge_obdatetime_bitget
doge_close_bitget=pd.DataFrame(bitget.fetch_ohlcv("DOGE/USDT",timeframe="1m",limit=50),columns=["time","open","high","low","close","volume"])
doge_close_bitget
datetimes=pd.DataFrame(doge_obdatetime_bitget["datetime"])
bit_dog_tabla=datetimes.join(bi_dog_ob_bid).join(bi_dog_ob_ask)
bit_dog_tabla["spread"]=bit_dog_tabla.loc[:,"price ask"]-bit_dog_tabla.loc[:,"price bid"]
bit_dog_tabla["close price"]=doge_close_bitget.loc[:,"close"]
bit_dog_tabla["symbol"]=doge_obdatetime_bitget.loc[:,"symbol"]
bit_dog_tabla

doge_ob_bitso=bitso.fetch_order_book("DOGE/USDT",limit=20)
doge_ob_bitso
bitso_dog_ob_ask = pd.DataFrame(doge_ob_bitso['asks'], columns = ['price ask','quantity ask'])
bitso_dog_ob_bid = pd.DataFrame(doge_ob_bitso['bids'], columns = ['price bid','quantity bid'])
doge_obdatetime_bitso=pd.DataFrame(doge_ob_bitso)
doge_obdatetime_bitso
doge_close_bitso=pd.DataFrame(bitso.fetch_ohlcv("DOGE/USDT",timeframe="1m",limit=20),columns=["time","open","high","low","close","volume"])
doge_close_bitso
datetimes=pd.DataFrame(doge_obdatetime_bitso["datetime"])
bitso_dog_tabla=datetimes.join(bitso_dog_ob_bid).join(bitso_dog_ob_ask)
bitso_dog_tabla["spread"]=bitso_dog_tabla.loc[:,"price ask"]-bitso_dog_tabla.loc[:,"price bid"]
bitso_dog_tabla["close price"]=doge_close_bitso.loc[:,"close"]
bitso_dog_tabla["symbol"]=doge_obdatetime_bitso.loc[:,"symbol"]
bitso_dog_tabla

doge_ob_aax=aax.fetch_order_book("DOGE/USDT",limit=20)
doge_ob_aax
aax_dog_ob_ask = pd.DataFrame(doge_ob_aax['asks'], columns = ['price ask','quantity ask'])
aax_dog_ob_bid = pd.DataFrame(doge_ob_aax['bids'], columns = ['price bid','quantity bid'])
doge_obdatetime_aax=pd.DataFrame(doge_ob_aax)
doge_obdatetime_aax
doge_close_aax=pd.DataFrame(aax.fetch_ohlcv("DOGE/USDT",timeframe="1m",limit=20),columns=["time","open","high","low","close","volume"])
doge_close_aax
datetimes=pd.DataFrame(doge_obdatetime_aax["datetime"])
aax_dog_tabla=datetimes.join(aax_dog_ob_bid).join(aax_dog_ob_ask)
aax_dog_tabla["spread"]=aax_dog_tabla.loc[:,"price ask"]-aax_dog_tabla.loc[:,"price bid"]
aax_dog_tabla["close price"]=doge_close_aax.loc[:,"close"]
aax_dog_tabla["symbol"]=doge_obdatetime_aax.loc[:,"symbol"]
aax_dog_tabla

#####SHIB

shiba_ob_bitget=bitget.fetch_order_book("SHIB/USDT",limit=50)
shiba_ob_bitget
bi_shiba_ob_ask = pd.DataFrame(shiba_ob_bitget['asks'], columns = ['price ask','quantity ask'])
bi_shiba_ob_bid = pd.DataFrame(shiba_ob_bitget['bids'], columns = ['price bid','quantity bid'])
shiba_obdatetime_bitget=pd.DataFrame(shiba_ob_bitget)
shiba_obdatetime_bitget
shiba_close_bitget=pd.DataFrame(bitget.fetch_ohlcv("SHIB/USDT",timeframe="1m",limit=50),columns=["time","open","high","low","close","volume"])
shiba_close_bitget
datetimes=pd.DataFrame(shiba_obdatetime_bitget["datetime"])
bit_shiba_tabla=datetimes.join(bi_shiba_ob_bid).join(bi_shiba_ob_ask)
bit_shiba_tabla["spread"]=bit_shiba_tabla.loc[:,"price ask"]-bit_shiba_tabla.loc[:,"price bid"]
bit_shiba_tabla["close price"]=shiba_close_bitget.loc[:,"close"]
bit_shiba_tabla["symbol"]=shiba_obdatetime_bitget.loc[:,"symbol"]
bit_shiba_tabla

shiba_ob_bitso=bitso.fetch_order_book("SHIB/USDT",limit=20)
shiba_ob_bitso
bitso_shiba_ob_ask = pd.DataFrame(shiba_ob_bitso['asks'], columns = ['price ask','quantity ask'])
bitso_shiba_ob_bid = pd.DataFrame(shiba_ob_bitso['bids'], columns = ['price bid','quantity bid'])
shiba_obdatetime_bitso=pd.DataFrame(shiba_ob_bitso)
shiba_obdatetime_bitso
shiba_close_bitso=pd.DataFrame(bitso.fetch_ohlcv("SHIB/USDT",timeframe="1m",limit=20),columns=["time","open","high","low","close","volume"])
shiba_close_bitso
datetimes=pd.DataFrame(shiba_obdatetime_bitso["datetime"])
bitso_shiba_tabla=datetimes.join(bitso_shiba_ob_bid).join(bitso_shiba_ob_ask)
bitso_shiba_tabla["spread"]=bitso_shiba_tabla.loc[:,"price ask"]-bitso_shiba_tabla.loc[:,"price bid"]
bitso_shiba_tabla["close price"]=shiba_close_bitso.loc[:,"close"]
bitso_shiba_tabla["symbol"]=shiba_obdatetime_bitso.loc[:,"symbol"]
bitso_shiba_tabla

shiba_ob_aax=aax.fetch_order_book("SHIB/USDT",limit=50)
shiba_ob_aax
aax_shiba_ob_ask = pd.DataFrame(shiba_ob_aax['asks'], columns = ['price ask','quantity ask'])
aax_shiba_ob_bid = pd.DataFrame(shiba_ob_aax['bids'], columns = ['price bid','quantity bid'])
shiba_obdatetime_aax=pd.DataFrame(shiba_ob_aax)
shiba_obdatetime_aax
shiba_close_aax=pd.DataFrame(aax.fetch_ohlcv("SHIB/USDT",timeframe="1m",limit=50),columns=["time","open","high","low","close","volume"])
shiba_close_aax
datetimes=pd.DataFrame(shiba_obdatetime_aax["datetime"])
aax_shiba_tabla=datetimes.join(aax_shiba_ob_bid).join(aax_shiba_ob_ask)
aax_shiba_tabla["spread"]=aax_shiba_tabla.loc[:,"price ask"]-aax_shiba_tabla.loc[:,"price bid"]
aax_shiba_tabla["close price"]=shiba_close_aax.loc[:,"close"]
aax_shiba_tabla["symbol"]=shiba_obdatetime_aax.loc[:,"symbol"]
aax_shiba_tabla

####Diccionario

currencies={"BTC/USDT":{"BITGET":bit_btc_tabla,"HUOBI":bitso_btc_tabla,"AAX":aax_btc_tabla},"DOGE/USDT":{"BITGET":bit_dog_tabla,"HUOBI":bitso_dog_tabla,"AAX":aax_dog_tabla},"SHIB/USDT":{"BITGET":bit_shiba_tabla,"HUOBI":bitso_shiba_tabla,"AAX":aax_shiba_tabla}}



####PUNTO 2


###levels
###Bitget
bit_btc_tabla["total volume"]=(bit_btc_tabla.loc[:,"quantity ask"]+bit_btc_tabla.loc[:,"quantity bid"])
bit_btc_tabla=bit_btc_tabla.sort_values(by=["spread"])
bit_btc_tabla["level"]=list(range(1,51))
bit_btc_tabla

bit_dog_tabla["total volume"]=(bit_dog_tabla.loc[:,"quantity ask"]+bit_dog_tabla.loc[:,"quantity bid"])
bit_dog_tabla=bit_dog_tabla.sort_values(by=["spread"])
bit_dog_tabla["level"]=list(range(1,51))
bit_dog_tabla

bit_shiba_tabla["total volume"]=(bit_shiba_tabla.loc[:,"quantity ask"]+bit_shiba_tabla.loc[:,"quantity bid"])
bit_shiba_tabla=bit_shiba_tabla.sort_values(by=["spread"])
bit_shiba_tabla["level"]=list(range(1,51))
bit_shiba_tabla
###Bitso
bitso_btc_tabla["total volume"]=(bitso_btc_tabla.loc[:,"quantity ask"]+bitso_btc_tabla.loc[:,"quantity bid"])
bitso_btc_tabla=bitso_btc_tabla.sort_values(by=["spread"])
bitso_btc_tabla["level"]=list(range(1,21))
bitso_btc_tabla


bitso_dog_tabla["total volume"]=(bitso_dog_tabla.loc[:,"quantity ask"]+bitso_dog_tabla.loc[:,"quantity bid"])
bitso_dog_tabla=bitso_dog_tabla.sort_values(by=["spread"])
bitso_dog_tabla["level"]=list(range(1,21))
bitso_dog_tabla

bitso_shiba_tabla["total volume"]=(bitso_shiba_tabla.loc[:,"quantity ask"]+bitso_shiba_tabla.loc[:,"quantity bid"])
bitso_shiba_tabla=bitso_shiba_tabla.sort_values(by=["spread"])
bitso_shiba_tabla["level"]=list(range(1,21))
bitso_shiba_tabla

aax_btc_tabla["total volume"]=(aax_btc_tabla.loc[:,"quantity ask"]+aax_btc_tabla.loc[:,"quantity bid"])
aax_btc_tabla=aax_btc_tabla.sort_values(by=["spread"])
aax_btc_tabla["level"]=list(range(1,51))
aax_btc_tabla

aax_dog_tabla["total volume"]=(aax_dog_tabla.loc[:,"quantity ask"]+aax_dog_tabla.loc[:,"quantity bid"])
aax_dog_tabla=aax_dog_tabla.sort_values(by=["spread"])
aax_dog_tabla["level"]=list(range(1,21))
aax_dog_tabla

aax_shiba_tabla["total volume"]=(aax_shiba_tabla.loc[:,"quantity ask"]+aax_shiba_tabla.loc[:,"quantity bid"])
aax_shiba_tabla=aax_shiba_tabla.sort_values(by=["spread"])
aax_shiba_tabla["level"]=list(range(1,51))
aax_shiba_tabla

close_prices=pd.concat([bit_btc_tabla,bit_dog_tabla,bit_shiba_tabla,bitso_btc_tabla,bitso_dog_tabla,bitso_shiba_tabla,aax_btc_tabla,aax_dog_tabla,aax_shiba_tabla])
close_prices=close_prices.loc[:,"close price"]
close_prices

spread_punto_3=pd.concat([bit_btc_tabla,bit_dog_tabla,bit_shiba_tabla,bitso_btc_tabla,bitso_dog_tabla,bitso_shiba_tabla,aax_btc_tabla,aax_dog_tabla,aax_shiba_tabla])
spread_punto_3=spread_punto_3.loc[:,"spread"]
spread_punto_3






#####vwaps bitget
vwap_bitcoin_bitget=bitcoin_close_bitget.loc[:,"volume"]*((bitcoin_close_bitget.loc[:,"high"]+bitcoin_close_bitget.loc[:,"low"]+bitcoin_close_bitget.loc[:,"close"])/3)/bitcoin_close_bitget.loc[:,"volume"]
len(vwap_bitcoin_bitget)
vwap_doge_bitget=doge_close_bitget.loc[:,"volume"]*((doge_close_bitget.loc[:,"high"]+doge_close_bitget.loc[:,"low"]+doge_close_bitget.loc[:,"close"])/3)/doge_close_bitget.loc[:,"volume"]
len(vwap_doge_bitget)
vwap_shiba_bitget=shiba_close_bitget.loc[:,"volume"]*((shiba_close_bitget.loc[:,"high"]+shiba_close_bitget.loc[:,"low"]+shiba_close_bitget.loc[:,"close"])/3)/shiba_close_bitget.loc[:,"volume"]
len(vwap_shiba_bitget)

#### vwaps bitso
vwap_bitcoin_bitso=bitcoin_close_bitso.loc[:,"volume"]*((bitcoin_close_bitso.loc[:,"high"]+bitcoin_close_bitso.loc[:,"low"]+bitcoin_close_bitso.loc[:,"close"])/3)/bitcoin_close_bitso.loc[:,"volume"]
len(vwap_bitcoin_bitso)
vwap_doge_bitso=doge_close_bitso.loc[:,"volume"]*((doge_close_bitso.loc[:,"high"]+doge_close_bitso.loc[:,"low"]+doge_close_bitso.loc[:,"close"])/3)/doge_close_bitso.loc[:,"volume"]
len(vwap_doge_bitso)
vwap_shiba_bitso=shiba_close_bitso.loc[:,"volume"]*((shiba_close_bitso.loc[:,"high"]+shiba_close_bitso.loc[:,"low"]+shiba_close_bitso.loc[:,"close"])/3)/shiba_close_bitso.loc[:,"volume"]
len(vwap_shiba_bitso)

###vwaps aax
vwap_bitcoin_aax=bitcoin_close_aax.loc[:,"volume"]*((bitcoin_close_aax.loc[:,"high"]+bitcoin_close_aax.loc[:,"low"]+bitcoin_close_aax.loc[:,"close"])/3)/bitcoin_close_aax.loc[:,"volume"]
len(vwap_bitcoin_aax)
vwap_doge_aax=doge_close_aax.loc[:,"volume"]*((doge_close_aax.loc[:,"high"]+doge_close_aax.loc[:,"low"]+doge_close_aax.loc[:,"close"])/3)/doge_close_aax.loc[:,"volume"]
len(vwap_doge_aax)
vwap_shiba_aax=shiba_close_aax.loc[:,"volume"]*((shiba_close_aax.loc[:,"high"]+shiba_close_aax.loc[:,"low"]+shiba_close_aax.loc[:,"close"])/3)/shiba_close_aax.loc[:,"volume"]
len(vwap_shiba_aax)


###vwaps concatenados
vwaps_bitget=pd.concat([vwap_bitcoin_bitget,vwap_doge_bitget,vwap_shiba_bitget])
len(vwaps_bitget)
vwaps_bitso=pd.concat([vwap_bitcoin_bitso,vwap_doge_bitso,vwap_shiba_bitso])
len(vwaps_bitso)
vwaps_aax=pd.concat([vwap_bitcoin_aax,vwap_doge_aax,vwap_shiba_aax])
len(vwaps_aax)

####mid prices
###bitget
mid_pr_bitcoin_bitget=(bit_btc_tabla.loc[:,"price ask"]+bit_btc_tabla.loc[:,"price bid"])/2
mid_pr_bitcoin_bitget
mid_pr_doge_bitget=(bit_dog_tabla.loc[:,"price ask"]+bit_dog_tabla.loc[:,"price bid"])/2
mid_pr_shiba_bitget=(bit_shiba_tabla.loc[:,"price ask"]+bit_shiba_tabla.loc[:,"price bid"])/2

#####bitso
mid_pr_bitcoin_bitso=(bitso_btc_tabla.loc[:,"price ask"]+bitso_btc_tabla.loc[:,"price bid"])/2
mid_pr_bitcoin_bitso
mid_pr_doge_bitso=(bitso_dog_tabla.loc[:,"price ask"]+bitso_dog_tabla.loc[:,"price bid"])/2
mid_pr_shiba_bitso=(bitso_shiba_tabla.loc[:,"price ask"]+bitso_shiba_tabla.loc[:,"price bid"])/2


###aax
mid_pr_bitcoin_aax=(aax_btc_tabla.loc[:,"price ask"]+aax_btc_tabla.loc[:,"price bid"])/2
mid_pr_bitcoin_aax
mid_pr_doge_aax=(aax_dog_tabla.loc[:,"price ask"]+aax_dog_tabla.loc[:,"price bid"])/2
mid_pr_shiba_aax=(aax_shiba_tabla.loc[:,"price ask"]+aax_shiba_tabla.loc[:,"price bid"])/2

###concatenado
mid_pr_bitget=pd.concat([mid_pr_bitcoin_bitget,mid_pr_doge_bitget,mid_pr_shiba_bitget])
mid_pr_bitget
mid_pr_bitso=pd.concat([mid_pr_bitcoin_bitso,mid_pr_doge_bitso,mid_pr_shiba_bitso])
mid_pr_bitso
mid_pr_aax=pd.concat([mid_pr_bitcoin_aax,mid_pr_doge_aax,mid_pr_shiba_aax])


bitget_2=pd.concat([bit_btc_tabla,bit_dog_tabla,bit_shiba_tabla])
bitget_2
bitget_2=pd.DataFrame(bitget_2,columns=["exchange","datetime","symbol","level","quantity bid","quantity ask","total volume","mid price"])
bitget_2
bitget_2["exchange"]=bitget_2.loc[:,"exchange"].fillna("Bitget")
bitget_2["vwap"]=np.array(vwaps_bitget)
bitget_2["total volume"]=bitget_2.loc[:,"quantity ask"]+bitget_2.loc[:,"quantity bid"]
bitget_2["mid price"]=mid_pr_bitget
bitget_2


bitso_2=pd.concat([bitso_btc_tabla,bitso_dog_tabla,bitso_shiba_tabla])
bitso_2=pd.DataFrame(bitso_2,columns=["exchange","datetime","symbol","level","quantity bid","quantity ask","total volume","mid price","vwap"])
bitso_2["exchange"]=bitso_2.loc[:,"exchange"].fillna("Bitso")
bitso_2["total volume"]=bitso_2.loc[:,"quantity ask"]+bitso_2.loc[:,"quantity bid"]
bitso_2["vwap"]=np.array(vwaps_bitso)
bitso_2["mid price"]=mid_pr_bitso
bitso_2

aax_2=pd.concat([aax_btc_tabla,aax_dog_tabla,aax_shiba_tabla])
aax_2=pd.DataFrame(aax_2,columns=["exchange","datetime","symbol","level","quantity bid","quantity ask","total volume","mid price","vwap"])
aax_2["exchange"]=aax_2.loc[:,"exchange"].fillna("AAX")
aax_2["total volume"]=aax_2.loc[:,"quantity bid"]+aax_2.loc[:,"quantity ask"]
aax_2
aax_2["vwap"]=np.array(vwaps_aax)
aax_2["mid price"]=mid_pr_aax
aax_2



punto_2=pd.concat([bitget_2,bitso_2,aax_2])
bitget_2.head()
punto_2

####visualizations
mid_prices_graph_bitcoin=go.Figure()
mid_prices_graph_bitcoin.add_trace(go.Scatter(y=bitcoin_obdatetime_bitget.loc[:,"datetime"],x=mid_pr_bitcoin_bitget,mode="lines", name="MP BTC/USDT BITGET"))
mid_prices_graph_bitcoin.add_trace(go.Scatter(y=bitcoin_obdatetime_bitso.loc[:,"datetime"],x=mid_pr_bitcoin_bitso, name="MP BTC/USDT BITSO"))
mid_prices_graph_bitcoin.add_trace(go.Scatter(y=bitcoin_obdatetime_aax.loc[:,"datetime"],x=mid_pr_bitcoin_aax, name="MP BTC/USDT AAX"))
##mid_prices_graph_bitcoin.show()

mid_prices_graph_doge=go.Figure()
mid_prices_graph_doge.add_trace(go.Scatter(y=doge_obdatetime_bitget.loc[:,"datetime"],x=mid_pr_doge_bitget,mode="lines", name=" MP DOGE/USDT BITGET"))
mid_prices_graph_doge.add_trace(go.Scatter(y=doge_obdatetime_bitso.loc[:,"datetime"],x=mid_pr_doge_bitso, name="MP DOGE/USDT BITSO"))
mid_prices_graph_doge.add_trace(go.Scatter(y=doge_obdatetime_aax.loc[:,"datetime"],x=mid_pr_doge_aax, name="MP DOGE/USDT AAX"))
##mid_prices_graph_doge.show()

mid_prices_graph_shiba=go.Figure()
mid_prices_graph_shiba.add_trace(go.Scatter(y=shiba_obdatetime_bitget.loc[:,"datetime"],x=mid_pr_shiba_bitget,mode="lines", name=" MP SHIB/USDT BITGET"))
mid_prices_graph_shiba.add_trace(go.Scatter(y=shiba_obdatetime_bitso.loc[:,"datetime"],x=mid_pr_shiba_bitso, name="MP SHIB/USDT BITSO"))
mid_prices_graph_shiba.add_trace(go.Scatter(y=shiba_obdatetime_aax.loc[:,"datetime"],x=mid_pr_shiba_aax, name="MP SHIB/USDT AAX"))
##mid_prices_graph_shiba.show()


#####Punto 3

efective_spread=pd.DataFrame(punto_2,columns=(["datetime","symbol"]))
efective_spread["close price"]=close_prices
efective_spread["spread"]=spread_punto_3
efective_spread
resagada_5=(efective_spread.shift(periods=5)).fillna(0)
efective_spread=(efective_spread.shift(periods=2)).fillna(0)
efective_spread
delta_pt=np.array([efective_spread.iloc[:,2]])
serie_resagada_5=np.array([resagada_5.iloc[:,2]])
for i in serie_resagada_5:
    delta_pt_1=serie_resagada_5.flat[:-1]-serie_resagada_5.flat[1:]
delta_pt=np.ediff1d(delta_pt)
delta_pt=pd.DataFrame(delta_pt)
delta_pt_1=pd.DataFrame(delta_pt_1)
cov=np.cov(delta_pt,delta_pt_1)
efective_spread=efective_spread
efective_spread["delta_pt"]=delta_pt.iloc[1:,0]
efective_spread["delta pt -1"]=delta_pt_1
efective_spread



