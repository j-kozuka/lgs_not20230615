# https://www.letsopt.com/entry/2020/09/06/095449
# >cd C:\Users\u345416g\Dropbox\tasks_dropbox\20230519\tree\database
# >python block_root_lib.py 
import networkx as nx
import matplotlib.pyplot as plt
import hashlib
import pickle
import datetime
import textwrap
import os
import subprocess
import random
import json
import time

# 生成したいPythonコードを文字列として定義する
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
py_code = """
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

fig, ax = plt.subplots()

circle = Circle((0, 0), radius=1, color='red')

ax.add_patch(circle)

ax.set_aspect('equal')

plt.show()
"""

readme = """
# function name

hello world!!

## environment 

> pip list

## execute

> python function.py

## output

> hello world!!
"""

def makeFolder(ssPath):
    if not os.path.exists(ssPath):
        os.mkdir(ssPath)
        print('making block directory:', ssPath)
    else:
        print('the directory exists, already:', ssPath)

def make_hash_name(_bn):
    name = _bn
    birth_day = str(datetime.datetime.now())
    code = name + birth_day
    hash_name = hashlib.sha256(code.encode()).hexdigest()
    return hash_name
    
def make_function_block(code=py_code, inst=readme):
    fbn = 'function_block'
    hash_name = make_hash_name(fbn)
    makeFolder(hash_name)
    
    # ファイルに書き込むモードで開く
    codePath = hash_name + "/" + "function.py"
    with open(codePath, "w") as f:
        # 生成したコードをファイルに書き込む
        f.write(code)
        
    instPath = hash_name + "/" + "README.md"
    # ファイルに書き込むモードで開く
    with open(instPath, "w") as f:
        # 生成したコードをファイルに書き込む
        f.write(inst)

    code = 'python add_function.py'
    print('[add data code]:')
    print(code, hash_name)
    
    return hash_name

def make_data_block():
    fbn = 'data_block'
    hash_name = make_hash_name(fbn)
    makeFolder(hash_name)
    
    # 0から1の範囲で乱数を10個生成する
    random_numbers = [random.random() for _ in range(10)]

    instPath = hash_name + "/" + "dataset.txt"
    # ファイルに書き込むモードで開く
    with open(instPath, "w") as f:
         # 乱数を一行ずつ書き込む
        for number in random_numbers:
            f.write(str(number) + "\n")

    # ファイルを閉じる
    f.close()    
        
    return hash_name

def loadRootBlock():
    bln = './root.pickle'
    
    with open(bln, 'rb') as file:
        return pickle.load(file)

class Block_Root:   
    #def __init__(self, name='db_root', home='./'):
    def __init__(self):
        
        bln = './root.pickle' # block name

        ##### make root ######
        ## make graph
        self.mangra = nx.DiGraph() # management graph (mangra)
        self.opegra = nx.DiGraph() #operation graph (opegra)
             
        node_root = [(0, {"color" : "orchid",
                          "pos" : (0,0),
                          "code" : "root", 
                          "block_id" : "00000",
                          "bic" : "00000"
                         })]        
        self.mangra.add_nodes_from(node_root) 
        self.opegra.add_nodes_from(node_root) 
        
        #self.name = name
        self.name = 'root'
        self.birth_day = str(datetime.datetime.now())
        self.code = self.name + self.birth_day
        #self.name_hash = hashlib.sha256(self.code.encode()).hexdigest()
        
        self.draw_width = 15
        self.draw_height = 5

    def info(self):       
        print('I am', self.name, '.')
        print('I was born on', self.birth_day, '.')
            
    def save(self):
        print('save')
        
        bln = self.name + '.pickle'
        with open(bln, 'wb') as file:
            pickle.dump(self, file)
               
    def add_function(self, func_id):        
        print('add function')
        ## add new block function
        child = self.mangra.number_of_nodes()
        parent = child - 1
        print(parent, '-', child)

        node_function_new = [(child, {"color" : "cornflowerblue",
                                      "pos" : (child,0), 
                                      "code" : "func", 
                                      "block_id" : func_id,
                                      "bic" : func_id[0:5]
                                     })]
        
        edge_new = [(parent, child, {"color" : "black"})]
        self.mangra.add_nodes_from(node_function_new)
        self.mangra.add_edges_from(edge_new)

    def add_data(self, child_id, func_id, parents_id=str("00000")):        
        ## add new block data to management graph
        child = self.mangra.number_of_nodes()
        parent = child - 1

        #new_node = [(child, {"color" : "honeydew", "pos" : (child,0), "code" : "data"})]
        new_node = [(child, {"color" : "limegreen",
                             "pos" : (child, 0),
                             "code" : "data",
                             "block_id" : child_id,
                             "bic" : child_id[0:5]
                            })]
        new_edge = [(parent, child, {"color" : "black"})]
        
        self.mangra.add_nodes_from(new_node)
        self.mangra.add_edges_from(new_edge)
        
        ## add new block data to operation graph
        child = self.opegra.number_of_nodes()
        new_node = [(child, {"color" : "limegreen",
                             "pos" : (child-1, -child),
                             "code" : "data",
                             "block_id" : child_id,
                             "bic" : child_id[0:5]
                            })]
        
        #new_node = [(child, {"color" : "honeydew", "code" : "data"})]
        block_id_list = {i: node["block_id"] for i, node in self.opegra.nodes(data=True)}

        for node in self.opegra.nodes():
            if block_id_list[node] == parents_id:
                parent = node
                print(f"Node {node} has parents_id")
                
        new_edge = [(parent, child, {"code": 'func',
                                         "edge_color": 'cornflowerblue',
                                         "bic" : func_id[0:5]
                                        })]

        self.opegra.add_nodes_from(new_node)
        self.opegra.add_edges_from(new_edge)

    def operation(self, func_id, parents_id=str("00000")):
       #print('parents_id:',parents_id)
        print('operation')

        #exe_com = 'python [func_id]/function.py [parents_id]'
        exe_code = func_id + "/function.py"
        argument = parents_id
        cp = subprocess.run(["python", exe_code, argument], encoding="utf-8", stdout=subprocess.PIPE)

        print(cp.stdout)
        
        child_id = make_data_block()
        self.add_data(child_id, func_id, parents_id)

        return child_id

    def show_managemet_graph(self):
        # ノードの色をセット       
        node_color = [node["color"] for node in self.mangra.nodes.values()]
        node_pos = [node["pos"] for node in self.mangra.nodes.values()]
        #node_label = {i: node["code"] for i, node in self.mangra.nodes(data=True)}
        node_label = {i: node["bic"] for i, node in self.mangra.nodes(data=True)}
        #print(node_label)
        #node_pos = nx.get_node_attributes(mangra,'pos')
        # エッジの色をセット
        edge_color = [edge["color"] for edge in self.mangra.edges.values()]

        fig = plt.figure(figsize=(self.draw_width,self.draw_height))
        plt.axis("off")
        plt.title("management graph")
        nx.draw_networkx(self.mangra, 
                         arrows=True, 
                         node_size=2000,
                         arrowsize=20,
                         arrowstyle='->',
                         edgecolors='black', 
                         pos=node_pos,
                         labels=node_label,
                         #node_shape='s',
                         node_color=node_color)
        
        plt.savefig('management_graph.png', transparent=True)
        
        plt.show()
        plt.close()   
        
    def show_operation_graph(self):
        # ノードの色をセット
        node_color = [node["color"] for node in self.opegra.nodes.values()]
        node_pos = [node["pos"] for node in self.opegra.nodes.values()]
        #node_pos = nx.get_node_attributes(self.opegra,'pos')

        #node_label = {i: node["code"] for i, node in self.opegra.nodes(data=True)}
        node_label = {i: node["bic"] for i, node in self.opegra.nodes(data=True)}
        
        # エッジの色をセット
        edge_color = [edge["edge_color"] for edge in self.opegra.edges.values()]
        #edge_labels = {(i, j): w['code'] for i, j, w in self.opegra.edges(data=True)} 
        edge_labels = {(i, j): w['bic'] for i, j, w in self.opegra.edges(data=True)} 
        #print(edge_labels)
        #エッジラベルの描画時に'code'の表示を無くすための工夫

        #fig = plt.figure(figsize=(self.draw_width,self.draw_height))
        fig = plt.figure(figsize=(self.draw_width,self.draw_width))
        plt.axis("off")
        plt.title("operation graph")
        fsize = 12
        #nx.draw_networkx_edges(self.opegra, node_pos, width=5)
        nx.draw_networkx(self.opegra,
                         arrows=True, 
                         node_size=2000,
                         arrowsize=20,
                         arrowstyle='->',
                         #edgecolors='blue',
                         edgecolors=node_color,
                         #node_color=node_color,
                         node_color='white',
                         linewidths = 2,
                         pos=node_pos, 
                         edge_color=edge_color,
                         width=2,
                         labels=node_label,
                         #node_shape='s',
                         #node_shape='^',
                         font_size=fsize)
                         #edge_labels=edge_labels)
        #エッジのラベルを描画
        nx.draw_networkx_edge_labels(self.opegra, 
        node_pos, 
        edge_labels=edge_labels,
        font_size=fsize) 
        
        plt.savefig('operation_graph.png', transparent=True)

        plt.show()
        plt.close()

if __name__ == '__main__':
        
    ### make root
    print('make root')
    root = Block_Root()
    root.info()
    root.save()

    #mb1 = loadRootBlock()
    #mb1.info()
    delay_time = 5
    #### add function
    function_id1 = make_function_block(py_code, readme)
    root.add_function(function_id1)
    #time.sleep(delay_time)
    ### operation

    data_id1 = root.operation(function_id1)
    #root.add_data(data_id1, function_id1)

    #### add function
    function_id2 = make_function_block(py_code_argv, readme)
    root.add_function(function_id2)
    
    ### operation
    data_id2 = root.operation(function_id2)
    
    data_id3 = root.operation(function_id1, data_id2)
    
    ### show graphes
    root.show_managemet_graph()
    root.show_operation_graph()