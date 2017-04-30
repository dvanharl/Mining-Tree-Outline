import math
from pprint import pprint
class_candids = None
attr_candids = None
attrs = None

def build_tree(root, attrs_t , dataset):
	global class_candids
	global attrs
	attrs = attrs_t
	attr_candids = get_attr_vals(dataset)
	split_lists = []
	# raw_input("This is the size from the input : " + str(len(dataset[0])))
	for attr_index in xrange(0 , len(dataset[0])):
		try:
			split_lists.append(split_attr(attr_index  , attr_candids[attr_index] , dataset))
		except:
			raw_input(root)
			raw_input(dataset)
			raw_input(attr_candids)
			raw_input(attr_index)
	selected_attrs = best_split(split_lists)	
	if selected_attrs < 0:
		raw_input(split_lists)
		return None
	try:	
		for row in split_lists[selected_attrs]:
			root["children"].append(make_node(row[0] , len(attr_candids[selected_attrs]) , selected_attrs))
	except:
		raw_input(selected_attrs)
	# remove that item from dataset
	# raw_input("This is the size: " + str(len(dataset[0])))
	for row in dataset:
		del row[selected_attrs]
	# raw_input("This is the size after: " + str(len(dataset[0])))
	#raw_input(dataset)
	# Do the same for each child
	
	
	for child in root["children"]:
		build_tree(child , attrs , dataset)
	
	
# 	pprint(root)
	# pass split_lists into best_split
	# --> 
	# 	pass split_list[x] into gini split
	# 	-->	
	# 		pass split_list[x][y] into gini
	
	##Calculate best split
	#best_index = best_split(split_lists)
	#best_attr = split_lists[best_index]
	
	##Form tree
	#Tree = root ++ best_attr
	
	##Remove best_split attribute from dataset
	#class_candids.remove(best_attr)
	
	##If number of remaining attributes is 1, return, otherwise, recurse
	#if len(class_candids) == 1:
		#return 
	#else:
		#return build_tree(tree, dataset)
	# pprint(split_lists[0])

def split_attr(index , value_candids , dataset):
	split_datasets = []
	for val in value_candids:
		split_dataset = []
		for row in dataset:	
			if row[index] == val:
				split_dataset.append(row)
		split_datasets.append( (val , split_dataset) )
	return split_datasets


def get_attr_vals(dataset):
	attr_vals = []
	# raw_input(dataset[0])
	for attr in xrange(0,len(dataset[0])):
		all_vals = []
		for row in dataset:
			all_vals.append(row[attr])
		attr_vals.append(tuple(set(all_vals)))
	return attr_vals		

def find_class_candids(dataset):
	global class_candids
	attr_num = len(dataset[0])
	class_index = attr_num - 1
	class_candids_t = []	
	yes_attr = 0
	no_attr = 0
	for row in dataset:
		if row[class_index] == "no":
			no_attr += 1
		else:
			yes_attr += 1

		class_candids_t.append(row[class_index])
	class_candids = list(set(class_candids_t))
	return list(set(class_candids_t)) , yes_attr , no_attr



def prob(index, value , dataset):
	count = 1.0
	for data in dataset:
		if data[index] == value:
			count += 1
		
	return float(float(count)/len(dataset))

def get_probs(class_index , class_candids , split_dataset):
	class_split = [None for x in xrange(0,len(class_candids))]
	for index , candid in enumerate(class_candids):
		class_split[index] = (candid , prob(class_index , candid , split_dataset))
	return class_split


def entropy(class_index , class_candids , split_dataset):
	class_split = get_probs(class_index , class_candids , split_dataset)
	entropy_val = 0
	for candid , class_val in class_split:
		entropy_val += -(class_val*math.log(class_val , 2))

	return entropy_val

def info_gain(parent_entropy , all_splits):
	info_list = []
	for attr, split_val in all_splits:
		info_list.append( (attr, parent_entropy - split_val) )
	return info_list

#Addition of best_split
def best_split(all_splits):
	min_gini = 2147483647
	best_attr = -1
	
	#Iterate to find best attribute in list
	for index,attr in enumerate(all_splits):
		g_index_attr = gini_split(attr)
		if(g_index_attr < min_gini):
			min_gini = g_index_attr
			best_attr = index
			
	#Return best attribute index; If none found, return -1
	return best_attr

#Attempted Implementation of gini_split
def gini_split(attr):
	global attr_candids
	size = 0
	g_index = 0
	size = 0
	
	#Get total number of occurances from all children
	for val,split in enumerate(attr):
		size += len(split)
		
	#Compute Gini index value
	for val,split in attr:
		gini_v = gini(len(split[0])-1,class_candids ,split)
		ratio =len(split)/size
		g_index += (gini_v * ratio)
	return g_index

def gini(class_index , class_candids , split_dataset):
	class_split = get_probs(class_index , class_candids , split_dataset)
	gini_val = 0
	for candid , class_val in class_split:
		gini_val += -(class_val*class_val)
	return 1 - gini_val
	
def make_node(name , attr_num , attr_index):
	node = {
		"name" : attrs[attr_index] + " = " + name,
		"children" : []
	}
	return node


