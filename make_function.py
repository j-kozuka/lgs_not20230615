
# >cd C:\Users\u345416g\Dropbox\tasks_dropbox\20230519\tree\database3
# >python make_function.py 
#from block_human_lib import loadBlock, randomname
from block_root_lib import make_function_block

#import datetime
#import hashlib
#import pickle

# 生成したいPythonコードを文字列として定義する
py_code = """
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots()

circle = Circle((0, 0), radius=1, color='red')

ax.add_patch(circle)

ax.set_aspect('equal')

plt.show()
"""

py_code_argv = """
# > python ./function_block/function.py argv1 argv2 argv3
import sys

# get number of argv
num_args = len(sys.argv)

# no argv
if num_args == 1:
    print("no argv")

# exist argv
else:
    print("number of argv is {}.".format(num_args - 1))
    for i in range(1, num_args):
        print("argv{} is {}.".format(i, sys.argv[i]))
"""

inst = """
# function name

hello world!!

## environment 

> pip list

## execute

> python function.py

## output

> hello world!!
"""

#make_function_block(py_code_argv, inst)
make_function_block(py_code, inst)