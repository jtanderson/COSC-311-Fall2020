import numpy as np
import numpy.linalg as la

class kNNModel:
    """ Take an n-by-d matrix of samples in dimension d """
    def __init__(self, train_x):
        # will have n samples in dimension d
        # i.e. an n-by-d matrix
        self.training_data = train_x
        
    """ Calcuates all distances of training_data to test_x (a 1-by-d np array ) """
    def distances(self, test_x):
        # np.sqrt(np.sum((points - test_x)**2,axis=1))
        # [la.norm(a - test_x) for a in points]
        return la.norm(self.training_data - test_x, axis=1)
    
    # TODO: write prediction routine