import random as rnd
from sklearn.metrics import mean_squared_error

class Chromosome:
    
    def __init__(self):
        self.chr = None
        self.mse = None
        self.coeff_size = 10
        self.power_size = 5
        self.term_size = 9
        self.str = None

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

def all_chromosoms(population_size):
    # making a list of all random chromosoms (generation 0)

    chromosoms = []
    for i in range(population_size):
        chr = Chromosome()
        chromosoms.append(chr)
    return chromosoms

def _mse(chr_list, X, actual_Y):
    # calculating the average-mae and best-mae for all of our trees and given inputs and outputs
    
    sum_mse = 0
    best_mse = float('inf')
    best_chr = None
    for c in chr_list:
        predicted_Y = calculator(X, c)
        c.mse = mean_squared_error(actual_Y, predicted_Y)        
        sum_mse += c.mse
        if (c.mse<best_mse):
            best_mse = c.mse
            best_chr = c

    return sum_mse/len(chr_list), best_mse, best_chr

def binatodeci(binary):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

def calculator(list_x, chr):
    # list of tuples (coeff, power)
    list_c_p = []
    str = None
    each_term = chr.coeff + chr.power
    
    for term in range(chr.term_size):
        coeff = []
        co_spot = each_term*term
        for i in range(co_spot, co_spot+chr.coeff_size):
            coeff.append(chr.chr[i])
        coeff_num = binatodeci(coeff)
            
        p_spot = co_spot+chr.coeff_size
        power = []
        for j in range(p_spot, p_spot+chr.power_size):
            power.append(chr.chr[j])
        power_num = binatodeci(power)
        
        list_c_p.append((coeff_num, power_num))
        str += to_string(coeff_num, power_num)
    
    chr.str = str

    predicted_y = []

    for x in list_x:
        y = 0
        for l in list_c_p:
            y += (l[0] * (x**l[1]))

        predicted_y.append(y)
        
    return predicted_y


def to_string(coeff_num, power_num):
    str = ''
    if(coeff_num==0):
        return str
    elif(coeff_num>0):
        str += f'+({coeff_num}'
    else:
        coeff_num *= (-1)
        str += '-({coeff_num}'
    
    if(power_num==0):
        str+=')'
        return str
    elif(power_num>0):
        str += f'x^{coeff_num}'
    else:
        str += 'x^{coeff_num})'
    
    return str