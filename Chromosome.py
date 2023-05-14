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

        return my_chr                

def find_best_mse(chr_list):
    # in this function we take a list of choromosomes and we find the best one in them (based on mse)
    sum_mse = 0
    best_mse = float('inf')
    best_chr = None
    for c in chr_list:
        sum_mse += c.mse
        if (c.mse<best_mse):
            best_mse = c.mse
            best_chr = c

    return sum_mse/len(chr_list), best_mse, best_chr

def all_chromosoms(population_size, X, Y):
    # making a list of all random chromosoms (generation 0)
    # and also calculating the mse of them and set it 

    chromosoms = []
    for i in range(population_size):
        chr = Chromosome()
        chr._fit()
        # print(chr.chr)
        chromosoms.append(chr)
    all_mse(chromosoms, X, Y)

    return chromosoms
    
def all_mse(chr_list, list_x, actual_y):
    # in this function we take a list of choromosomes and x and y and
    # for each chromosome we are setting its mse
    
    for c in chr_list:
        c.mse = _mse(c, list_x, actual_y)

def _mse(single_chr, list_x, actual_y):
    # in this function we take a single choromosome and we calculate the predicted_y of it,
    # and we calulate its mse, and return it
        
    predicted_y = calculator(list_x, single_chr)
    mse = mean_squared_error(actual_y, predicted_y)     
    return mse

def binatodeci(binary):
    # here we take a binary list and we return its decimal
    
    return sum(val*(2**idx) for idx, val in enumerate(reversed(binary)))

def calculator(list_x, chr):
    # in this function we take a single choromosome and the list of x,
    # and we calculate the predicted_y list and return it
    # and after each time calculating power and coeff we also make the string of them and set it to our choromosome
    
    # list of tuples (coeff, power)
    list_c_p = []
    str = ''
    each_term = chr.coeff_size + chr.power_size
    
    for term in range(chr.term_size):
        coeff = []
        co_spot = each_term*term
        for i in range(co_spot, co_spot+chr.coeff_size):
            coeff.append(chr.chr[i])
        coeff_num = (binatodeci(coeff)/10) - 50.4
            
        p_spot = co_spot+chr.coeff_size
        power = []
        for j in range(p_spot, p_spot+chr.power_size):
            power.append(chr.chr[j])
        power_num = (binatodeci(power)*0.25) - 4
        
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
    # in here we take a coeff and power decimal and return the string show of it
    
    str = ''
    if(coeff_num==0):
        return str
    elif(coeff_num>0):
        str += f'+({coeff_num}'
    else:
        coeff_num *= (-1)
        str += f'-({coeff_num}'
    
    if(power_num==0):
        str+=')'
        return str
    elif(power_num>0):
        str += f'x^{power_num})'
    else:
        str += f'x^{power_num})'
    
    return str