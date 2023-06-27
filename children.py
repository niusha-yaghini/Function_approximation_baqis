import copy
import random as rnd
import Chromosome


def making_children(list_of_parents, type_of_selection, k, pc, pm_changing, pm_increase_probblity, pm_neighbors_amount, list_x, actual_y, best_sofar_mse, result, gen_num):
    # here we make children base on:
    #           choosing parents: type_of_selection
    #           cross over: cross_over_one_point
    #           mutation: mutation_different_value, if we had provement we do neighbor thing
    
    # the parents that we take, have mse values set
    # after cross overing we set the new mses and gave them to mutation
    # in mutation each time the new mses will set
    
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

    mutation_different_value(children, pm_changing, pm_increase_probblity)
    Chromosome.all_mse(children, list_x, actual_y)
    child = finding_best_child(children)
    result.write(f"best child mse before mutation, generation {gen_num}: {child.mse}\n")        

    
    # if(child.mse<best_sofar_mse):
    mutation_different_value_with_neighbors_singleChr(child, pm_changing, pm_increase_probblity, pm_neighbors_amount, list_x, actual_y)
    result.write(f"best child mse after mutation, generation {gen_num}: {child.mse}\n")        
        
    return children

def tournament_selection(p_chrs, k):
    # in here we choose parents for cross over with tournoment method
    
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
    # in here we choose parents for cross over with roulette wheel method
    
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
    # in here first we choose a random term, then we change the second part of parents to each other (with cross-over-rate (pc))
    
    terms = parent1.term_size
    
    x = rnd.random()
    if(x<=pc):
        choosed_term = rnd.randint(2, terms)                
        child1, child2 = replace_terms(parent1, parent2, choosed_term)
        return child1, child2    
    else:
        return parent1, parent2

def replace_terms(paren1, paren2, choosed_term):
    # in here we change parts of our choromosome base on choosed term
    
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
        
def mutation_different_value(children, pm_changing, pm_increase_probblity):
    # here we do the mutation on different bits by different chance each bits chance increases by 0.001
    # pm2<pm1

    term = 9
    coeff = 10
    power = 5
    for child in children:
        for t in range(term):
            pm = pm_changing
            x = t*(coeff+power)
            #coeff
            for i in range(x, coeff+x):
                r = rnd.random()
                if(r<=pm):
                    if(child.chr[i]==0): child.chr[i]=1
                    else: child.chr[i]=0
                pm += pm_increase_probblity
            
            x += coeff   
            pm = pm_changing
            #power
            for h in range(x, power+x):
                r = rnd.random()
                if(r<=pm):
                    if(child.chr[h]==0): child.chr[h]=1
                    else: child.chr[h]=0
                pm += pm_increase_probblity

def mutation_for_neighbors(child, pm_changing, pm_increase_probblity):
    # here we do the mutation on different bits by different chance each bits chance increases by pm_increase_probblity
    # we take one chromosome and do the mutation on a copy of it, and return the copy

    new_child = copy.deepcopy(child)

    term = 9
    coeff = 10
    power = 5
    for t in range(term):
        pm = pm_changing
        x = t*(coeff+power)
        #coeff
        for i in range(x, coeff+x):
            r = rnd.random()
            if(r<=pm):
                if(new_child.chr[i]==0): new_child.chr[i]=1
                else: new_child.chr[i]=0
            pm += pm_increase_probblity
        
        x += coeff   
        pm = pm_changing
        #power
        for h in range(x, power+x):
            r = rnd.random()
            if(r<=pm):
                if(new_child.chr[h]==0): new_child.chr[h]=1
                else: new_child.chr[h]=0
            pm += pm_increase_probblity
            
    return new_child

def make_neighbors(child, pm_changing, pm_increase_probblity, neighbors_amount, list_x, actual_y):
    # in here we make neighbors_amount of neighbors for a single choromosome
    # and also we set the mse of them here
        
    all_neighbors = []
    for i in range(neighbors_amount):
        neighbor = mutation_for_neighbors(child, pm_changing, pm_increase_probblity)
        neighbor.mse = Chromosome._mse(neighbor, list_x, actual_y)
        all_neighbors.append(neighbor)
    return all_neighbors
        
def finding_best_child(children):
    # in here we seach between all made neighbors, and we return the choromosome with best mse
    
    best_mse = float('inf')
    best_child = None
    for child in children:
        if(best_mse>child.mse):
            best_mse = child.mse
            best_child = child
            
    return best_child
        
def mutation_different_value_with_neighbors_singleChr(child, pm_changing, pm_increase_probblity, pm_neighbors_amount, list_x, actual_y):
        
    provement = True

    while(provement):
        all_neighbors = make_neighbors(child, pm_changing, pm_increase_probblity, pm_neighbors_amount, list_x, actual_y)
        best_neighbor = finding_best_child(all_neighbors)
        if(best_neighbor.mse<child.mse):
            # print(f"imporoved!, child = {child.mse}, imporoved = {best_neighbor.mse}")
            child.mse = best_neighbor.mse
            child.chr = best_neighbor.chr
            child.str = best_neighbor.str
        else:
            provement = False