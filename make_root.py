# >cd C:\Users\u345416g\Dropbox\tasks_dropbox\20230519\tree\database3
# >python make_root.py 
from block_root_lib import Block_Root, make_function_block, py_code, makeFolder

import datetime
import hashlib
import pickle

### make root
print('make root')
root = Block_Root() 
root.info()
root.save()

### show graphes
root.show_managemet_graph()
root.show_operation_graph()

