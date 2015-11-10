'''
Created on Nov 7, 2015

@author: jj1745
'''

import sys
from simulation import writeResult, plotResult

class InvalidNumTrialsException(Exception):
    '''exception of invalid num_trials input'''
    def __str__(self):
        return 'Your input of num_trials is not valid'
    
class NonPositiveException(Exception):
    def __str__(self):
        return 'Your input is not a positive integer'

class InvalidPositionsException(Exception):
    '''exception of invalid positions input'''
    def __str__(self):
        return 'Your input of positions is not valid'
    
def getTrials(input):
    '''
    covert user input into a integer for num_trials
    '''
    if input.isdigit():
        n = int(input)
        if n <= 0:
            raise NonPositiveException() #input must be a positive integer
        else:
            return n
    else:
        raise InvalidNumTrialsException()
    
def checkPositions(input_list):
    '''
    check if the entered positions is correct
    it can only be [1,10,100,1000] (no whitespace)
    '''
    if input_list == '[1,10,100,1000]':
        return True
    else:
        raise InvalidPositionsException() 
    
def getPositions(input_list):
    '''
    given that the input_list is valid: [1,10,100,1000],
    convert it into a list of integers     
    '''
    output = []
    stripped = input_list[1:-1]
    value_list = stripped.split(',')
    for v in value_list:
        output.append(int(v)) #output a list of integers
    
    return output            

def obtainPositionsFromUser():
    '''
    Ask inputs from user for a list of positions
    The user must enter [1,10,100,1000]. Otherwise it will ask again
    '''
    try:
        text = raw_input('PLease enter a list of positions, e.g. [1,10,100,1000]. No whitespace allowed')       
        if checkPositions(text):
            return getPositions(text)
    except InvalidPositionsException:
        print 'Please enter a valid list of positions'
        obtainPositionsFromUser() #recursively call this function if user input is not valid
    except (EOFError, KeyboardInterrupt):
        sys.exit()
    
def obtainTrialsFromUser():
    '''
    Ask inputs from user for num_trials
    The user must enter a positive integer. Otherwise it will ask again
    '''
    try:
        text = raw_input('PLease enter the number of trials. It should be a positive integer')       
        return getTrials(text)
    except InvalidNumTrialsException:
        print 'Please enter a valid number'
        obtainTrialsFromUser() #call the function recursively if input is not valid
    except NonPositiveException:
        print 'Please enter a positive integer'
        obtainTrialsFromUser()
    except (EOFError, KeyboardInterrupt):
        sys.exit()
           
if __name__ == '__main__':
    
    positions = obtainPositionsFromUser()
    num_trials = obtainTrialsFromUser()
    writeResult(positions, num_trials)
    plotResult(positions,num_trials)
    print 'Your simulation results have been saved. Thanks!'
    
    
            
