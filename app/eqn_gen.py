import random
import operator
randomlist = []
longtermlist = []
ops = ['+', '-', '*', '/']

def math():
    for i in range(18000):
        n = random.randint(1,9)
        randomlist.append(n)
    n=9
    output=[randomlist[i:i + n] for i in range(0, len(randomlist), n)]
    output_2=[] #final output list of list with only integer values
    for i in range(0,2000): # 3240 / 9 = 360 - closest to the one year set value from multiple of 9
        each_list = output[i]
        operation1 = random.choice(ops)
        operation2 = random.choice(ops)
        each_list[2] = operation1
        each_list[5] = operation2
        each_list[8] = '='
        try:
            target=bidmas_calc(each_list)
        except ZeroDivisionError:
            pass
        if type(target)!=float:
            each_list.append(target)
            output_2.append(each_list)
        
    for i in output:
        if type(i[-1])==float:
            output.remove(i)
        else:
            pass
    return output_2

def bidmas_calc(input):
    equ = "".join(input)
    return eval(equ)
