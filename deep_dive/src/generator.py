'''
   ______                           __            
  / ____/__  ____  ___  _________ _/ /_____  _____
 / / __/ _ \/ __ \/ _ \/ ___/ __ `/ __/ __ \/ ___/
/ /_/ /  __/ / / /  __/ /  / /_/ / /_/ /_/ / /    
\____/\___/_/ /_/\___/_/   \__,_/\__/\____/_/     
                       

'''

import numpy as np
from random import random


# Generates a dataset pair, consisting of two input values in [0, 1) and the corresponding groundtruth 
def generate_data_pair(a=0.5, b=0.5):
    """
    Please keep in mind that numpy's random generator is NOT suitable for
    cryptography or highly-sensitive scientific simulations.
    numpy uses PCG-64 pseudo-random generator internally, more info here:
    https://www.pcg-random.org/
    """
    x1 = np.random.randint(10)
    x2 = np.random.randint(10)
    
    y = np.square(a*x1 + b*x2)
    
    return x1, x2, y


# Copyright and contact: Mark.schutera@mailbox.org

