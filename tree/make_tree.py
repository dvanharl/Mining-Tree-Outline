from helpers import get_data
from tree_tools import *
from pprint import pprint
import json


# first get all the data
data_to_use , attrs = get_data()
dataset = []
for row in data_to_use:
	dataset.append(list(row))

tree_root = {
	"name" : None,
	"children" : []
	}

testset = dataset[0:10]

print "Assuming class index is the last value"

# Gather the class index value
class_candids = []

class_candids , yes_attr , no_attr = find_class_candids(dataset)

tree_root["name"] = ("yes : " + str(yes_attr) + " no: " + str(no_attr))
class_candids = list(set(class_candids))

# raw_input(attrs)


build_tree(tree_root,attrs,testset)

pprint(tree_root)

# The children of the root node is the rule and the dataset or their results


