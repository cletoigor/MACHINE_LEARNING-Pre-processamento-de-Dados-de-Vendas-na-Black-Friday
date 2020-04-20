#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# #### Respostas do desafio realizado por Igor Cleto:

# In[3]:


#Primeiro contato visual com o dataset:
black_friday.head()


# In[4]:


black_friday.tail()


# In[5]:


#Verificando as observações,as colunas e o tipo de dados salvos para a resposta da primeira questão:
shape = black_friday.shape


# In[6]:


print(type(shape))
print(shape)


# In[7]:


black_friday.info()


# In[8]:


black_friday_Q02 = black_friday.loc[ (black_friday['Age']=='26-35') & (black_friday['Gender']=='F')]


# In[9]:


filtro = ['Age','Gender']


# In[10]:


black_friday_Q02[filtro]


# In[11]:


Q02 = black_friday_Q02['Gender'].count()


# In[12]:


type(Q02)


# In[13]:


usuarios_unicos = black_friday['User_ID'].nunique()


# In[14]:


black_friday.nunique()


# In[15]:


print(usuarios_unicos)
print(type(usuarios_unicos))


# In[16]:


dtypes_sum = black_friday.dtypes.nunique()
print(dtypes_sum)


# In[17]:


type(dtypes_sum)


# In[46]:


count_nan = black_friday.isna().sum()
print(count_nan)


# In[50]:


count_nan = (black_friday['Product_Category_3'].isna() | black_friday['Product_Category_2'].isna())


# In[53]:


count_nan = count_nan.sum()


# In[47]:


q10 = black_friday['Product_Category_3'].isna().equals(black_friday['Product_Category_2'].isna())
print(q10)


# In[21]:


all_rows = black_friday.shape[0]


# In[54]:


count_nan_percent = (count_nan / all_rows)
print(count_nan_percent)


# In[23]:


count_nan_Product_Category_3 = black_friday['Product_Category_3'].isnull().values.sum()
print(count_nan_Product_Category_3)


# In[59]:


black_friday['Product_Category_3'].count().sum()


# In[24]:


df_Product_Category_3 = black_friday['Product_Category_3'].dropna()


# In[60]:


mode_Product_Category_3 = df_Product_Category_3.mode()


# In[63]:


mode_Product_Category_3 = int(mode_Product_Category_3)


# In[27]:


normalized = (black_friday['Purchase'] - black_friday['Purchase'].min()) / (black_friday['Purchase'].max() - black_friday['Purchase'].min())


# In[28]:


normalized_mean = normalized.mean()


# In[29]:


padronizacao = (black_friday['Purchase'] - black_friday['Purchase'].mean()) / black_friday['Purchase'].std()


# In[30]:


i = 0
for value in padronizacao:
    if -1 < value < 1:
        i += 1
print(i)


# In[31]:


filtro = ['Product_Category_2','Product_Category_3']


# In[32]:


dataframe = black_friday[filtro]


# In[33]:


q10 = black_friday['Product_Category_2'].isna().equals(black_friday['Product_Category_3'].isna())


# In[34]:


print(q10)


# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[35]:


def q1():
    return shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[36]:


def q2():
    return Q02


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[37]:


def q3():
    return usuarios_unicos


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[38]:


def q4():
    return dtypes_sum


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[39]:


def q5():
    return count_nan_percent


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[40]:


def q6():
    return count_nan_Product_Category_3


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[41]:


def q7():
    return mode_Product_Category_3


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[42]:


def q8():
    return normalized_mean


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[43]:


def q9():
    return i


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[44]:


def q10():
    return q10

