
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
# 导入自定义依赖包
import LoadFileDemo as lf
import SeparateWordDemo as sw


# In[2]:


# 提取词干
# 对于提取词干后判断单词是否有效，无效单词则用回提取词干前单词
porter = nltk.PorterStemmer()
lancaster=nltk.LancasterStemmer()
word_list = set(words.words())

def get_stem(word_before):
    word_after = porter.stem(word_before) # 还可以选择使用lancaster.stem(t)
    if word_after in word_list: # 判断是否有含义的英语单词
        return word_after
    else:
        return word_before


# In[3]:


# 定义停用词集合，java项目保留关键字集合
stop_use_word_java = ['private','protected','public',
                      'abstract','class','extends','final','implements','interface','native','new','static','strictfp','synchronized','transient','volatile',
                      'break','continue','return','do','while','if','else','for','instanceof','switch','case','deault',
                      'catch','finally','throw','throws','try',
                      'import','package',
                      'boolean','byte','char','double','float','int','long','short','null','true','false',
                      'super','this','void',
                      'const','goto',
                      'this'
                     ]


# In[4]:


# 特征处理
def clean_word(word = ''):
    # 去掉中文、去掉无效字符、去掉停用词
    if not(word.isalpha()) or (word in stop_use_word_java):
        return 'this_word_is_illegle'
    # 提取词干、单词全部小写
    rs = get_stem(word).lower()
    return rs

def clean_text(text = ['']):
    # 遍历文章每个分词
    print('本次处理文章的长度：%i ' % len(text))
    return [clean_word(word) for word in text if not(clean_word(word) == 'this_word_is_illegle')]

def word_clean(text_list):
    # 遍历每篇文章
    return [clean_text(text) for text in text_list]




