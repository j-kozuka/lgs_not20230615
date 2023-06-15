# >cd C:\Users\u345416g\Dropbox\tasks_dropbox\20230519\tree\database3
# >python operation.py [function id] [parent id]

import sys
import subprocess
from block_root_lib import Block_Root, loadRootBlock

# get number of argv
num_args = len(sys.argv)

# no argv
if num_args == 1:
    print("no argv")
elif num_args == 2:
    parent_id = '00000'
else:
    print("number of argv is {}.".format(num_args - 1))
    for i in range(1, num_args):
        print("argv{} is {}.".format(i, sys.argv[i]))
    parent_id = sys.argv[2]

print("function id : ", sys.argv[1])
func_id = sys.argv[1]

### load root
print('load root')
root = loadRootBlock()
root.info()

### operate function #########
root.operation(func_id, parent_id)

root.save()
### show graphes
root.show_managemet_graph()
root.show_operation_graph()