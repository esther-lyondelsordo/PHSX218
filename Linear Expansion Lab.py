#!/usr/bin/env python
# coding: utf-8

# In[36]:


import numpy as np


# In[41]:


## COPPER uncertainty in delta T, rule 3
deltact = np.array([.02,.02])

def rule3(deltact):
    errcopperT = np.sqrt(np.sum(deltact**2))
    return errcopperT
errcopperT = rule3(deltact)
print('error in delta T for copper = +/-',errcopperT,'degrees C')


# In[42]:


## COPPER uncertainty in alpha, rule 4
deltaca = np.array([.000005,.0005,errcopperT])
consca = np.array([1,-1,-1])
valca = np.array([.000805,.6835,66.77])
cAlpha = .0000176

def rule4(cAlpha,consca,deltaca,valca):
    errcopperAlpha = np.abs(cAlpha)*np.sqrt(np.sum((consca*deltaca/valca)**2))
    return errcopperAlpha
errcopperAlpha = rule4(cAlpha,consca,deltaca,valca)
print('error in alpha for copper = +/-',errcopperAlpha,'/degree C')


# In[43]:


## ALUMINUM uncertainty in delta T, rule 3
deltaat = np.array([.02,.02])

def rule3(deltaat):
    erralumT = np.sqrt(np.sum(deltaat**2))
    return erralumT
erralumT = rule3(deltaat)
print('error in delta T for aluminum = +/-',erralumT,'degrees C')


# In[44]:


## ALUMINUM uncertainty in alpha, rule 4
deltaa = np.array([.000005,.0005,erralumT])
consa = np.array([1,-1,-1])
vala = np.array([.00113,.6845,56.61])
aAlpha = .0000292

def rule4(aAlpha,consa,deltaa,vala):
    erralumAlpha = np.abs(aAlpha)*np.sqrt(np.sum((consa*deltaa/vala)**2))
    return erralumAlpha
erralumAlpha = rule4(aAlpha,consa,deltaa,vala)
print('error in alpha for aluminum = +/-',erralumAlpha,'/degree C')


# In[ ]:




