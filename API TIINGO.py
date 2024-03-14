#!/usr/bin/env python
# coding: utf-8

# ---
# 
# # *EXPLORANDO A API TIINGO COM PYTHON: Dados de ações dos EUA, Forex e Criptomoedas*

# ![image.png](data:image/png;base64,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)

# Referências:
# 
# - https://www.tiingo.com/
# 
# - Dashboard de mercado
# https://app.tiingo.com/
# 
# - Suas credenciais de API:
# https://www.tiingo.com/documentation/general/overview
# 

# In[15]:


TIINGO_API_KEY = (your key here)


# ## *1. Instalações e configuração*

# In[16]:


get_ipython().system('pip install tiingo')


# In[17]:


from tiingo import TiingoClient
import pandas as pd
import plotly.graph_objects as go
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Dicionário de configurações para utilizar a API
config = {
    'api_key': TIINGO_API_KEY,
    'session': True
}

client = TiingoClient(config)


# ## *2. Obtenção básica de dados*
# 
# <br>
# 
# - Não possui dados da bolsa brasileira, apenas ADRs de empresas brasileiras negociadas internacionalmente.

# **Metadados**

# In[18]:


client.get_ticker_metadata('AAPL')


# In[19]:


client.get_ticker_metadata('VALE')


# ## *3. Cotações de stocks*
# 
# <br>
# 
# - Dados diários e intraday

# In[20]:


client.get_ticker_price('MSFT', frequency = 'daily')


# In[21]:


client.get_ticker_price('AAPL', frequency = 'weekly')


# For values of `frequency`:
# 
# <br>
# 
# - You can specify any of the end of day frequencies (**daily, weekly, monthly, and annually**) or any intraday frequency for both the ``get_ticker_price`` and ``get_dataframe`` methods.  Weekly frequencies resample to the end of day on Friday, monthly frequencies resample to the last day of the month, and annually frequencies resample to the end of day on 12-31 of each year.  The intraday frequencies are specified using an integer followed by `Min` or `Hour`, for example `30Min` or `1Hour`.

# In[22]:


# Dados intraday
prices = client.get_ticker_price('MSFT',
                        fmt = 'json',
                        startDate = '2024-01-02',
                        endDate = '2024-01-02',
                        frequency = '1min')


# In[23]:


prices


# In[24]:


prices[3]


# In[25]:


# Transformando json em DataFrame
prices = pd.DataFrame(prices)
prices


# In[26]:


prices.close.plot();


# ## *4. Todos os Ticker disponíveis*

# In[27]:


tickers = client.list_stock_tickers()


# In[28]:


tickers[0]


# In[29]:


tickers[0]['exchange']


# In[30]:


# Checando todas as exchanges disponíeveis na Tiingo
exchange = list()

for i in range(0,len(tickers)):
    j = tickers[i]['exchange']
    exchange.append(j)


# In[31]:


set(exchange)


# - **AMEX:** *NYSE American (American Stock Exchange)*
# - **ASX:** *Australian Securities Exchange*
# - **BATS:** *BATS Global Markets*
# - **CSE:** *Canadian Securities Exchange*
# - **EXPM:** *NYSE Arca Equities Feed*
# - **LSE:** *London Stock Exchange*
# - **NASDAQ:** *NASDAQ Stock Market*
# - **NMFQS:** *NASDAQ Market Feed*
# - **NYSE:** *New York Stock Exchange*
# - **NYSE ARCA:** *NYSE Arca*
# - **NYSE MKT:** *NYSE American (antigo NYSE MKT)*
# - **NYSE NAT:** *NYSE National (National Stock Exchange)*
# - **OTCBB:** *OTC Bulletin Board*
# - **OTCCE:** *OTC Markets Group's OTC Link LLC (formerly Pink Sheets LLC)*
# - **OTCGREY:** *OTC Grey Market*
# - **OTCMKTS:** *OTC Markets Group (Over-The-Counter Markets)*
# - **OTCQB:** *OTCQB Venture Market*
# - **OTCQX:** *OTCQX Best Market*
# - **PINK:** *Pink Sheets*
# - **SHE:** *Shanghai Stock Exchange*
# - **SHEB:** *Shanghai Stock Exchange B Share Market*
# - **SHG:** *Shanghai-Hong Kong Stock Connect (Stock Exchange of Hong Kong)*
# - **SHGB:** *Shanghai-Hong Kong Stock Connect B Share Market (Stock Exchange of Hong Kong)*

# ## *5. DataFrame*

# In[32]:


tsla = client.get_dataframe('TSLA',
                   startDate = '2023-01-01',
                   endDate = '2024-01-01',
                   frequency = 'daily')


# In[33]:


tsla


# In[34]:


tsla.adjClose.plot();


# In[35]:


colunas_plotar = ['adjClose','adjVolume']

tsla[colunas_plotar].plot.line(subplots = True)


# In[36]:


colunas_plotar = ['adjClose','adjOpen']

tsla[colunas_plotar].plot.line(subplots = False)


# Mais de 1 ticker ao mesmo tempo

# In[37]:


stocks = client.get_dataframe(['TSLA','MSFT','GOOG','AMZN','KO'],
                   startDate = '2023-01-01',
                   endDate = '2024-01-01',
                   metric_name = 'adjClose',
                   frequency = 'daily')


# In[38]:


stocks.plot.line();


# ## *6. Como obter dados de outras classes*

# ### FOREX

# In[39]:


data = client.get_dataframe('eurusd',
                             startDate = '2024-01-01',
                             endDate = '2024-03-13',
                             frequency = 'daily')


# In[40]:


data.drop(columns = {'adjVolume','divCash','splitFactor'},inplace = True)


# In[41]:


data.drop(columns = {'volume'},inplace = True)


# In[42]:


data


# In[43]:


# Supondo que você tenha seu DataFrame EURUSD com os dados

EURUSD = pd.DataFrame(data)
EURUSD.index = pd.to_datetime(EURUSD.index)


# In[44]:


# Criar o gráfico de candlestick
fig = go.Figure(data=[go.Candlestick(x=EURUSD.index,
                                     open=EURUSD['open'],
                                     high=EURUSD['high'],
                                     low=EURUSD['low'],
                                     close=EURUSD['close'])])

# Atualizar o layout do gráfico
fig.update_layout(title='Gráfico de Candlestick - EURUSD',
                   xaxis_title='Data',
                   yaxis_title='Preço',
                   xaxis_rangeslider_visible=False)

# Exibir o gráfico
fig.show()


# In[45]:


EURUSD.close.plot();


# In[46]:


USDBRL = client.get_dataframe('usdbrl',
                             startDate = '2024-01-01',
                             endDate = '2024-03-13',
                             frequency = 'daily')


# In[48]:


USDBRL.close.plot();


# ### Criptomoedas

# In[49]:


BTCUSD = client.get_dataframe('btcusd',
                             startDate = '2024-01-01',
                             endDate = '2024-03-13',
                             frequency = 'daily')


# In[50]:


BTCUSD.close.plot();


# In[51]:


ETH = client.get_dataframe('ethusd',
                             startDate = '2024-01-01',
                             endDate = '2024-03-13',
                             frequency = 'daily')


# In[52]:


ETH.close.plot();


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




