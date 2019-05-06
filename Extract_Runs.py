# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 23:24:36 2019

@author: Shriram
"""

import os
import json
import pandas as pd
import time
from pandas.io.json import json_normalize
df = pd.DataFrame()

rootdir ='C:/Users/shrir/Google Drive (karthikeyan.s@husky.neu.edu)/INFO_6210/Hyperparameter Project/hyperparameter-db-project-ds11-master/Extracted Files'

for subdir, dirs, files in os.walk(rootdir):
    #print('dirs'+str(dirs))
    print('subdirs'+str(subdir))
    for file in files:
        print(str("file:"+file))
        if (file.endswith('json') and file.startswith('meta')):
            fullfilepath = subdir+"/"+file
            with open(str(subdir)+"/"+file) as f:
                d = json.load(f)
                #print(d)
                df = df.append(json_normalize(d))
                df['file_creation_time']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getctime(subdir+"/"+file)))
                #df['execution_time_ts']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(df['execution_time']))
                #df['start_time_ts']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(df['start_time'].astype(float)))
                #df['end_time_ts']=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(df['end_time']))
            #count = len(readlines())
            #print("num_lines:"+num_lines)
            f.close()

rundf = df['run_id']

df.to_csv("C:/Users/shrir/Google Drive (karthikeyan.s@husky.neu.edu)/INFO_6210/Hyperparameter Project/metadata_scraped.csv",index=False)
#rundf.to_csv("C:/Users/shrir/Google Drive (karthikeyan.s@husky.neu.edu)/INFO_6210/Hyperparameter Project/rundf.csv",index=False)

#df.columns
