# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from numpy import array

max_iterations = 10

with open('C:/AI2/input.txt', 'r') as f:
   l = [[int(num) for num in line.split(',')] for line in f]
   number_of_neurons = len(l[0])
   num_of_vectors = len(l) 
   a = array(l)
   print(a)


def change_zero_values(l):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] == 0:
                l[i][j] = -1
    return l

def change_zero_values_ch(l):
    for i in range(len(l)):
            if l[i] == 0:
                l[i] = -1
    return l

def weights_of_matrices(l, num, number_of_neurons):
    W = np.zeros((number_of_neurons, number_of_neurons))
    for i in range(number_of_neurons):
        for j in range(number_of_neurons):
            if i == j:
                W[i, j] = 0
            else:
                w = 0
        
                for n in range(number_of_neurons-1):
                    w += l[n][i] * l[n][j]
            
                W[i, j] = w / num
                W[j, i] = W[i, j]
    W.tolist()
    print(W)
    return W  

def calc_llt(l,num):
    l = change_zero_values(l) 
   # print (l)
    result = (np.dot(np.asarray(l).T,np.asarray(l))/num)
    #result.tolist()
    remove_vals = np.multiply(result,np.identity(len(result)))
    result = result - remove_vals
    result = result.tolist()
    return result

def tresholding(l):
    for i in range(len(l)):
            if l[i] >= 0:
                l[i] = 1
            else:
                l[i] = -1
    return l
                 
def check_stability(l3, l, tr_vec, num_inp, num_of_vectors):
    #check_vector = []
    result = ""
    #l = array(l)
    l = change_zero_values(l)
    tr_vec = change_zero_values(tr_vec)
    '''
    for i in range(num_of_vectors):
        check_vector = (np.dot(np.asarray(l[i]).T, np.asarray(l3)))
        check_vector = check_vector.tolist()
        check_vector = tresholding(check_vector)
        #p = l[i]
    '''
    
    for i in range(num_inp):
        check_vector = (np.dot(np.asarray(l[i]).T, np.asarray(l3)))
        check_vector = check_vector.tolist()
        check_vector = tresholding(check_vector)
        print(check_vector)
        found_solution = False
        for j in range(max_iterations):
            for k in range(num_of_vectors):
                if (check_vector == tr_vec[k] and not found_solution):
                    result+=str(check_vector) + " is stable. " + "\n"
                    j=max_iterations
                    found_solution= True
                    break
                else:
                    check_vector = change_zero_values_ch(check_vector)
                    check_vector = (np.dot(np.asarray(check_vector).T, np.asarray(l3)))
                    check_vector = check_vector.tolist()
                    check_vector = tresholding(check_vector)
                    ''' if (check_vector == tr_vec[k]):
                        result+=str(check_vector) + " is stable. " + "\n"
                        break
                    else:
                        if (j == 9):
                            result+=str(check_vector) + " is unstable. " + "\n"
                            continue     '''
        if(not found_solution):
            result+=str(check_vector) + " is unstable. " + "\n"
    return result

#l2 = change_zero_values(a)

#print (l2)

l3 = calc_llt(a, num_of_vectors)

print (l3)
                
ch_output = check_stability(l3, l, l, num_of_vectors, num_of_vectors) 

print(ch_output)  

#print(l)      

f= open("C:\\AI2\\output.txt","w+")
for row in ch_output:
    f.write(str(row))
f.close() 
       

