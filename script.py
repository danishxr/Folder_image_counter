
import os, os.path

import pandas as pd

import argparse 

parser=argparse.ArgumentParser()

parser.add_argument("-dir",dest="d",help="Specify the directory for counting subfolders containing images")

options=parser.parse_args()

Directory = options.d

lines=os.listdir(Directory)

dictionary_empty={}

for i in lines:

	u=Directory+i

	dictionary_empty[i]=len(os.listdir(u))

data_frame=pd.DataFrame.from_dict(dictionary_empty,orient="index")

data_frame.to_csv("counts.csv", sep="\t", encoding="utf-8")
