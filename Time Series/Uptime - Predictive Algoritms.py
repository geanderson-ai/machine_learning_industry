
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from fbprophet import Prophet
import matplotlib as plt
from sklearn.metrics import mean_absolute_error, accuracy_score


# In[2]:


# American Falls
americanfalls = pd.read_csv('americanfalls.csv', low_memory=False)
american_uptime =  (americanfalls.loc[(americanfalls['Super Reason'] == 'Uptime')].groupby(['Logical Date'])['Hours'].sum())/(len(americanfalls.Asset.unique()))
american_up_forecast = pd.DataFrame({'ds':american_uptime.index, 'y':american_uptime.values})
#train = american_up_forecast.iloc[0:62]
#test = american_up_forecast[63:79]
american_up_forecast['y'] = np.log(american_up_forecast['y'])
american_up_forecast.set_index('ds')
m = Prophet()
m.fit(american_up_forecast)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
forecast_adjust = np.exp(forecast[['yhat']])
y_true = american_up_forecast.y
y_pred = forecast_adjust.yhat[0:79]
# Accuracy score
accuracy_score(y_true.round(0), y_pred.round(0))
# MAE output is non-negative floating point. The best value is 0.0.
mean_absolute_error(y_true, y_pred)
# ROOT MEAN SQUARE output is non-negative floating point. The best value is 0.0.
rms = np.sqrt(np.mean((forecast.yhat)**2))


# In[3]:


m.plot(forecast)


# In[5]:


# Boardman
boardman = pd.read_csv('boardman.csv', low_memory=False)
boardman_uptime =  (boardman.loc[(boardman['Super Reason'] == 'Uptime')].groupby(['Logical Date'])['Hours'].sum())/(len(boardman.Asset.unique()))
boardman_up_forecast = pd.DataFrame({'ds':boardman_uptime.index, 'y':boardman_uptime.values})
#train = boardman_up_forecast.iloc[0:62]
#test = boardman_up_forecast[63:79]
boardman_up_forecast['y'] = np.log(boardman_up_forecast['y'])
boardman_up_forecast.set_index('ds')
m = Prophet()
m.fit(boardman_up_forecast)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
forecast_adjust = np.exp(forecast[['yhat']])
y_true = boardman_up_forecast.y
y_pred = forecast_adjust.yhat[0:76]
# Accuracy score
accuracy_score(y_true.round(0), y_pred.round(0))
# MAE output is non-negative floating point. The best value is 0.0.
mean_absolute_error(y_true, y_pred)
# ROOT MEAN SQUARE output is non-negative floating point. The best value is 0.0.
rms = np.sqrt(np.mean((forecast.yhat)**2))


# In[6]:


m.plot(forecast)


# In[10]:


# Connell
connell = pd.read_csv('connell.csv', low_memory=False)
connell_uptime =  (connell.loc[(connell['Super Reason'] == 'Uptime')].groupby(['Logical Date'])['Hours'].sum())/(len(connell.Asset.unique()))
connell_up_forecast = pd.DataFrame({'ds':connell_uptime.index, 'y':connell_uptime.values})
connell_up_forecast['y'] = np.log(connell_up_forecast['y'])
connell_up_forecast.set_index('ds')
m = Prophet()
m.fit(connell_up_forecast)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
forecast_adjust = np.exp(forecast[['yhat']])
y_true = connell_up_forecast.y
y_pred = forecast_adjust.yhat[0:87]
# Accuracy score
accuracy_score(y_true.round(0), y_pred.round(0))
# MAE output is non-negative floating point. The best value is 0.0.
mean_absolute_error(y_true, y_pred)
# ROOT MEAN SQUARE output is non-negative floating point. The best value is 0.0.
rms = np.sqrt(np.mean((forecast.yhat)**2))


# In[11]:


m.plot(forecast)


# In[14]:


# Delhi
delhi = pd.read_csv('delhi.csv', low_memory=False)
delhi_uptime =  (delhi.loc[(delhi['Super Reason'] == 'Uptime')].groupby(['Logical Date'])['Hours'].sum())/(len(delhi.Asset.unique()))
delhi_up_forecast = pd.DataFrame({'ds':delhi_uptime.index, 'y':delhi_uptime.values})
delhi_up_forecast['y'] = np.log(delhi_up_forecast['y'])
delhi_up_forecast.set_index('ds')
m = Prophet()
m.fit(delhi_up_forecast)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
forecast_adjust = np.exp(forecast[['yhat']])
y_true = delhi_up_forecast.y
y_pred = forecast_adjust.yhat[0:86]
# Accuracy score
accuracy_score(y_true.round(0), y_pred.round(0))
# MAE output is non-negative floating point. The best value is 0.0.
mean_absolute_error(y_true, y_pred)
# ROOT MEAN SQUARE output is non-negative floating point. The best value is 0.0.
rms = np.sqrt(np.mean((forecast.yhat)**2))


# In[15]:


m.plot(forecast)


# In[18]:


# Park Rapids
park_rapids = pd.read_csv('park_rapids.csv', low_memory=False)
park_rapids_uptime =  (park_rapids.loc[(park_rapids['Super Reason'] == 'Uptime')].groupby(['Logical Date'])['Hours'].sum())/(len(park_rapids.Asset.unique()))
park_rapids_up_forecast = pd.DataFrame({'ds':park_rapids_uptime.index, 'y':park_rapids_uptime.values})
park_rapids_up_forecast['y'] = np.log(park_rapids_up_forecast['y'])
park_rapids_up_forecast.set_index('ds')
m = Prophet()
m.fit(park_rapids_up_forecast)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
forecast_adjust = np.exp(forecast[['yhat']])
y_true = park_rapids_up_forecast.y
y_pred = forecast_adjust.yhat[0:78]
# Accuracy score
accuracy_score(y_true.round(0), y_pred.round(0))
# MAE output is non-negative floating point. The best value is 0.0.
mean_absolute_error(y_true, y_pred)
# ROOT MEAN SQUARE output is non-negative floating point. The best value is 0.0.
rms = np.sqrt(np.mean((forecast.yhat)**2))


# In[19]:


m.plot(forecast)


# In[21]:


# Pasco
pasco = pd.read_csv('pasco.csv', low_memory=False)
pasco_uptime =  (pasco.loc[(pasco['Super Reason'] == 'Uptime')].groupby(['Logical Date'])['Hours'].sum())/(len(park_rapids.Asset.unique()))
pasco_up_forecast = pd.DataFrame({'ds':pasco_uptime.index, 'y':pasco_uptime.values})
pasco_up_forecast['y'] = np.log(pasco_up_forecast['y'])
pasco_up_forecast.set_index('ds')
m = Prophet()
m.fit(pasco_up_forecast)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
forecast_adjust = np.exp(forecast[['yhat']])
y_true = pasco_up_forecast.y
y_pred = forecast_adjust.yhat[0:83]
# Accuracy score
accuracy_score(y_true.round(0), y_pred.round(0))
# MAE output is non-negative floating point. The best value is 0.0.
mean_absolute_error(y_true, y_pred)
# ROOT MEAN SQUARE output is non-negative floating point. The best value is 0.0.
rms = np.sqrt(np.mean((forecast.yhat)**2))


# In[22]:


m.plot(forecast)


# In[24]:


# Richland 
richland = pd.read_csv('richland.csv', low_memory=False)
richland_uptime =  (richland.loc[(richland['Super Reason'] == 'Uptime')].groupby(['Logical Date'])['Hours'].sum())/(len(park_rapids.Asset.unique()))
richland_up_forecast = pd.DataFrame({'ds':richland_uptime.index, 'y':richland_uptime.values})
richland_up_forecast['y'] = np.log(richland_up_forecast['y'])
richland_up_forecast.set_index('ds')
m = Prophet()
m.fit(richland_up_forecast)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
forecast_adjust = np.exp(forecast[['yhat']])
y_true = richland_up_forecast.y
y_pred = forecast_adjust.yhat[0:76]
# Accuracy score
accuracy_score(y_true.round(0), y_pred.round(0))
# MAE output is non-negative floating point. The best value is 0.0.
mean_absolute_error(y_true, y_pred)
# ROOT MEAN SQUARE output is non-negative floating point. The best value is 0.0.
rms = np.sqrt(np.mean((forecast.yhat)**2))


# In[25]:


m.plot(forecast)

