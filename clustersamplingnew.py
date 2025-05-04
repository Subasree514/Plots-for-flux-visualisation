#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import cobra.test
import os
from os.path import join
import cobra
#import json
import scipy
import optlang
import numpy as np
import pandas as pd
from scipy.io import loadmat
from cobra.io import load_matlab_model
import openpyxl
import pathlib
from os.path import join
from pickle import load
from typing import TYPE_CHECKING
import pathlib
#import pytest
from cobra.io import load_matlab_model
from cobra.io import save_matlab_model
#from cobra.io import model_to_pymatbridge


# In[ ]:


cobra_config = cobra.Configuration()
#cobra_config.solver ="gurobi"


# In[ ]:


model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelHCC1143rslooplessfinal.mat"))#*****
model_py_1b.solver = 'gurobi'
from cobra.sampling import OptGPSampler, ACHRSampler


# In[ ]:


achr = ACHRSampler(model_py_1b,thinning=1)
s1a = achr.sample(100000)
s1a.to_csv('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/hcc1143lrsooplessachr.csv')#*****
s1a_valid = s1a[achr.validate(s1a) == "v"]
len(s1a_valid)
colonRS_median=s1a.median(axis = 0) #dtype=np.float64
colonRS_median=colonRS_median[0:len(colonRS_median)]
colonRS_median_df=pd.DataFrame(colonRS_median)
colonRS_median_df.to_excel('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/hcc1143rslooplessmedian.xlsx')#*****
##
#optgp = OptGPSampler(model_py_1b,thinning=1)
#s1a = optgp.sample(50000)
#s1a.to_csv('HMELoptgp.csv')
#s1a_valid = s1a[optgp.validate(s1a) == "v"]
#len(s1a_valid)


# In[ ]:


model_py_1c=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelOVKATElooplessfinal.mat"))#*****
#model_py_1c.solver = 'gurobi'
from cobra.sampling import OptGPSampler, ACHRSampler


# In[ ]:


achr = ACHRSampler(model_py_1c,thinning=1)
s2 = achr.sample(100000)
s2.to_csv('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/ovkatelooplessachr.csv')#*****
s2_valid = s2[achr.validate(s2) == "v"]
len(s2_valid)
colon_median=s2.median(axis = 0) #dtype=np.float64
colon_median=colon_median[0:len(colon_median)]
colon_median_df=pd.DataFrame(colon_median)
colon_median_df.to_excel('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/ovkatelooplessmedian.xlsx')#*****
##
#optgp = OptGPSampler(model_py_1b,thinning=1)
#s1a = optgp.sample(50000)
#s1a.to_csv('HMELoptgp.csv')
#s1a_valid = s1a[optgp.validate(s1a) == "v"]
#len(s1a_valid)


# In[ ]:


model_py_1d=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelOVKATErslooplessfinal.mat"))#*****
#model_py_1d.solver = 'gurobi'
from cobra.sampling import OptGPSampler, ACHRSampler


# In[ ]:


achr = ACHRSampler(model_py_1d,thinning=1)
s2a = achr.sample(100000)
s2a.to_csv('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/ovkatersooplessachr.csv')#*****
s2a_valid = s2a[achr.validate(s2a) == "v"]
len(s2a_valid)
colonRS_median=s2a.median(axis = 0) #dtype=np.float64
colonRS_median=colonRS_median[0:len(colonRS_median)]
colonRS_median_df=pd.DataFrame(colonRS_median)
colonRS_median_df.to_excel('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/ovkaterslooplessmedian.xlsx')#*****
##
#optgp = OptGPSampler(model_py_1b,thinning=1)
#s1a = optgp.sample(50000)
#s1a.to_csv('HMELoptgp.csv')
#s1a_valid = s1a[optgp.validate(s1a) == "v"]
#len(s1a_valid)


# In[ ]:


model_py_1e=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelSW620looplessfinal.mat"))#*****
#model_py_1e.solver = 'gurobi'
from cobra.sampling import OptGPSampler, ACHRSampler


# In[ ]:


achr = ACHRSampler(model_py_1e,thinning=1)
s3 = achr.sample(100000)
s3.to_csv('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/sw620looplessachr.csv')#*****
s3_valid = s3[achr.validate(s3) == "v"]
len(s3_valid)
colon_median=s3.median(axis = 0) #dtype=np.float64
colon_median=colon_median[0:len(colon_median)]
colon_median_df=pd.DataFrame(colon_median)
colon_median_df.to_excel('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/sw620looplessmedian.xlsx')#*****
##
#optgp = OptGPSampler(model_py_1b,thinning=1)
#s1a = optgp.sample(50000)
#s1a.to_csv('HMELoptgp.csv')
#s1a_valid = s1a[optgp.validate(s1a) == "v"]
#len(s1a_valid)


# In[ ]:


model_py_1f=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelSW620rslooplessfinal.mat"))#*****
#model_py_1f.solver = 'gurobi'
from cobra.sampling import OptGPSampler, ACHRSampler


# In[ ]:


achr = ACHRSampler(model_py_1f,thinning=1)
s3a = achr.sample(100000)
s3a.to_csv('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/sw620lrsooplessachr.csv')#*****
s3a_valid = s3a[achr.validate(s3a) == "v"]
len(s3a_valid)
colonRS_median=s3a.median(axis = 0) #dtype=np.float64
colonRS_median=colonRS_median[0:len(colonRS_median)]
colonRS_median_df=pd.DataFrame(colonRS_median)
colonRS_median_df.to_excel('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/sw620rslooplessmedian.xlsx')#*****
##
#optgp = OptGPSampler(model_py_1b,thinning=1)
#s1a = optgp.sample(50000)
#s1a.to_csv('HMELoptgp.csv')
#s1a_valid = s1a[optgp.validate(s1a) == "v"]
#len(s1a_valid)

