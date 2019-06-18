#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../../../Jupyterlab/Workspace/what_is_your_tag_schema'))
	print(os.getcwd())
except:
	pass

#%%
train_file = 'conll_2000/train.txt'


#%%
import os
import re

def load_data(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        raw_data = f.read()
    data = []
    for raw in raw_data.split("\n\n"):
        sent = []
        raw = raw.strip()
        if raw == '':
            continue
        for line in raw.split("\n"):
            sent.append(line)
        data.append(sent)
    return data


#%%
train_data = load_data(train_file)


#%%
len(train_data)


#%%
dev_ratio = 0.15
dev_idx = int(len(train_data)*dev_ratio)
dev_idx = 1000


#%%
import random

random.shuffle(train_data)


#%%
train_data,dev_data = train_data[:-dev_idx],train_data[-dev_idx:]


#%%
len(train_data),len(dev_data)


#%%
def save_conll_format(file_path,data):
    with open(file_path,'w',encoding='utf-8') as f:
        for sent in data:
            f.writelines('\n'.join(sent))
            f.write('\n\n')


#%%
save_conll_format('conll_2000/train.txt',train_data)
save_conll_format('conll_2000/dev.txt',dev_data)


#%%
get_ipython().system('ls conll_2000/ -l')


