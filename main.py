#    numerical python
import numpy as np

#    random sample generation
from generate_data import generate_data

#    visualization
from visualize import visualize

def main():
    #    number of measurements
    N = 1000
    
    #    means of random sample
    m = np.zeros(N)

    #    sigmas
    s = np.ones(N)
    
    #    generate random data
    R = generate_data(m, s, 3)
    
    print(R)
    
    visualize(R)
    
 
    
if __name__ == "__main__":
    main()