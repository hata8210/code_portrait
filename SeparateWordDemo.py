
# coding: utf-8

# In[1]:


# 导入依赖包
import os
import csv
import numpy as np
import pandas as pd
import json
from nltk import word_tokenize
# 导入自定义依赖包
import LoadFileDemo as lf



# In[12]:


# 1.定义分词符号集合和目标分词符号
sepatate_symbol = ['\r\n','\r','\n','\t',' ','_','.',',','+'
                   ,'-','=',';',':','/','*','#','@','?','!'
                   ,'%','^',"'",'"','(',')','[',']','{','}','&','~','|','-']
target_symbol = ' '

# 2.分词符号分词方法
def sepatate_by_symbol(text = '',sepatate_symbol = [' ']):
    # 1.循环匹配分词符号集合sepatate_symbol,替换成目标分词符号target_symbol
    for symbol in sepatate_symbol:
        text = text.replace(symbol, target_symbol)
    #print('分词符号替换后效果:  %s ' % text)
    return text

# 3.分词符号分词方法
def sepatate_by_case(text = ''):
    # 1.遍历text字符（可使用集合序列化操作或map方法）
    text_list = list(text)
    for i in range(len(text_list)):
        if i==0 : continue
        # 判断是数字则用分词符号替换
        if text_list[i].isdigit():
            text_list[i] = target_symbol
        # 判断符合驼峰命名的插入分词符号分词
        if text_list[i-1].isalpha() and text_list[i].isalpha():
            if text_list[i-1] == text_list[i-1].lower() and text_list[i] == text_list[i].upper():
                text_list.insert(i,target_symbol)
    rs =  "".join(text_list)   
    #print('驼峰命名替换后效果:  %s ' % rs)
    return rs

# 4.输入文本进行分词
def separate_text_single(text = ''):
    # 加入目标分词符号
    print("分词符号集合: %s " % sepatate_symbol)
    print("目标分词符号: %s " % target_symbol)
    text_pro = sepatate_by_case(sepatate_by_symbol(text, sepatate_symbol))
    # 使用word_tokenize分词
    rs = word_tokenize(text_pro)
    return rs

def separate_texts(text_list = ['']):
    # 遍历每篇文章
    return [separate_text_single(text) for text in text_list]


