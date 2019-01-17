#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 23:26:38 2019

@author: mbaye
"""
import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_csv("/media/mbaye/DATA/mescours/datascience/dev/datasciencecourses/data/train.csv")
df.head(10)
df.describe()