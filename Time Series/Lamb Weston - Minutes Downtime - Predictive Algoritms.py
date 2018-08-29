
# coding: utf-8

# In[1]:


import pandas as pd
from sklearn.model_selection import train_test_split


# In[2]:


# American Falls
americanfalls = pd.read_csv('americanfalls.csv', low_memory=False)
american_downtime =  americanfalls.loc[(americanfalls['Super Reason'] != 'Uptime')]
# Boardman
boardman = pd.read_csv('boardman.csv', low_memory=False)
boardman_downtime =  boardman.loc[(boardman['Super Reason'] != 'Uptime')]
# Connell
connell = pd.read_csv('connell.csv', low_memory=False)
connell_downtime =  connell.loc[(connell['Super Reason'] != 'Uptime')]
# Delhi
delhi = pd.read_csv('delhi.csv', low_memory=False)
delhi_downtime =  delhi.loc[(delhi['Super Reason'] != 'Uptime')]
# Park Rapids
park_rapids = pd.read_csv('park_rapids.csv', low_memory=False)
park_rapids_downtime =  park_rapids.loc[(park_rapids['Super Reason'] != 'Uptime')]
# Pasco
pasco = pd.read_csv('pasco.csv', low_memory=False)
pasco_downtime =  pasco.loc[(pasco['Super Reason'] != 'Uptime')]
# Richland 
richland = pd.read_csv('richland.csv', low_memory=False)
richland_downtime =  richland.loc[(richland['Super Reason'] != 'Uptime')]


# In[3]:


# American: create the features for model
y = american_downtime[['Minutes']]
X = american_downtime[['Asset', 'Super Reason', 'Reason Lvl1', 'Reason Lvl2', 'Shift', 'Hours']]
# dummy variables for categorical variables
X = pd.get_dummies(X)
# cross validation with train, test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.linear_model import Ridge
clf = Ridge(alpha=1.0, solver='lsqr')
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
american_predict = clf.predict(X_test)[0:30]
american_predict = pd.DataFrame(data=american_predict)


# In[4]:


american_predict.plot(figsize=(16, 10))


# In[5]:


# Boardman: create the features for model
y = boardman_downtime[['Minutes']]
X = boardman_downtime[['Asset', 'Super Reason', 'Reason Lvl1', 'Reason Lvl2', 'Shift', 'Hours']]
# dummy variables for categorical variables
X = pd.get_dummies(X)
# cross validation with train, test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.linear_model import Ridge
clf = Ridge(alpha=1.0, solver='lsqr')
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
boardman_predict = clf.predict(X_test)[0:30]
boardman_predict = pd.DataFrame(data=boardman_predict)


# In[6]:


boardman_predict.plot(figsize=(16, 10))


# In[7]:


# connell: create the features for model
y = connell_downtime[['Minutes']]
X = connell_downtime[['Asset', 'Super Reason', 'Reason Lvl1', 'Reason Lvl2', 'Shift', 'Hours']]
# dummy variables for categorical variables
X = pd.get_dummies(X)
# cross validation with train, test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.linear_model import Ridge
clf = Ridge(alpha=1.0, solver='lsqr')
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
connell_predict = clf.predict(X_test)[0:30]
connell_predict = pd.DataFrame(data=connell_predict)


# In[8]:


connell_predict.plot(figsize=(16, 10))


# In[9]:


# delhi: create the features for model
y = delhi_downtime[['Minutes']]
X = delhi_downtime[['Asset', 'Super Reason', 'Reason Lvl1', 'Reason Lvl2', 'Shift', 'Hours']]
# dummy variables for categorical variables
X = pd.get_dummies(X)
# cross validation with train, test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.linear_model import Ridge
clf = Ridge(alpha=1.0, solver='lsqr')
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
delhi_predict = clf.predict(X_test)[0:30]
delhi_predict = pd.DataFrame(data=delhi_predict)


# In[10]:


delhi_predict.plot(figsize=(16, 10))


# In[11]:


# park_rapids: create the features for model
y = park_rapids_downtime[['Minutes']]
X = park_rapids_downtime[['Asset', 'Super Reason', 'Reason Lvl1', 'Reason Lvl2', 'Shift', 'Hours']]
# dummy variables for categorical variables
X = pd.get_dummies(X)
# cross validation with train, test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.linear_model import Ridge
clf = Ridge(alpha=1.0, solver='lsqr')
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
park_rapids_predict = clf.predict(X_test)[0:30]
park_rapids_predict = pd.DataFrame(data=park_rapids_predict)


# In[12]:


park_rapids_predict.plot(figsize=(16, 10))


# In[13]:


# Pasco: create the features for model
y = pasco_downtime[['Minutes']]
X = pasco_downtime[['Asset', 'Super Reason', 'Reason Lvl1', 'Reason Lvl2', 'Shift', 'Hours']]
# dummy variables for categorical variables
X = pd.get_dummies(X)
# cross validation with train, test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.linear_model import Ridge
clf = Ridge(alpha=1.0, solver='lsqr')
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
pasco_predict = clf.predict(X_test)[0:30]
pasco_predict = pd.DataFrame(data=pasco_predict)


# In[14]:


pasco_predict.plot(figsize=(16, 10))


# In[15]:


# richland: create the features for model
y = richland_downtime[['Minutes']]
X = richland_downtime[['Asset', 'Super Reason', 'Reason Lvl1', 'Reason Lvl2', 'Shift', 'Hours']]
# dummy variables for categorical variables
X = pd.get_dummies(X)
# cross validation with train, test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
from sklearn.linear_model import Ridge
clf = Ridge(alpha=1.0, solver='lsqr')
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
richland_predict = clf.predict(X_test)[0:30]
richland_predict = pd.DataFrame(data=richland_predict)


# In[16]:


richland_predict.plot(figsize=(16, 10))

