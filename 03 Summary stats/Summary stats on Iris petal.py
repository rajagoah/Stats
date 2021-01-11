#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 20:56:01 2021

@author: aakarsh.rajagopalan
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "/Users/aakarsh.rajagopalan/Personal documents/Python projects/Statistics/Stats_dataset/Iris dataset/IRIS.csv"
#importing the data
iris = pd.read_csv(path)

#the columns in the dataset are
print(iris.columns)

iris['sepal_length'].hist(); plt.show();
iris['sepal_width'].hist(); plt.show();
iris['petal_length'].hist(); plt.show();
iris['petal_width'].hist(); plt.show();
iris['species'].hist(); plt.show();


