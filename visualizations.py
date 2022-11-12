import datalab4 as dt4
import plotly.graph_objects as go

####visualizations
mid_prices_graph_bitcoin=go.Figure()
mid_prices_graph_bitcoin.add_trace(go.Scatter(y=dt4.mid_pr_bitcoin_bitget,mode="lines", name="MP BTC/USDT BITGET"))
mid_prices_graph_bitcoin.add_trace(go.Scatter(y=dt4.mid_pr_bitcoin_bitso, name="MP BTC/USDT HUOBI"))
mid_prices_graph_bitcoin.add_trace(go.Scatter(y=dt4.mid_pr_bitcoin_aax, name="MP BTC/USDT AAX"))
mid_prices_graph_bitcoin

mid_prices_graph_doge=go.Figure()
mid_prices_graph_doge.add_trace(go.Scatter(y=dt4.mid_pr_doge_bitget,mode="lines", name=" MP DOGE/USDT BITGET"))
mid_prices_graph_doge.add_trace(go.Scatter(y=dt4.mid_pr_doge_bitso, name="MP DOGE/USDT HUOBI"))
mid_prices_graph_doge.add_trace(go.Scatter(y=dt4.mid_pr_doge_aax, name="MP DOGE/USDT AAX"))
mid_prices_graph_doge

mid_prices_graph_shiba=go.Figure()
mid_prices_graph_shiba.add_trace(go.Scatter(y=dt4.mid_pr_shiba_bitget,mode="lines", name=" MP SHIB/USDT BITGET"))
mid_prices_graph_shiba.add_trace(go.Scatter(y=dt4.mid_pr_shiba_bitso, name="MP SHIB/USDT HUOBI"))
mid_prices_graph_shiba.add_trace(go.Scatter(y=dt4.mid_pr_shiba_aax, name="MP SHIB/USDT AAX"))
mid_prices_graph_shiba