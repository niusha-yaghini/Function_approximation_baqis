import Chromosome
import matplotlib.pyplot as plt
import children    
import print_function
import random as rnd


def draw_average_mse(x_generation_number, y_average_mse_of_each, given_function):
    fig, ax = plt.subplots()
    average_of_each, = plt.plot(x_generation_number, y_average_mse_of_each, label='average mse of each generation')
    ax.set_title(f"function = {given_function}, population = {population_size}")
    ax.legend(handles=[average_of_each])
    name = f"average_{photo_number}_" + str(population_size) + '.png'

    plt.savefig(name)
    plt.show()

def draw_best_mse(x_generation_number, y_best_mse_of_each, y_best_mse_of_all, given_function, y_min_mse):
    
    fig, ax = plt.subplots()
    best_of_each,  = plt.plot(x_generation_number, y_best_mse_of_each, label='best mse of this generation')
    best_of_all, = plt.plot(x_generation_number, y_best_mse_of_all, label='best mse of all generations since now')

    ax.set_title(f"function: {given_function}, population_num: {population_size}, generations_num: {amount_of_generations}, min_mse: {y_min_mse}")
    ax.legend(handles=[best_of_each, best_of_all])
    name = f"result_{photo_number}_" + str(population_size) + '.png'

    print("best mse: ", y_min_mse)

    plt.savefig(name)
    plt.show()

def Termination_condition(min_mse):
    if(min_mse<0.0001): return True
    else: return False

def Genetic(input_file_name):
    
    f = open(f'{input_file_name}', 'r')
    given_function = f.readline().split(':')[1]
    X = []
    Y = []
    for i in range(input_nodes_amount):
        a = f.readline().split(',')
        X.append(float(a[0]))
        Y.append(float(a[1]))
        
    # population number zero
    print("population number 0\n")
    list_of_parents = Chromosome.all_chromosoms(population_size)
    parents_average_mse, parents_best_mse, best_parent = Chromosome._mse(list_of_parents, X, Y)
    
    # making lists for showing 
    generation_number = []
    average_mse_of_eachGen = []
    best_mse_of_eachGen = []
    best_mse_of_all = []
    best_chromosome = []
    min_mse = None
    
    # appending 0 generation information
    generation_number.append(0)
    average_mse_of_eachGen.append(parents_average_mse)
    best_mse_of_eachGen.append(parents_best_mse)
    min_mse = parents_best_mse
    print("best mse so far: ", min_mse)
    best_mse_of_all.append(min_mse)
    best_chromosome.append(best_parent)

    for i in range(amount_of_generations):
        
        if(Termination_condition(min_mse)):
            return
    
        print(f"population number {i+1}")
        list_of_children = children.making_children(list_of_parents, type_of_selection, k, pc, pm)
        
        average_mse, best_mse, best_chr = Chromosome._mse(list_of_children, X, Y)
        list_of_parents = list_of_children
        
        generation_number.append(i)
        average_mse_of_eachGen.append(average_mse)
        best_mse_of_eachGen.append(best_mse)
        min_mse = min(best_mse_of_eachGen)
        print("best mse so far: ", min_mse)
        best_mse_of_all.append(min_mse)
        best_chromosome.append(best_chr)

    final_best_chr = None
    for c in best_chromosome:
        if c.mse==min_mse:
            final_best_chr = c

    # return min_mse
    draw_best_mse(generation_number, best_mse_of_eachGen, best_mse_of_all, given_function, min_mse)
    
    print(final_best_chr.str)
    # print_function.print_func(X, Y, final_best_chr, given_function, final_best_chr.str, photo_number)

    draw_average_mse(generation_number, average_mse_of_eachGen, given_function)

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
        
    list_of_parents = Chromosome.all_chromosoms(population_size)
    parents_average_mse, parents_best_mse, best_parent = Chromosome._mse(list_of_parents, X, Y)
    
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
    for i in range(amount_of_generations):
        
        if(Termination_condition(min_mse)):
            break
        
        if(amount_of_no_change>=no_change_limit):
            break
    
        list_of_children = children.making_children(list_of_parents, type_of_selection, k, pc, pm)
        
        average_mse, best_mse, best_chr = Chromosome._mse(list_of_children, X, Y)
        list_of_parents = list_of_children
        
        generation_number.append(i)
        average_mse_of_eachGen.append(average_mse)
        best_mse_of_eachGen.append(best_mse)
        min_mse = min(best_mse_of_eachGen)
        
        l = len(best_mse_of_all)
        if(min_mse==best_mse_of_all[l-1]):
            amount_of_no_change+=1
        else:
            amount_of_no_change = 0
            
        best_mse_of_all.append(min_mse)
        best_chromosome.append(best_chr)

    return min_mse, amount_of_no_change, i


    
if __name__ == "__main__":
    
    # rnd.seed(1)
    
    photo_number = 4
    
    # parameters
    input_nodes_amount = 100

    # population size (0)
    population_size = 1000
    
    # coromosoms = 15 bits / 10 bits = coeffisient and 5 bits = power 

    k = 3 # k tournoment parameter
    pc = 0.8 # the probblity of cross-over
    pm = 0.02 # the probblity of mutation(leaf_mutation)

    amount_of_generations = 200
    
    parents_percent_of_next_generation = 10
    children_percent_of_next_generation = 90
    
    input_file_name = 'in_out.txt'
    
    type_of_selection = "tournoment"
    # type_of_selection = "roulette_wheel"
    
    no_change_limit = 40
    
    iteration = 30

    result = open('result6.txt', 'w')

    best_mses = []
    sum = 0
    for i in range(iteration):
        print(f"iteration number {i}: ")
        mse, no_change, gen_num = Genetic_to_compare(input_file_name)
        print(f"mse = {mse}, generation nums = {gen_num} \n")
        sum += mse
        best_mses.append(mse)
        result.write(f"iteration number {i}: ")        
        result.write(f"mse = {mse}, generation nums = {gen_num} \n")
        
    all_min = min(best_mses)
    avg = sum/iteration
    result.write(f"the best mse of all: {all_min} \n")
    result.write(f"the average mse of all: {avg} \n")
    
    result.close()
    
    # for now the new generation is the children

    print()