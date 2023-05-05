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
        choosed_term = rnd.randint(2, terms)                
        child1, child2 = replace_terms(parent1, parent2, choosed_term)
        return child1, child2    
    else:
        return parent1, parent2

def replace_terms(paren1, paren2, choosed_term):
    
    each_term = paren1.coeff_size + paren1.power_size

    child1 = Chromosome.Chromosome()
    child2 = Chromosome.Chromosome()
    
    chr1 = []
    chr2 = []
    
    x = (choosed_term-1) * each_term
        
    chr1.extend(paren1.chr[:x])
    chr1.extend(paren2.chr[x:])
        
    chr2.extend(paren2.chr[:x])
    chr2.extend(paren1.chr[x:])
    
    child1.chr = chr1
    child2.chr = chr2
    
    return child1, child2        

def mutation(children, pm):
    for child in children:
        for bit in child.chr:
            x = rnd.random()
            if(x<=pm):
                if(bit==0): bit=1
                else: bit=0