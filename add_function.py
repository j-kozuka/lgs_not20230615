# >cd C:\Users\u345416g\Dropbox\tasks_dropbox\20230519\tree\database3
# >python add_function.py [function id] 
import sys

from block_root_lib import Block_Root, loadRootBlock

import datetime
import hashlib
import pickle

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

function_id = sys.argv[1]

### make root
print('load root')
root = loadRootBlock()
root.info()

root.add_function(function_id)
root.save()

### show graphes
root.show_managemet_graph()
root.show_operation_graph()
