'''
Created on Dec 7, 2012

@author: leal


TODO:

This will be the future Executor for MPI, multithreading or OAR

'''

import subprocess as sub
import sys
import os

# local
import config
import log
logger = log.setupLogger('exec')

def getClass( className, argsToConstructor=None ):
    '''
    returns a class instance given a name
    :param className : class name 
    :type className : str
    
    '''
    if argsToConstructor is None:
        return globals()[className]()    
    else:
        return globals()[className](argsToConstructor)


class Execution:
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        logger.debug("Execution init....")
    
    @staticmethod
    def run(command) :
        p = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
        output, errors = p.communicate()
        if errors is not None and len(errors) > 0 :
            sys.stderr.write(errors)
        return p.pid, output
    
    @staticmethod
    def checkIfPidExists(pid):        
        """ 
        Check For the existence of a unix pid. 
        Sending signal 0 to a pid will raise an OSError exception if the 
        pid is not running, and do nothing otherwise.
        """
        try:
            os.kill(pid, 0)
        except OSError:
            return False
        else:
            return True
    
    # Methods to be implemented by the children classes:
    def init(self):
        """ """
        pass
    
    def execute(self):
        """ """
        pass

    def wait(self):
        """ """
        pass

    def finish(self):
        """ """
        pass


class SerialExecution(Execution):
    '''
    ParallelExecution
    
    '''

    def __init__(self):
        '''
        Constructor
        '''
        print "Constructor SerialExecution"
        pass
    
    def execute(self, command):
        '''
        Just sends the the command to be executed in a shell
        '''
        pass
        
    def wait(self):
        """
        Waits for all threads to complete their job
        """
        pass
    def finish(self):
        """ """
        pass        
    
    

class OarExecution(Execution):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass        


if __name__ == "__main__":
    
    # Serial
    serial = getClass('SerialExecution')
    
    pid,out = serial.run('sleep 1')
    print pid
    
    
