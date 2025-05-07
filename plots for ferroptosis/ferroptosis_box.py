#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


#import joypy
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm
from sklearn.datasets import load_iris


# In[ ]:


data_cw2= pd.read_csv('/home/ibsc/subasree/hs255tlooplessachr.csv')
data_cw2rs= pd.read_csv('/home/ibsc/subasree/hs255trsmlooplessachr.csv')
data_ovkate= pd.read_csv('/home/ibsc/subasree/oelelooplessachr.csv')
data_ovkaters= pd.read_csv('/home/ibsc/subasree/oelerslooplessachr.csv')
data_hcc1143rs= pd.read_csv('/home/ibsc/subasree/hmelrslooplessachr.csv')
data_hcc1143= pd.read_csv('/home/ibsc/subasree/hmellooplessachr.csv')


# In[ ]:


data_cancer1=data_cw2
data_cancerrs1=data_cw2rs


# In[ ]:


a=data_cancer1['DM_atp_c_']
b=data_cancerrs1['DM_atp_c_']
##CYSTGLUex DHORD9 HMR_5135 r0193
##SLC7A11 CARS1 CTH DM_atp_c_


# In[ ]:


df1=pd.DataFrame(a)
df2=pd.DataFrame(b)
##


# In[ ]:


df1.columns=['r0193']
df2.columns=['r0193']
dataframe_1=pd.concat([df1,df2], ignore_index=True, sort=False)


# In[ ]:


schema1 = ['CRC'] * 100000
schema2 = ['RS-CRC'] * 100000
##


# In[ ]:


schema1_series=pd.Series(schema1)
schema2_series=pd.Series(schema2)
schema_DF_1=pd.DataFrame(schema1_series)
schema_DF_2=pd.DataFrame(schema2_series)


# In[ ]:


schema_DF=pd.concat([schema_DF_1, schema_DF_2], ignore_index=True, sort=False)


# In[ ]:


s=[dataframe_1,schema_DF]


# In[ ]:


rows3=pd.concat(s,axis=1)
## FCLTm FERO HMR_2368


# In[ ]:


rows3.columns=['CTH','Cancers']


# In[ ]:


rows3


# In[ ]:


data_cancer2=data_hcc1143
data_cancerrs2=data_hcc1143rs


# In[ ]:


c=data_cancer2['DM_atp_c_']
d=data_cancerrs2['DM_atp_c_']


# In[ ]:


df3=pd.DataFrame(c)
df4=pd.DataFrame(d)


# In[ ]:


df3.columns=['r0193']
df4.columns=['r0193']
dataframe_2=pd.concat([df3,df4], ignore_index=True, sort=False)


# In[ ]:


schema3 = ['TNBC'] * 100000
schema4 = ['RS-TNBC'] * 100000


# In[ ]:


schema3_series=pd.Series(schema3)
schema4_series=pd.Series(schema4)
schema_DF_3=pd.DataFrame(schema3_series)
schema_DF_4=pd.DataFrame(schema4_series)


# In[ ]:


schema_DF_1=pd.concat([schema_DF_3, schema_DF_4], ignore_index=True, sort=False)


# In[ ]:


s1=[dataframe_2,schema_DF_1]


# In[ ]:


rows4=pd.concat(s1,axis=1)
rows4.columns=['CTH','Cancers']


# In[ ]:


rows4


# In[ ]:


data_cancer3=data_ovkate
data_cancerrs3=data_ovkaters


# In[ ]:


e=data_cancer3['DM_atp_c_']
f=data_cancerrs3['DM_atp_c_']


# In[ ]:


df5=pd.DataFrame(e)
df6=pd.DataFrame(f)


# In[ ]:


df5.columns=['r0193']
df6.columns=['r0193']
dataframe_3=pd.concat([df5,df6], ignore_index=True, sort=False)


# In[ ]:


schema5 = ['HGSOC'] * 100000
schema6 = ['RS-HGSOC'] * 100000


# In[ ]:


schema5_series=pd.Series(schema5)
schema6_series=pd.Series(schema6)
schema_DF_5=pd.DataFrame(schema5_series)
schema_DF_6=pd.DataFrame(schema6_series)


# In[ ]:


schema_DF_2=pd.concat([schema_DF_5, schema_DF_6], ignore_index=True, sort=False)


# In[ ]:


s2=[dataframe_3,schema_DF_2]


# In[ ]:


rows5=pd.concat(s2,axis=1)
rows5.columns=['CTH','Cancers']


# In[ ]:


rows5


# In[ ]:


#define plotting region (2 rows, 2 columns)
fig, axes = plt.subplots(3,1,figsize=(3,5))
fig.subplots_adjust(left=0.3,hspace=0.5, wspace=0.5)

#create boxplot in each subplot
#plt.subplot(3,2,1)
boxplot1=sns.boxplot(data=rows3, x='Cancers', y='CTH',ax=axes[2])
boxplot1.set(
    xlabel='', 
    title='',
    ylabel=''
)
medians = rows3.groupby(['Cancers'])['CTH'].median()
medians_round=np.round(medians,2)
vertical_offset = rows3['CTH'].median() * 0.05
for xtick in boxplot1.get_xticks():
    boxplot1.text(xtick,medians_round[xtick] + vertical_offset,medians_round[xtick], 
            horizontalalignment='right',size='medium',color='k',weight='bold')
##
#plt.subplot(3,2,2)
boxplot2=sns.boxplot(data=rows4, x='Cancers', y='CTH',ax=axes[0])
boxplot2.set(
    xlabel='', 
    title='',
    ylabel=''
)
medians = rows4.groupby(['Cancers'])['CTH'].median()
medians_round=np.round(medians,2)
mediansnew=medians.reindex(index = ['TNBC', 'RS-TNBC'])
medians_round=np.round(mediansnew,2)
vertical_offset = rows4['CTH'].median() * 0.05
for xtick in boxplot2.get_xticks():
    boxplot2.text(xtick,medians_round[xtick] + vertical_offset,medians_round[xtick], 
            horizontalalignment='right',size='medium',color='k',weight='bold')
##
#plt.subplot(3,2,3)
boxplot3=sns.boxplot(data=rows5, x='Cancers', y='CTH',ax=axes[1])
boxplot3.set(
    xlabel='', 
    title='',
    ylabel=''
)
medians = rows5.groupby(['Cancers'])['CTH'].median()
medians_round=np.round(medians,2)
vertical_offset = rows5['CTH'].median() * 0.05
for xtick in boxplot3.get_xticks():
    boxplot3.text(xtick,medians_round[xtick] + vertical_offset,medians_round[xtick], 
            horizontalalignment='right',size='medium',color='k',weight='bold')
##
fig.supylabel('Flux (mmol/gDW/h)')
fig.suptitle('Non-growth associated ATP maintenance rate')


# In[ ]:


fig.savefig("/home/ibsc/subasree/NGAMRSFULL.pdf", format="pdf")
#'4NPHSULT','FCLTm','FERO','HMR_2368',

