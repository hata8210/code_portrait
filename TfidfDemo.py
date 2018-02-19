
# coding: utf-8

# In[1]:


# 导入依赖包
import os
import csv
import numpy as np
import pandas as pd
import json
from nltk import word_tokenize
from nltk.corpus import words
import nltk
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
import copy
# 导入自定义依赖包
import LoadFileDemo as lf
import SeparateWordDemo as sw
import WordCleanDemo as wc


# In[42]:


# 输入多篇文章样本（不分词）进行短语权重分析
def tfidf_tlist(text_list = ['']):
    #该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频 
    vectorizer=CountVectorizer()
    #该类会统计每个词语的tf-idf权值  
    transformer=TfidfTransformer()
    #第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
    tfidf=transformer.fit_transform(vectorizer.fit_transform(text_list))
    #获取词袋模型中的所有词语  
    word=vectorizer.get_feature_names()
    #将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重  
    weight=tfidf.toarray()
    return word,weight

# 输入多篇文章样本（分词后）进行短语权重分析
def tfidf_wlist(text_list = [['']]):
    text_list_org = [" ".join(text) for text in text_list]
    return tfidf_tlist(text_list_org)

# 数组元素调换位置
def change_pos(arr,first_idx,second_idx):
    if first_idx>=0 and second_idx>0 and first_idx<=len(arr) and second_idx<=len(arr):
        temp_value = arr[second_idx]
        arr[second_idx] = arr[first_idx]
        arr[first_idx] = temp_value

# 找一个样本的所有单词权重最top的k个数组下标
def find_topk_tfidf_single(weight_row = [],topk = 10):
    if len(weight_row) < topk : topk=len(weight_row)
    weight_row_temp = copy.deepcopy(weight_row)
    org_idx = [i for i in range(len(weight_row_temp))]
    for i in range(topk):
        max_idx = i
        for j in range(len(weight_row_temp)-i):
            #找出最第i位top的置换到weight_row_temp的i位置
            if weight_row_temp[max_idx] < weight_row_temp[j+i] : max_idx = j+i
        change_pos(weight_row_temp,i,max_idx)
        change_pos(org_idx,i,max_idx)
    return org_idx[:topk]

def find_topk_tfidf(weight = [],topk = 10):
    return [find_topk_tfidf_single(weight[j],topk) for j in range(len(weight))]




