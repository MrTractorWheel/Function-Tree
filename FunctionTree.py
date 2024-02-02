def datum(Tree): return Tree[0] + "," +  Tree[1]
def left(Tree): return Tree[2]
def right(Tree): return Tree[-1]
def is_empty(Tree): return Tree == []
def create_node(datum,left,right): return [datum,[left],[right]]

def construct_forest(defs): # defs is a list of strigs
    def construct_tree(treeList):
        if treeList == []:
            return []
        else:
            string_tree = treeList[0].replace(" ","")
            tree_list = string_tree.split("=")
            function = tree_list[0][0]
            if "+" in tree_list[1]:
                operator = "+"
                term_list = tree_list[1].split("+")
                term1 = term_list[0]
                term2 = term_list[1]
            elif "-" in tree_list[1]:
                operator = "-"
                term_list = tree_list[1].split("-")
                term1 = term_list[0]
                term2 = term_list[1]
            elif "*" in tree_list[1]:
                operator = "*"
                term_list = tree_list[1].split("*")
                term1 = term_list[0]
                term2 = term_list[1]
            elif "^" in tree_list[1]:
                operator = "^"
                term_list = tree_list[1].split("^")
                term1 = term_list[0]
                term2 = term_list[1]
            else:
                return "invalid operation or no operation"
            return [[function,operator,[term1],[term2]]]+ construct_tree(treeList[1:])
    forest_trees = construct_tree(defs)
    def is_leaf(tree):
        str2 = (str(tree[2])).strip("[]")
        str1 = (str(tree[-1])).strip("[]")
        if '(x)' not in str2:
            if '(x)' not in str1:
                return True
        return False
    def branch_search(forest_trees,forest_list):
        if len(forest_trees) == 0:
            return forest_list
        elif len(forest_trees) > 1:
            tree = forest_trees[0]
            if is_leaf(tree):
                branch = [forest_trees[0][0]+"(x)"]
                i=0
                while i < len(forest_trees):
                    if branch == forest_trees[i][2]:
                        forest_trees[i][2] = forest_trees[0] 
                        forest_trees.pop(0)
                        return branch_search(forest_trees,forest_list)
                    if branch == forest_trees[i][-1]:
                        forest_trees[i][-1] = forest_trees[0] 
                        forest_trees.pop(0)
                        return branch_search(forest_trees,forest_list)
                    else: i += 1
                forest_list.append(tree)
                forest_trees.pop(0)
                return branch_search(forest_trees,forest_list)
            else:
                newList = forest_trees[1::]+[forest_trees[0]]
                return branch_search(newList,forest_list)
        elif len(forest_trees) == 1:
            if is_leaf(forest_trees[0]):
                forest_list.append(forest_trees[0])
                forest_trees.pop(0)
                return branch_search(forest_trees,forest_list)
            else: return "input mistake"
    forest1 = branch_search(forest_trees,[])
    forest = forest1[::-1]
    return forest
    
        
        
    
