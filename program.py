import Chromosome
import matplotlib.pyplot as plt
import children    
import print_function
import random as rnd
import time
import datetime


def Termination_condition(min_mse):
    if(min_mse<0.0001): return True
    else: return False

def Genetic_to_compare(input_file_name):
    
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
    
    generation_number = []
    average_mse_of_eachGen = []
    best_mse_of_eachGen = []
    best_mse_of_all = []
    best_chromosome = []
    min_mse = None
    

    generation_number.append(0)
    average_mse_of_eachGen.append(parents_average_mse)
    best_mse_of_eachGen.append(parents_best_mse)
    min_mse = parents_best_mse
    best_mse_of_all.append(min_mse)
    best_chromosome.append(best_parent)

    i = 0
    for i in range(max_of_generations):
        
        if(Termination_condition(min_mse)):
            break
        
        if(amount_of_no_change>=no_change_limit):
            break
    
        print(f"generation number {i+1}, best so far mse: {min_mse}, ", end='') 
        e = datetime.datetime.now()

        print ("time: %s:%s:%s" % (e.hour, e.minute, e.second))

        list_of_children = children.making_children(list_of_parents, type_of_selection, k, pc, pm_changing, pm_increase_probblity, pm_neighbors_amount, X, Y, min_mse)
        average_mse, best_mse, best_chr = Chromosome.find_best_mse(list_of_children)

        list_of_parents = list_of_children
        
        generation_number.append(i)
        average_mse_of_eachGen.append(average_mse)
        best_mse_of_eachGen.append(best_mse)
        min_mse = min(best_mse_of_eachGen)
        
        if(min_mse == best_mse_of_all[-1]):
            amount_of_no_change += 1
        else:
            amount_of_no_change = 0
            
        best_mse_of_all.append(min_mse)
        best_chromosome.append(best_chr)

    return min_mse, amount_of_no_change, i

    
if __name__ == "__main__":
    
    # rnd.seed(1)
    photo_number = 4
    text_compare_name = 'result7.txt'

    population_size = 1000  #size of population (0)
    max_of_generations = 400
    iteration_of_genetic = 30


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
    pm_neighbors_amount = 10 # the amount of neighbors that each time for each chromosome our mutation will create


    # parameters for making the next generation
    parents_percent_of_next_generation = 10
    children_percent_of_next_generation = 90
    
    input_file_name = 'in_out.txt'
        

    result = open(f'{text_compare_name}', 'a')
    result.write(f"mutation with different values (increases probblity = 0.001) and making 10 neighbors each time\n")        

    # get the start time
    st = time.time()
    
    best_mses = []
    sum = 0
    for i in range(iteration_of_genetic):
        print(f"iteration number {i}: ")
        mse, no_change, gen_num = Genetic_to_compare(input_file_name)
        print(f"mse = {mse}, generation nums = {gen_num} \n")
        sum += mse
        best_mses.append(mse)
        result.write(f"iteration number {i}: ")        
        result.write(f"mse = {mse}, generation nums = {gen_num} \n")
        
    # get the end time
    et = time.time()

    all_min = min(best_mses)
    avg = sum/iteration_of_genetic
    result.write(f"the best mse of all: {all_min} \n")
    result.write(f"the average mse of all: {avg} \n")
    # result.write('Execution time:', elapsed_time, 'seconds')

    result.close()
    
    # get the execution time    
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')

    # for now the new generation is the children

    print()