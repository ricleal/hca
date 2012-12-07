'''
Created on Dec 7, 2012

@author: leal
'''

import subprocess as sub
import ConfigParser
import os
import logging
from multiprocessing.pool import ThreadPool

class Execution:
    '''
    classdocs
    '''


    def __init__(self,configFileName='hca.cfg'):
        '''
        Constructor
        '''
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open(configFileName))
    
    def run(self,command) :
        '''
        Run a command in the shell
        @return: None if Error, otherwise the output
        '''
        p = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
        output, errors = p.communicate()
        if errors is not None and len(errors) > 0 :
            logging.error(errors)
            return None
        else :
            return output

class ParallelExecution(Execution):
    '''
    ParallelExecution
    
    '''


    def __init__(self,configFileName='hca.cfg'):
        '''
        Constructor
        Creates a pool of threads
        '''
        Execution.__init__(self,configFileName)
        nCores = self.config.getint('Common', 'cores')
        self.threadPool = ThreadPool(nCores)
        self.threadList = []
    
    def execute(self, command):
        '''
        Just sends the the command to be executed in a shell
        '''
        t = self.threadPool.Process(target=self.run, args=(command,))
        t.start()
        self.threadList.append(t)
    
    def wait(self):
        """
        Waits for all threads to complete their job
        """
        # Start all threads
        [t.join() for t in self.threadList]
        del self.threadList[:]
        
        
    
    

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
    from datetime import datetime
    
    p = ParallelExecution()
    t_start = datetime.now()
    
    for i in range(8):
        p.execute('python ~/workspace/PyTests/src/speedTest.py')
    p.wait()
    t_end = datetime.now()
    t_total = t_end - t_start
    
    print "Total time: ", t_total
    print "Main has finished!"
