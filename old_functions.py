# import Chromosome
# import matplotlib.pyplot as plt
# import children    
# import print_function
# import random as rnd
# import time


# # in program 

# def draw_average_mse(x_generation_number, y_average_mse_of_each, given_function):
#     fig, ax = plt.subplots()
#     average_of_each, = plt.plot(x_generation_number, y_average_mse_of_each, label='average mse of each generation')
#     ax.set_title(f"function = {given_function}, population = {population_size}")
#     ax.legend(handles=[average_of_each])
#     name = f"average_{photo_number}_" + str(population_size) + '.png'

#     plt.savefig(name)
#     plt.show()

# def draw_best_mse(x_generation_number, y_best_mse_of_each, y_best_mse_of_all, given_function, y_min_mse):
    
#     fig, ax = plt.subplots()
#     best_of_each,  = plt.plot(x_generation_number, y_best_mse_of_each, label='best mse of this generation')
#     best_of_all, = plt.plot(x_generation_number, y_best_mse_of_all, label='best mse of all generations since now')

#     ax.set_title(f"function: {given_function}, population_num: {population_size}, generations_num: {amount_of_generations}, min_mse: {y_min_mse}")
#     ax.legend(handles=[best_of_each, best_of_all])
#     name = f"result_{photo_number}_" + str(population_size) + '.png'

#     print("best mse: ", y_min_mse)

#     plt.savefig(name)
#     plt.show()


# def Genetic(input_file_name):
    
#     f = open(f'{input_file_name}', 'r')
#     given_function = f.readline().split(':')[1]
#     X = []
#     Y = []
#     for i in range(input_nodes_amount):
#         a = f.readline().split(',')
#         X.append(float(a[0]))
#         Y.append(float(a[1]))
        
#     # population number zero
#     print("population number 0\n")
#     list_of_parents = Chromosome.all_chromosoms(population_size)
#     parents_average_mse, parents_best_mse, best_parent = Chromosome.all_mse(list_of_parents, X, Y)
    
#     # making lists for showing 
#     generation_number = []
#     average_mse_of_eachGen = []
#     best_mse_of_eachGen = []
#     best_mse_of_all = []
#     best_chromosome = []
#     min_mse = None
    
#     # appending 0 generation information
#     generation_number.append(0)
#     average_mse_of_eachGen.append(parents_average_mse)
#     best_mse_of_eachGen.append(parents_best_mse)
#     min_mse = parents_best_mse
#     print("best mse so far: ", min_mse)
#     best_mse_of_all.append(min_mse)
#     best_chromosome.append(best_parent)

#     for i in range(amount_of_generations):
        
#         if(Termination_condition(min_mse)):
#             return
    
#         print(f"population number {i+1}")
#         list_of_children = children.making_children(list_of_parents, type_of_selection, k, pc, pm1, pm2)
        
#         average_mse, best_mse, best_chr = Chromosome.all_mse(list_of_children, X, Y)
#         list_of_parents = list_of_children
        
#         generation_number.append(i)
#         average_mse_of_eachGen.append(average_mse)
#         best_mse_of_eachGen.append(best_mse)
#         min_mse = min(best_mse_of_eachGen)
#         print("best mse so far: ", min_mse)
#         best_mse_of_all.append(min_mse)
#         best_chromosome.append(best_chr)

#     final_best_chr = None
#     for c in best_chromosome:
#         if c.mse==min_mse:
#             final_best_chr = c

#     # return min_mse
#     draw_best_mse(generation_number, best_mse_of_eachGen, best_mse_of_all, given_function, min_mse)
    
#     print(final_best_chr.str)
#     # print_function.print_func(X, Y, final_best_chr, given_function, final_best_chr.str, photo_number)

#     draw_average_mse(generation_number, average_mse_of_eachGen, given_function)



# # ---------------------------------------------------------------------------

# # in chromosome

# def old_all_mse(chr_list, list_x, actual_y):
#     sum_mse = 0
#     best_mse = float('inf')
#     best_chr = None
#     for c in chr_list:
#         predicted_y = calculator(list_x, c)
#         c.mse = mean_squared_error(actual_y, predicted_y)     

#         sum_mse += c.mse
#         if (c.mse<best_mse):
#             best_mse = c.mse
#             best_chr = c

#     return sum_mse/len(chr_list), best_mse, best_chr


# # -----------------------------------------------------------------------------

# # in children

# def making_children_keep(list_of_parents, type_of_selection, k, pc, pm1, pm2, list_x, actual_y):
#     # we want to make children, our mutation here is different pm value and keeping the best
    
#     lenght = len(list_of_parents)
#     children = []
    
#     for i in range(int(lenght/2)):
        
#         if(type_of_selection == "tournoment"):
#             parent1, parent2 = tournament_selection(list_of_parents, k)     
#         elif(type_of_selection == "roulette_wheel"):   
#             parent1, parent2 = roulette_wheel_selection(list_of_parents)        

#         child1, child2 = cross_over_one_point(parent1, parent2, pc)
#         children.append(child1)
#         children.append(child2)
        
#     Chromosome.all_mse(children, list_x, actual_y)
#     mutation_different_value_keep_best(children, pm1, pm2, list_x, actual_y)
    
#     return children



# def mutation(children, pm):
#     # this is the first version of mutation, a simple and regular one
    
#     for child in children:
#         for bit in child.chr:
#             x = rnd.random()
#             if(x<=pm):
#                 if(bit==0): bit=1
#                 else: bit=0
                
                
# def mutation_different_value_half(children, pm1, pm2, amount):
#     # in here we do the different pms on half of coeff and power of each term\
        
#     # x = (choosed_term-1) * each_term
#     term = 9
#     coeff = 10
#     co1 = 5
#     co2 = 5
#     power = 5
#     po1 = 2
#     po2 = 3
    
#     for child in children:
#         for t in range(term):
#             x = t*(coeff+power)
#             #coeff
#             for i in range(x, co1+x):
#                 r = rnd.random()
#                 if(r<=pm2):
#                     if(child.chr[i]==0): child.chr[i]=1
#                     else: child.chr[i]=0
#             x += co1

#             for j in range(x, co2+x):
#                 r = rnd.random()
#                 if(r<=pm1):
#                     if(child.chr[j]==0): child.chr[j]=1
#                     else: bit=0
#             x += co2
                
#             #power
#             for h in range(x, po1+x):
#                 r = rnd.random()
#                 if(r<=pm2):
#                     if(child.chr[h]==0): child.chr[h]=1
#                     else: child.chr[h]=0
#             x += po1

#             for z in range(x, po2+x):
#                 r = rnd.random()
#                 if(r<=pm1):
#                     if(child.chr[z]==0): child.chr[z]=1
#                     else: child.chr[z]=0


# def mutation_different_value(children, pm_mutation):
#     # here we do the mutation on different bits by different chance each bits chance increases by 0.001
#     # pm2<pm1

#     term = 9
#     coeff = 10
#     power = 5
#     for child in children:
#         for t in range(term):
#             pm = pm_mutation
#             x = t*(coeff+power)
#             #coeff
#             for i in range(x, coeff+x):
#                 r = rnd.random()
#                 if(r<=pm):
#                     if(child.chr[i]==0): child.chr[i]=1
#                     else: child.chr[i]=0
#                 pm+=0.001
            
#             x += coeff   
#             pm = pm_mutation
#             #power
#             for h in range(x, power+x):
#                 r = rnd.random()
#                 if(r<=pm):
#                     if(child.chr[h]==0): child.chr[h]=1
#                     else: child.chr[h]=0
#                 pm+=0.001


# def mutation_different_value_keep_best(children, pm1, pm2, list_x, actual_y):
#     # in here we do the mutation on half of bits of each coeff and power of each term with different pms

#     # after each time doing mutation on 1 whole term, if we had provement we keep going,
#     # if we had not any porovement we stop and return the choromosome that we have made 
    
#     # this function has a problem because after some times doing mutation if we reach to a point that we do not have any provement
#     # it return the latest version that it had created, but it replace the latest best chromosome(i mean assume that we only have one time doing mutation
#     # and there is no provement we replace our node with new one and we are done and its okay, now assume that we have done mutation several times
#     # and in last ones each time we had provements and now we do not have, so we should replace our node with the last one that was better,
#     # not with the latest version that is not as good as the things that we had made before)
    
#     # x = (choosed_term-1) * each_term
#     term = 9
#     coeff = 10
#     co1 = 5
#     co2 = 5
#     power = 5
#     po1 = 2
#     po2 = 3
#     provement = True
#     for child in children:
#         old_mse = child.mse
#         while(provement):
#             for t in range(term):
#                 x = t*(coeff+power)
#                 #coeff
#                 for i in range(x, co1+x):
#                     r = rnd.random()
#                     if(r<=pm2):
#                         if(child.chr[i]==0): child.chr[i]=1
#                         else: child.chr[i]=0
#                 x += co1

#                 for j in range(x, co2+x):
#                     r = rnd.random()
#                     if(r<=pm1):
#                         if(child.chr[j]==0): child.chr[j]=1
#                         else: child.chr[j]=0
#                 x += co2
                    
#                 #power
#                 for h in range(x, po1+x):
#                     r = rnd.random()
#                     if(r<=pm2):
#                         if(child.chr[h]==0): child.chr[h]=1
#                         else: child.chr[h]=0
#                 x += po1

#                 for z in range(x, po2+x):
#                     r = rnd.random()
#                     if(r<=pm1):
#                         if(child.chr[z]==0): child.chr[z]=1
#                         else: child.chr[z]=0
            
#             new_mse = Chromosome._mse(child, list_x, actual_y)
#             child.mse = new_mse
#             if(new_mse>=old_mse):
#                 provement = False
#             else:
#                 old_mse = new_mse


# def mutation_different_value_singleChr(child, pm_changing, pm_increase_probblity):
#     # here we do the mutation on different bits by different chance each bits chance increases by pm_increase_probblity
#     # we take one chromosome and do the mutation on a copy of it, and return the copy

#     new_child = copy.deepcopy(child)

#     term = 9
#     coeff = 10
#     power = 5
#     for t in range(term):
#         pm = pm_changing
#         x = t*(coeff+power)
#         #coeff
#         for i in range(x, coeff+x):
#             r = rnd.random()
#             if(r<=pm):
#                 if(new_child.chr[i]==0): new_child.chr[i]=1
#                 else: new_child.chr[i]=0
#             pm += pm_increase_probblity
        
#         x += coeff   
#         pm = pm_changing
#         #power
#         for h in range(x, power+x):
#             r = rnd.random()
#             if(r<=pm):
#                 if(new_child.chr[h]==0): new_child.chr[h]=1
#                 else: new_child.chr[h]=0
#             pm += pm_increase_probblity
            
#     return new_child


# def make_neighbors_for_mutation(child, pm_changing, pm_increase_probblity, neighbors_amount, list_x, actual_y):
#     # in here we make neighbors_amount of neighbors for a single choromosome
#     # and also we set the mse of them here
    
#     all_neighbors = []
#     for i in range(neighbors_amount):
#         neighbor = mutation_different_value_singleChr(child, pm_changing, pm_increase_probblity)
#         neighbor.mse = Chromosome._mse(neighbor, list_x, actual_y)
#         all_neighbors.append(neighbor)
#     return all_neighbors
        
# def finding_best_neighbor(neighbors):
#     # in here we seach between all made neighbors, and we return the choromosome with best mse
    
#     best_mse = float('inf')
#     best_neighbor = None
#     for n in neighbors:
#         if(best_mse>n.mse):
#             best_mse = n.mse
#             best_neighbor = n
#     return best_neighbor
        
# def mutation_different_value_with_neighbors(children, pm_changing, pm_increase_probblity, pm_neighbors_amount, list_x, actual_y):
        
#         for child in children:
#             provement = True
#             flag_first_run = True

#             while(provement):
#                 all_neighbors = make_neighbors_for_mutation(child, pm_changing, pm_increase_probblity, pm_neighbors_amount, list_x, actual_y)
#                 best_neighbor = finding_best_neighbor(all_neighbors)
#                 if(best_neighbor.mse<child.mse):
#                     print(f"imporoved!, child = {child.mse}, imporoved = {best_neighbor.mse}")
#                     child = best_neighbor
#                     flag_first_run = False
#                 else:
#                     provement = False
#                     if(flag_first_run):
#                         child = best_neighbor
    

# def mutation_different_value_with_neighbors_singleChr(child, pm_changing, pm_increase_probblity, pm_neighbors_amount, list_x, actual_y):
        
#     provement = True
#     # flag_first_run = True

#     while(provement):
#         all_neighbors = make_neighbors(child, pm_changing, pm_increase_probblity, pm_neighbors_amount, list_x, actual_y)
#         best_neighbor = finding_best_child(all_neighbors)
#         if(best_neighbor.mse<child.mse):
#             print(f"imporoved!, child = {child.mse}, imporoved = {best_neighbor.mse}")
#             child = copy.deepcopy(best_neighbor)            
#             # flag_first_run = False
#         else:
#             provement = False
#             # if(flag_first_run):
#             #     child = best_neighbor

