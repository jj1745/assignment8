'''
Created on Nov 9, 2015

@author: jj1745
'''
'''
This module lets us create each invetment instrument with positions set by input list. It then
runs the simulation with given num_trials, and finally writes and plots results
'''

from investment import instrument
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(100) #set a seed so that the results do not change. Just for checking purpose

def simulateTrials(ins, num_trials):
    '''
    given a type of investment instrument, simulate for multiple times
    output a list of daily returns
    '''
    daily_ret = []
    for trial in range(num_trials):
        value = ins.generateOneDay()
        value = value / 1000.0 - 1
        daily_ret.append(value)
    
    return daily_ret
        
def writeResult(positions, num_trials):
    '''
    write the simulation results into a results.txt file
    '''
    file = open('results.txt','w')
    for p in positions:
        ins = instrument(p) #create an investment instrument of type p
        daily_ret = np.array(simulateTrials(ins, num_trials)) #get daily return
        mean = np.mean(daily_ret)
        sd = np.std(daily_ret)
        str_out = 'For position = %d, mean = %f, standard deviation = %f' %(p, mean, sd)
        file.write(str_out)
        file.write('\n') 
        
    file.close()
    
def plotResult(positions, num_trials):
    '''
    plot the simulation results and save to 4 different pdf files
    '''
    for p in positions:
        ins = instrument(p) #create an investment instrument of type p
        daily_ret = np.array(simulateTrials(ins, num_trials)) #get daily return
        fig = plt.figure()
        plt.hist(daily_ret, 100, range = [-1,1])
        plt.title('return for investing ' + str(p) + ' shares')
        plt.xlabel('daily return')
        plt.ylabel('frequency')
        file_name = 'histogram_' + str(p).zfill(4) + '_pos.pdf'
        fig.savefig(file_name)
        plt.clf()
        
    
