
# coding: utf-8

# In[1]:

""" Process IFPRI IMPACT excel files into csv and bigquery
-------------------------------------------------------------------------------



Author: Rutger Hofste
Date: 20190916
Kernel: python35
Docker: rutgerhofste/gisdocker:ubuntu16.04

"""

TESTING = 0

SCRIPT_NAME = "Y2019M09D16_RH_Process_IMPACT_V01"
OUTPUT_VERSION = 3

BQ_PROJECT_ID = "aqueduct30"

S3_INPUT_PATH = "s3://wri-projects/Aqueduct30/rawData/IFRPI/Y2019M09D16_RH_IFPRI_IMPACT_2015_Raw_V01/20161118_IMPACT_data"

ec2_input_path = "/volumes/data/{}/input_V{:02.0f}".format(SCRIPT_NAME,OUTPUT_VERSION)
ec2_output_path = "/volumes/data/{}/output_V{:02.0f}".format(SCRIPT_NAME,OUTPUT_VERSION)

s3_output_path = "s3://wri-projects/Aqueduct30/processData/{}/output_V{:02.0f}".format(SCRIPT_NAME,OUTPUT_VERSION)


# In[2]:

import time, datetime, sys
dateString = time.strftime("Y%YM%mD%d")
timeString = time.strftime("UTC %H:%M")
start = datetime.datetime.now()
print(dateString,timeString)
sys.version


# In[3]:

import os
import subprocess
import pandas as pd
from tqdm import tqdm
from google.cloud import bigquery


# In[4]:

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/.google.json"
os.environ["GOOGLE_CLOUD_PROJECT"] = "aqueduct30"
client = bigquery.Client(project=BQ_PROJECT_ID)


# In[5]:

get_ipython().system('rm -r {ec2_input_path}')
get_ipython().system('rm -r {ec2_output_path}')
get_ipython().system('mkdir -p {ec2_input_path}')
get_ipython().system('mkdir -p {ec2_output_path}')


# In[6]:

get_ipython().system('aws s3 cp {S3_INPUT_PATH} {ec2_input_path} --recursive')


# In[7]:

scenarios = ["gfdl",
             "hgem",
             "ipsl",
             "miro",
             "NoCC"
            ]


# In[8]:

listje = []
for scenario in scenarios:
    print(scenario)
    input_filename = "{}_all.xlsx".format(scenario)
    input_path = "{}/{}".format(ec2_input_path,input_filename)
    df = pd.read_excel(input_path)
    listje.append(df)
df_concat = pd.concat(listje)
print(df_concat.shape)


# In[9]:

output_filename = "ifpri_impact_2015_v{:02.0f}".format(OUTPUT_VERSION)
output_path = "{}/{}".format(ec2_output_path,output_filename)
df_concat.to_csv(output_path)


# In[10]:

get_ipython().system('aws s3 cp {ec2_output_path} {s3_output_path} --recursive')


# In[11]:

if TESTING:
    df_concat = df_concat[0:10]


# In[12]:

gbq_dataset_name = "IFPRI_IMPACT_2015"        
table_name = output_filename
destination_table= "{}.output_v{:02.0f}".format(gbq_dataset_name,OUTPUT_VERSION)


# In[13]:

df_concat.to_gbq(project_id=BQ_PROJECT_ID,
                 destination_table=destination_table,
                 chunksize=100000,
                 if_exists="fail")


# In[14]:

end = datetime.datetime.now()
elapsed = end - start
print(elapsed)


# previous run:  
