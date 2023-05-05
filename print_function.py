import matplotlib.pyplot as plt
import Chromosome


def result(chr, list_x):    
    chrs_y = []
    for single_x in list_x:
        flag = False
        c_y = Chromosome.calculator(list_x, chr)
        chrs_y.append(c_y)
    return chrs_y

def print_func(list_x, actual_y, predicted_chromosome, actual_function, predicted_function, photo_number):

    predicted_y = result(predicted_chromosome, list_x)

    fig, ax = plt.subplots()
    actual_function, = plt.plot(list_x, actual_y, label='actual function')
    predicted_function, = plt.plot(list_x, predicted_y, label='predicted function')

    ax.set_title(f"actual function: {actual_function}, predicted function: {predicted_function}")
    ax.legend(handles=[actual_function, predicted_function])
    name = f"exact_function_{photo_number}_" + '.png'

    plt.savefig(name)
    plt.show()
    
    print()