
# coding: utf-8

# In[9]:


import os
import csv
import numpy as np
import pandas as pd
import json


# In[33]:


def log(title=''):print('------------------'                         +title+'-------------------')


# In[ ]:


project_file_type = ['*']

def set_project_file_type(file_type):
    project_file_type = file_type


# In[11]:


# 清洗数据
def clean_book(document):
    lines = document.split("\n")
    start= 0
    end = len(lines)
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith("*** START OF THIS PROJECT GUTENBERG"):
            start = i + 1
        elif line.startswith("*** END OF THIS PROJECT GUTENBERG"):
            end = i - 1
    return "\n".join(lines[start:end])

# 检查输入文件名是否符合需要的文件类型，不输入file_type默认都符合
def check_file_type(file_name = '', file_type = ['*']):
    if file_name == '':
        print('请输入合法的文件名！')
        return False
    if '*' in file_type : return True
    rs = False
    for f_type in file_type:
        if file_name.endswith('.'+f_type):
            rs = True
            break
    return rs


# In[24]:


# 加载数据（限制两层目录）
def load_project_data_limit(folder = ''):
    # 文件目录合法性校验
    if not(os.path.isdir(folder)):
        print('请输入合法的文件目录！')
        return [],[]
    # 定义载入数组
    documents = []
    paths = []
    # 遍历目录及其子目录，生成目录数组
    # 目前只有两层。。。这里需要重构成一个递归方法，递归生成所有目录。。。。
    subfolders = [subfolder for subfolder in os.listdir(folder)
                  if os.path.isdir(os.path.join(folder, subfolder))]
    # 根据目录数组找出所有目录下的所有文件
    for subfolder in subfolders:
        full_subfolder_path = os.path.join(folder, subfolder)
        print('目前加载目录：%s' % full_subfolder_path)
        for document_name in os.listdir(full_subfolder_path):
            print(document_name)
            if not(check_file_type(document_name,['txt'])):continue
            try:
                with open(os.path.join(full_subfolder_path, document_name), 'r',encoding='utf-8') as inf:
                    documents.append(clean_book(inf.read()))
                    paths.append(full_subfolder_path)
            except(UnicodeDecodeError):
                print('error file : %s '%os.path.join(full_subfolder_path, document_name))
    return documents, paths


# In[25]:


# 加载数据（兼容所有嵌套目录）
def load_project_data(folder = '',file_type = ['*']):
    # 文件目录合法性校验
    if not(os.path.isdir(folder)):
        print('请输入合法的文件目录！')
        return [],[]
    # 定义载入数组
    documents = []
    filenames = []
    paths = []
    print('输入目录地址：%s' % folder)
    for full_folder_path, dirs, files in os.walk(folder):
        print('－－－－－－－－－－－')
        print('当前目录地址：%s' % full_folder_path) #当前目录路径，得到指定目录下的所有嵌套目录结构（只有目录没有文件）
        print('含有文件：%s' % files) #当前路径下所有非目录子文件
        for document_name in files:
            if check_file_type(document_name, file_type):
                try:
                    with open(os.path.join(full_folder_path, document_name), 'r',encoding='utf-8') as inf:
                        documents.append(clean_book(inf.read()))
                        filenames.append(document_name)
                        paths.append(full_folder_path)
                except(UnicodeDecodeError):
                    print('读取文件错误 : %s '%os.path.join(full_folder_path, document_name))
    return documents, filenames, paths


# In[26]:


# os包中的walk使用
def file_name(file_dir):
    print('输入目录地址：%s' % file_dir)
    for root, dirs, files in os.walk(file_dir):
        print('－－－－－－－－－－－')
        print('当前目录地址：%s' % root) #当前目录路径，得到指定目录下的所有嵌套目录结构（只有目录没有文件）
        print('含有文件夹：%s' % dirs) #当前路径下所有子目录
        print('含有文件：%s' % files) #当前路径下所有非目录子文件  


# In[32]:


# os包中的listdir使用
def listdir(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path): # 判断是文件夹还是文件
            listdir(file_path) # 递归搜索子目录
        else:
            print('含有文件：%s' % file_path) # 找到文件



