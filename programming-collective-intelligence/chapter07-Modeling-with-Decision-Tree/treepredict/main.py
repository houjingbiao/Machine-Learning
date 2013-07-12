import os
os.chdir('D:\\Machine-Learning\\trunk\\programming-collective-intelligence\\chapter07-Modeling-with-Decision-Tree\\treepredict')
import treepredict

mydata = [treepredict.dataType(line.split('\t')[0], line.split('\t')[1], line.split('\t')[2], 
                   line.split('\t')[3], line.split('\t')[4])
          for line in file('decision_tree_example.txt')]

tree = treepredict.TreeNode(None, False, mydata)

print('Hello World')
