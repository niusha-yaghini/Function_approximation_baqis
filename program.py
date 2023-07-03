import Chromosome
import matplotlib.pyplot as plt
import children    
import print_function
import random as rnd
import time
import datetime
import copy


def Termination_condition(best_sofar_mse):
    if(best_sofar_mse<0.0001): return True
    else: return False

def Genetic_to_compare(input_file_name, iteration_number):
    
    amount_of_no_change = 0
    
    f = open(f'{input_file_name}', 'r')
    given_function = f.readline().split(':')[1]
    X = []
    Y = []
    for i in range(input_nodes_amount):
        a = f.readline().split(',')
        X.append(float(a[0]))
        Y.append(float(a[1]))
            
    list_of_parents = Chromosome.all_chromosoms(population_size, X, Y)
    parents_average_mse, parents_best_mse, best_parent = Chromosome.find_best_mse(list_of_parents)
    result.write(f"best mse so far, generation 0: {parents_best_mse}\n")        

    generation_number = []
    average_mse_of_eachGen = []
    best_mse_of_eachGen = []
    best_mse_of_all = []
    best_chromosome_of_eachGen = []
    best_sofar_mse = None
    
    generation_number.append(0)
    average_mse_of_eachGen.append(parents_average_mse)
    best_mse_of_eachGen.append(parents_best_mse)
    best_sofar_mse = parents_best_mse
    best_mse_of_all.append(best_sofar_mse)
    best_chromosome_of_eachGen.append(best_parent)

    i = 0
    for i in range(max_of_generations):
        
        if(Termination_condition(best_sofar_mse)):
            break
        
        if(amount_of_no_change>=no_change_limit):
            break
    
        print(f"iteration {iteration_number} generation {i+1}, best so far mse: {best_sofar_mse}, ", end='') 
        e = datetime.datetime.now()

        print ("time: %s:%s:%s" % (e.hour, e.minute, e.second))

        list_of_children = children.making_children(list_of_parents, type_of_selection, k, pc, pm_changing, pm_increase_probblity, pm_neighbors_amount, X, Y, best_sofar_mse, result, i)
        average_mse, best_mse, best_chr = Chromosome.find_best_mse(list_of_children)

        list_of_parents = list_of_children
        
        generation_number.append(i)
        average_mse_of_eachGen.append(average_mse)
        best_mse_of_eachGen.append(best_mse)
        best_chromosome_of_eachGen.append(copy.deepcopy(best_chr))

        best_sofar_mse = min(best_mse_of_eachGen)
        
        if(best_sofar_mse == best_mse_of_all[-1]):
            amount_of_no_change += 1
        else:
            amount_of_no_change = 0

        best_mse_of_all.append(best_sofar_mse)
            
        best_chromo = Chromosome.Chromosome()
        for chromo in best_chromosome_of_eachGen:
            if chromo.mse==best_sofar_mse:
                best_chromo.str = chromo.str
                best_chromo.chr = chromo.chr
        # print(f"string: {best_chromo.str}, chr: {best_chromo.chr}")
        if(best_chromo.str==None or best_chromo.chr==None):
            print("The choromosome is None")

        
    return best_sofar_mse, i, best_chromo

    
if __name__ == "__main__":
    
    rnd.seed(1)
    photo_number = 4
    text_compare_name = 'result10.txt'

    population_size = 1000  #size of population (0)
    max_of_generations = 500
    iteration_of_genetic = 1

    # coromosoms = 15 bits / 10 bits = coeffisient and 5 bits = power 
    input_nodes_amount = 100
    
    no_change_limit = 50
    
    # parameters of child making function
    # type_of_selection = "roulette_wheel"
    type_of_selection = "tournoment"
    k = 3 # k tournoment parameter
    pc = 0.8 # the probblity of cross-over
    pm1 = 0.02 # the probblity of mutation for low value
    pm2 = 0.01 # the probblity of mutation for high value
    pm_changing = 0.01 # the probblity of mutation that will change and increase for different bits
    pm_increase_probblity = 0.001 # the amount, that is gonna add to pm_changing each time for different bits
    pm_neighbors_amount = 500 # the amount of neighbors that each time for each chromosome our mutation will create

    # parameters for making the next generation
    parents_percent_of_next_generation = 10
    children_percent_of_next_generation = 90
    
    input_file_name = 'in_out.txt'

    result = open(f'{text_compare_name}', 'a')
    result.write(f"mutation with different values (increases probblity = 0.001) and making 10 neighbors each time\n")        
    result.close()

    # get the start time
    st = time.time()
    
    best_mses = []
    sum = 0
    for i in range(iteration_of_genetic):
        iteration_st = time.time()
        result = open(f'{text_compare_name}', 'a')
        
        print(f"iteration number {i}: ")
        mse, gen_num, chromo = Genetic_to_compare(input_file_name, i)
        print(f"mse = {mse}, generation nums = {gen_num} \n")
        sum += mse
        best_mses.append(mse)
        result.write(f"iteration number {i}: ")        
        result.write(f"mse = {mse}, generation nums = {gen_num} \n")
        result.write(f"string: {chromo.str}\n chr: {chromo.chr}\n")
        iteration_et = time.time()
        iteration_elapsed_time = iteration_et - iteration_st
        result.write(f"Execution time of iteration: {iteration_elapsed_time} seconds\n \n")
        
        result.close()

    result = open(f'{text_compare_name}', 'a')
        
    all_min = min(best_mses)
    avg = sum/iteration_of_genetic
    result.write(f"the best mse of all: {all_min} \n")
    result.write(f"the average mse of all: {avg} \n")

    # get the end time
    et = time.time()

    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
    
    result.write(f'Execution time of all: {elapsed_time} seconds')

    result.close()
    
    # get the execution time    

    # for now the new generation is the children

    print()