
# coding: utf-8

# - https://www.clips.uantwerpen.be/conll2003/
# ```
#    U.N.         NNP  I-NP  I-ORG 
#    official     NN   I-NP  O 
#    Ekeus        NNP  I-NP  I-PER 
#    heads        VBZ  I-VP  O 
#    for          IN   I-PP  O 
#    Baghdad      NNP  I-NP  I-LOC 
#    .            .    O     O 
# ```
# 
# - https://www.clips.uantwerpen.be/conll2000/chunking/
# ```
#    He        PRP  B-NP
#    reckons   VBZ  B-VP
#    the       DT   B-NP
#    current   JJ   I-NP
#    account   NN   I-NP
#    deficit   NN   I-NP
#    will      MD   B-VP
#    narrow    VB   I-VP
#    to        TO   B-PP
#    only      RB   B-NP
#    #         #    I-NP
#    1.8       CD   I-NP
#    billion   CD   I-NP
#    in        IN   B-PP
#    September NNP  B-NP
#    .         .    O
# ```

# In[230]:


import os
import re

def load_data(file_path,label_column_id=-1,is_test=False):
    '''
    file_path:文件路径
    label_column_id:当前考虑的标签列,取值为-1,0,1,2...,默认-1
    '''
    with open(file_path, "r", encoding="utf8") as f:
        raw_data = f.read()
    if  is_test:
        return raw_data.split("\n\n")
    else:
        data = []
        labels = []
        for raw in raw_data.split("\n\n"):
            sent = []
            raw = raw.strip()
            if raw == '':
                continue
            for line in raw.split("\n"):
                word,*tags = re.split(r'\s+',line)
                if tags==[]:
                    print(line)
                    raise Exception('Data format is not right!')
                sent.append((word, tags[label_column_id]))
                labels.append(tags[label_column_id])
            if sent!=[]:
                data.append(sent)
        return data,labels


# In[231]:


from collections import Counter

def analysis(namespace):
    print('Namespace = {}'.format(namespace.folder))
    print('tag_columns = {}'.format(','.join(namespace.tag_columns)))
    print('Result')
    print('-'*50)
    for file in os.listdir(namespace.folder):
        if file.find('test')!=-1:
            file_path = os.path.join(namespace.folder,file)
            print('File = {}'.format(file_path))
            data = load_data(file_path,is_test=True)
            print('Sentences = {}'.format(len(data)))
        else:
            file_path = os.path.join(namespace.folder,file)
            print('File = {}'.format(file_path))
            for i in range(len(namespace.tag_columns)):
                print('Column = {}'.format(namespace.tag_columns[i]))
                data,labels = load_data(file_path,label_column_id=i)
                print('Sentences = {} '.format(len(data)))
                print('Tags = {}'.format(','.join(set(labels))))
                if namespace.tag_columns[i]=='NER' or namespace.tag_columns[i]=='NP':
                    tag_schema = Counter([t.split('-')[0] for t in labels if t!='-X-'])
                    tags = Counter([t.split('-')[-1] for t in labels if t!='-X-'])
                    print('Tag schema')
                    print(tag_schema.most_common())
                    print('Tags')
                    print(tags.most_common())
                print()
    print('-'*50)


# In[232]:


from argparse import Namespace

def main():
    coll2003 = Namespace(
        folder = 'conll_2003',
        tag_columns = ['POS','NP','NER']
    )
    coll2000 = Namespace(
        folder = 'conll_2000',
        tag_columns = ['POS','NP']
    )
    analysis(coll2000)
    analysis(coll2003)


# In[233]:


main()

