import random as rnd
from sklearn.metrics import mean_squared_error


class Chromosome:
    
    def __init__(self):
        self.chr = None
        self.mse = None
        self.coeff_size = 10
        self.power_size = 5
        self.term_size = 9

        
    def _fit(self):
        self.chr = self._create(self.coeff_size, self.power_size, self.term_size)
        
    def _create(self, coefficient_size, power_size, term_size):
        my_chr = []
        
        for t in range(term_size):
            for i in range(coefficient_size):
                x = rnd.randint(0, 1)
                my_chr.append(x)
                
            for j in range(power_size):
                y = rnd.randint(0, 1)
                my_chr.append(y)

        self.chr = my_chr                
        

def all_chromosoms(amount):
    # making a list of all random chromosoms (generation 0)

    chromosoms = []
    for i in range(amount):
        chr = Chromosome()
        chromosoms.append(chr)
    return chromosoms




def _mse(chr_list, X, actual_Y):
    # calculating the average-mae and best-mae for all of our trees and given inputs and outputs
    
    # i = 1
    # mae_sum = 0
    # best_mae = float('inf')
    # best_tree = None
    for c in chr_list:
        # c.mae = mean_squared_error(c, X, Y)
        predicted_Y = calculator(X, c)
        c.mse = mean_squared_error(actual_Y, predicted_Y)
        
        # mae_sum += t.mae
        # if (t.mae<best_mae):
        #     best_mae = t.mae
        #     best_tree = t
        # # print(f"tree number {i} = {t.in_order} and its mae is = {t.mae}")
        # i += 1

    # return mae_sum/i, best_mae, best_tree

def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

def calculator(list_x, chr):
    # term = 0
    each_term = chr.coeff + chr.power
    
    
    for term in range(chr.term_size):
        coeff = []
        co_spot = each_term*term
        for i in range(co_spot, co_spot+chr.coeff_size):
            coeff.append(chr.chr[i])
        p_spot = co_spot+chr.coeff_size
        power = []
        for j in range(p_spot, p_spot+chr.power_size):
            power
            
            
        
    





def to_math_string(node):
    if(node.is_leaf):
        if(node.operator!='x'):
            a = format(float(node.operator), ".2f")
            return f"{a}"
        else:
            return f"{node.operator}"
    else:
        if(len(node.children)) == 1:
            return f"{node.operator}{to_math_string(node.children[0])}"
        else:
            return f"{to_math_string(node.children[0])}{node.operator}{to_math_string(node.children[1])}"

        
def calculator(root, x, flag):
    # doing the calculating for each function that we have made with given input
    
    if(flag):
        return
    
    if(root.is_leaf):
        if(root.operator == 'x'): 
            return x
        else: 
            return root.operator
    else:
        
        left_val = calculator(root.children[0], x, flag)
        right_val = calculator(root.children[1], x, flag)

        if (root.operator == '+'):
            return left_val + right_val
        elif (root.operator == '-'):
            return left_val - right_val
        elif (root.operator == '*'):
            return left_val * right_val
        elif (root.operator == '**'):
            if(left_val==0 and right_val<0):
                flag = True
                return 1
            else:
                try:
                    return left_val**right_val
                except:
                    flag = True
                    return 1
        
def mean_abs_error(actual_y, predicted_y):
    amount = len(predicted_y)
    sum = 0
    for i in range(amount):
        sum += abs(predicted_y[i]-actual_y[i])
    return sum/amount
        
def _mae(tree, list_x, list_y):
    # calculating each tree mae with given inputs and outputs
    #here mae is our fitness
    
    trees_y = []
    for single_x in list_x:
        flag = False
        t_y = calculator(tree.root, single_x, flag)
        if(flag==True or math.isnan(t_y) or t_y>100000 or t_y<-100000):
            t_y = 100000

        trees_y.append(t_y)

    mae = mean_abs_error(list_y, trees_y)
    return mae

def calculating_mae(tree_list, X, Y):
    # calculating the average-mae and best-mae for all of our trees and given inputs and outputs
    
    i = 1
    mae_sum = 0
    best_mae = float('inf')
    best_tree = None
    for t in tree_list:
        t.mae = _mae(t, X, Y)
        mae_sum += t.mae
        if (t.mae<best_mae):
            best_mae = t.mae
            best_tree = t
        # print(f"tree number {i} = {t.in_order} and its mae is = {t.mae}")
        i += 1

    return mae_sum/i, best_mae, best_tree
    