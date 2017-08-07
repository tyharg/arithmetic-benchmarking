import time
import random
#import numpy as np


#Settings
#N = length of vectors
    #vector_pairs = number of dot products to take
N = 50000
vector_pairs = 100

#dot_product(list, list):
#   takes two lists (vectors) as arguments
#   fills list from 0 to N 
#   returns dot product using iterators
def benchmark(h, k):
    for i in range(N):
        h.append(random.randint(0,1000000))
        k.append(random.randint(0,1000000))
    #print("numpy result: ", np.dot(h,k))
    return sum(vec[0] * vec[1] for vec in zip(h, k)) #return dot product


#main():
#   initialize data structure
#   load concurrent.futures.ProcessPoolExecutor()
#       map method and data structure to executor
#       launch executors
#       print out dot products
#       print time
def main():

    #init data
    data1, data2 = [], []
    for i in range(vector_pairs): data1.append([]); data2.append([])

    #load executor
    start_time = time.time()
    
    for i in range(vector_pairs):
        print(benchmark(data1[i], data2[i]))
    
    print("--- %s seconds ---" % (time.time() - start_time))



### Init Main ###
if __name__ == '__main__':
    main()
 
 
 
 
### Results ###
#


 
 
 
 
 
 
 
 
 