import copy
import random as rnd
import Chromosome

def making_children(list_of_parents, type_of_selection, k, pc, pm):
    # we want to make children on base of a list of trees (parent_trees)
    
    lenght = len(list_of_parents)
    children = []
    
    for i in range(int(lenght/2)):
        
        if(type_of_selection == "tournoment"):
            parent1, parent2 = tournament_selection(list_of_parents, k)     
        elif(type_of_selection == "roulette_wheel"):   
            parent1, parent2 = roulette_wheel_selection(list_of_parents)        

        child1, child2 = cross_over_one_point(parent1, parent2, pc)
        children.append(child1)
        children.append(child2)
    
    mutation(children, pm)
    
    return children

def tournament_selection(p_chrs, k):
    # using the tournament preceture for selecting a couple tree
    # in this method we choose 3 tree randomly 2 times (2 times becuase we want a couple), and select the best-mae tree
    
    couple_parent = []
    
    for j in range(2):
        best_mse = float('inf')
        best_chr = None
        for z in range(k):
            chr = rnd.choice(p_chrs)  
            
            if(chr.mse<best_mse):
                best_mse = chr.mse
                best_chr = chr        
        couple_parent.append(best_chr)
    return couple_parent[0], couple_parent[1]       
        
def roulette_wheel_selection(p_chrs):
    # how much the mae is smaller the probbility of choosing it increases
    
    couple_parent = []
    
    for i in range(2):

        sum_mse = sum([(1/(c.mse+1)) for c in p_chrs])
        
        #this is going to choose a number between 0 and 1    
        p = rnd.random()
        s = 0
        
        flag = True
        for c in p_chrs:
            if(flag):
                if(p < (((1/(c.mse+1)) / sum_mse) + s)):
                    couple_parent.append(c)
                    flag = False
                else:
                    s += (1/(c.mse+1))/sum_mse    
    return couple_parent[0], couple_parent[1]     

def cross_over_one_point(parent1, parent2, pc):
    # doing the cross-over with the given cross-over-rate (pc), on 2 tree
    terms = parent1.term_size
    
    x = rnd.random()
    if(x<=pc):
        
        # making the child nodes for changing nodes        
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)        
        
        choosed_term = rnd.randint(1, 9)
                
        replace_terms(child1, child2, choosed_term)

        return child1, child2    
    else:
        return parent1, parent2

def replace_terms(child1, child2, choosed_term):
    
    
    
    
    
    # change the specific node1 in tree1 with the specific node2 in tree2 with each other
    #       and making new trees as children
    
    queue1 = []
    queue1.append(child_root1)
    
    # making a cope of node1, because we will lose it after we change it with node2
    cn1 = copy.deepcopy(choosed_node1)
    
    # searching in tree1 untill we find our specific node, and changing it with node2
    flag1 = True
    while flag1:
        node = queue1.pop()
        if(node!=choosed_node1):
            for i in range(len(node.children)):
                queue1.append(node.children[i])
        else:
            node.depth = choosed_node2.depth
            node.operator = choosed_node2.operator
            node.children = copy.deepcopy(choosed_node2.children)
            node.is_leaf = choosed_node2.is_leaf
            flag1 = False
            
    queue2 = []
    queue2.append(child_root2)
         
    # searching in tree2 untill we find our specific node, and changing it with node1 (cn1)  
    flag2 = True
    while flag2:
        node = queue2.pop()
        if(node!=choosed_node2):
            for j in range(len(node.children)):
                queue2.append(node.children[j])
        else:
            node.depth = cn1.depth
            node.operator = cn1.operator
            node.children = copy.deepcopy(cn1.children)
            node.is_leaf = cn1.is_leaf
            flag2 = False          
        

        
def change_node(root, choosed_node):

    queue = []
    queue.append(root)
        
    # searching in tree1 untill we find our specific node, and changing it with node2
    flag = True
    while flag:
        node = queue.pop()
        if(node!=choosed_node):
            for i in range(len(node.children)):
                queue.append(node.children[i])
        else:
            d = node.depth
            t = tree.Tree(d)
            t._fit()
            node.depth = t.root.depth
            node.operator = t.root.operator
            node.children = t.root.children
            node.is_leaf = t.root.is_leaf
            flag = False
          
def subtree_mutation(children, pm):
    
    for child in children:
        x = rnd.random()
        if(x<=pm):

            nodes = []
            make_list_node(child.root, nodes)
            
            # choosing a node to change
            choosed_node = rnd.choice(nodes)
            
            change_node(child.root, choosed_node)
            
            # child.print_tree()
         
def make_list_node_leaf(root, leaf_nodes):
    # making a list of leaf nodes in our tree
    
    if(root.is_leaf==True):
        leaf_nodes.append(root)

    if(len(root.children)!=0):
        for i in root.children:
            make_list_node(i, leaf_nodes)
                
    return leaf_nodes

def leaf_mutation(children, pm):
    for child in children:
        x = rnd.random()
        if(x<=pm):

            leaf_nodes = []
            make_list_node_leaf(child.root, leaf_nodes)
            
            # choosing a node to change
            choosed_node = rnd.choice(leaf_nodes)
            
            change_node(child.root, choosed_node)
            
            # child.print_tree()        
          
