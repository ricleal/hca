'''
Created on Dec 7, 2012

@author: leal


TODO:

This will be the future Executor for MPI, multithreading or OAR

'''

import subprocess as sub
import sys
import os
import threading
from string import Template
import inspect
import time
import getpass

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


    def __init__(self,runFolder=None):
        '''
        Constructor
        '''
        logger.debug("Execution init....")
        self.initialDir = os.getcwd()
        if runFolder is not None:
            if os.path.isfile(runFolder):
                runFolder = os.path.abspath(runFolder)
                runFolder = os.path.dirname(runFolder)
            logger.info("Changing to folder: " + runFolder)
            os.chdir(runFolder)
            self.runFolder = runFolder
        self.sub_init()
            
    
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
    def sub_init(self):
        """ """
        pass
    
    def sub_finish(self):
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
        os.chdir(self.initialDir)
        self.sub_finish()


class SerialExecution(Execution):
    '''
    SerialExecution
    
    '''

    def sub_init(self):
        '''
        Constructor
        '''
        logger.debug("Constructor SerialExecution...")
        pass
    
    def execute(self, command):
        '''
        Just sends the the command to be executed in a shell
        '''
        logger.info("Starting 1 thread with the command: " + command)
        self.t = threading.Thread(target=self.run, args=(command,))
        self.t.start()
        
    def wait(self):
        """
        Waits for all threads to complete their job
        """
        timeout = int(config.Config().getPar("Common","execution_timeout"))
        logger.info("Waiting for the command to finish. Timeout = %d "%timeout)
        self.t.join(timeout)
        
        
    def sub_finish(self):
        """ """
        logger.info("Finished...")        
        
    

class OarExecution(Execution):
    '''
    OarExecution
    
    '''

    def sub_init(self):
        '''
        Constructor
        '''
        logger.debug("Constructor OarExecution...")
        self.oarJobName = 'HClusterA'
    
    def __createJob(self, executable ):
        """
        Fills in the template job with the job name and saves it in 
        the oar run folder
        
        executable : normally XDS
        
        secondExecutable : followed by best
        
        
        return complete job path
        
        """
        thisfileFolderPath = os.path.dirname(inspect.getfile( inspect.currentframe() ))
        inp = open( os.path.join(thisfileFolderPath,"job.oar.tpl"), 'r')
        t = Template(inp.read())
        
        s = t.substitute(executable=executable)
        
        completePath = os.path.join(self.runFolder,"job.oar.sh")
        outp = open(completePath, 'w')
        outp.write(s)
        outp.close()
        
        os.system('chmod +x ' + completePath)
        print "OAR: created job file: ", completePath
        return completePath
    
    def __launchJob(self, jobFile,jobName):
        """ 
        Launches the jobfile

        """  
        launchFolder = self.runFolder
        
        print "OAR: Launching job in: " + launchFolder
        
        jobFilePath = os.path.join(launchFolder, os.path.basename(jobFile))
        
        if os.path.isfile(jobFilePath) :
            
            command = "/usr/bin/oarsub  --stdout=job.oar.out --stderr=job.oar.err --name=" \
                + jobName + " -l nodes=1/core=4,walltime=00:30:00 " + jobFilePath
            
            
            logger.info("Launching job: " + command + " in " + launchFolder)
            # execute command and get output
            pid, output = self.run(command)
            if output is not None and len(output)>0 :
                logger.info(output)
            
        else :
            logger.warning("job.oar.sh does not exist in " + launchFolder + ". Have you created the job file?")


    def execute(self, command):
        '''
        Just sends the the command to be executed in a shell
        '''
        jobFilePath = self.__createJob(command)
        self.__launchJob(jobFilePath,self.oarJobName)
        
        
    def wait(self):
        """
        Waits for all threads to complete their job
        """
        command = '/usr/bin/oarstat  -u ' + getpass.getuser() + " | grep " + self.oarJobName
        pid,output = self.run(command)
        while output is not None and len(output)>0 :
            self.sendTextMessage(output.strip())
            output="Sleeping for 10 seconds: Waiting for the jobs to stop..."
            #self.emit(QtCore.SIGNAL("output(QString)"),QtCore.QString(output))
            self.sendTextMessage(output.strip())
            time.sleep(10)
            pid,output = self.run(command)
        #self.emit(QtCore.SIGNAL("output(QString)"),QtCore.QString("OAR Job(s) finished"))
        
        
        
    def sub_finish(self):
        """ """
        logger.info("Finished...")        


if __name__ == "__main__":
    
    # Serial
    serial = getClass('SerialExecution')
    pid,out = serial.run('sleep 0')
    print pid
    
    serial = getClass('SerialExecution','.')
    serial.execute('sleep 1')
    serial.wait()
    serial.finish()
    
    oar = getClass('OarExecution','/tmp')
    oar.execute('sleep 1')
    oar.wait()
    oar.finish()
    
