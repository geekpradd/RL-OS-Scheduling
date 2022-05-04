import random 
import argparse 

# ap = argparse.ArgumentParser()
# ap.add_argument("-n", "--NUM", default=100, type=int)
# ap.add_argument("-st", "--STD_TIME", default=30, type=float)
# ap.add_argument("-sb", "--STD_BURST", default=20, type=float)

# args = ap.parse_args()
import numpy 

def get_testcase(n, q, std_time=30, std_burst=20):
    tc = []
    quantums = [8*i for i in range(1, q+1)]

    for i in range(n):
        t = numpy.random.randn()*std_time
        b = numpy.random.randn()*std_burst
        tc.append((t, b))
    
    return tc, quantums
    


    