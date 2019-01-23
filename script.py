import os
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-dir", dest="d",help="Specify the directory for counting sub folders containing images")
options = parser.parse_args()
directory = options.d
try:

    lines = [x for x in os.listdir(directory) if os.path.isdir(directory)]
    dictionary_empty = {}
    for i in lines:
        u = directory + i

        dictionary_empty[i] = len([x for x in os.listdir(u)
                                   if x.endswith((".jpg", ".JPG", ".jpeg", ".JPEG", ".png", ".PNG", ".gif", ".GIF"))])

    data_frame = pd.DataFrame.from_dict(dictionary_empty, orient="index")
    data_frame.to_csv("counts.csv", sep="\t", encoding="utf-8")


except OSError:
    print("The passed path is not a directory")


