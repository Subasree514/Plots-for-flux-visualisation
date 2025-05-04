# libraries
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


cobra_config = cobra.Configuration()
## colon cancer and non-cancerous
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelSW620_rs_revised.mat"))
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelSW620.mat"))
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelHS255T_rsmin_full_revised.mat"))
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelHS255Tnew.mat.mat"))

## ovarian cancer and non-cancerous
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelOVKATE_rs_revised.mat"))
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelOVKATE.mat"))
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelOELE_rsmin_full_revised.mat"))
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelOELE.mat"))

## breast cancer and non-cancerous
model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelHCC1143_rs_revised.mat"))
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelHCC1143.mat"))
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelHMEL_rsmin_full_revised.mat"))
#model_py_1b=cobra.io.load_matlab_model(join(r'/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models',"modelHMEL.mat"))

model_py_1b.solver = 'gurobi'

## flux sampling analysis - we choose ACHR
from cobra.sampling import OptGPSampler, ACHRSampler

achr = ACHRSampler(model_py_1b,thinning=1)
s1a = achr.sample(100000)

## validate the samples
s1a_valid = s1a[achr.validate(s1a) == "v"]
len(s1a_valid)
## save the data
s1a.to_csv('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/hcc1143lrsooplessachr.csv')

## find median and save the data
cancerRS_median=s1a.median(axis = 0) #dtype=np.float64
cancerRS_median=cancerRS_median[0:len(cancerRS_median)]
cancerRS_median_df=pd.DataFrame(cancerRS_median)
cancerRS_median_df.to_excel('/home/ibsc/Downloads/Subasree MEJ models/MEJ loop models/hcc1143rslooplessmedian.xlsx')
