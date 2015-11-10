'''
Created on Nov 7, 2015

@author: jj1745
'''
import numpy as np

class instrument(object):
    '''
    Create the object of an investment instrument
    the instrument is determined by how many shares the investor holds. 
    the value of each investment is then computed accordingly
    '''
    
    def __init__(self, num_shares):
        '''
        Constructor
        '''
        self.num_shares = num_shares #number of shares to buy
        self.position_value = 1000 / self.num_shares #the value of each investment
        
    def generateOneDay(self):
        '''
        simulate the outcome of one day of investment
        '''
        cumu_ret = 0
        for s in range(self.num_shares):
            r = np.random.rand()
            if r <= 0.51:
                cumu_ret = cumu_ret + 2 * self.position_value #if the coin is head, then my position value doubles 
            
        return cumu_ret
                    