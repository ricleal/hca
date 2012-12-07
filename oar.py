
import sys
import os
from string import Template
import subprocess as sub
import os.path
import inspect


class Oar :
    """
    Creates a condor job and can launch it
    
    oarRunFolder is mandatory!
    
    """
    
    def __init__(self,oarRunFolder) :
        self.oarRunFolder = oarRunFolder
        print 'OAR: oarRunFolder:',oarRunFolder
    
    def createJob(self, executable ):
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
        
        completePath = os.path.join(self.oarRunFolder,"job.oar.sh")
        outp = open(completePath, 'w')
        outp.write(s)
        outp.close()
        
        os.system('chmod +x ' + completePath)
        print "OAR: created job file: ", completePath
        return completePath
    
    def launchJob(self, jobFile,jobName):
        """ 
        Launches the jobfile

        """  
        currentFolder =  os.getcwd()
        os.chdir(self.oarRunFolder)
        launchFolder = os.getcwd()
        
        print "OAR: Launching job in: " + launchFolder
        
        jobFilePath = os.path.join(launchFolder, os.path.basename(jobFile))
        
        if os.path.isfile(jobFilePath) :
            
            command = "/usr/bin/oarsub  --stdout=job.oar.out --stderr=job.oar.err --name=" \
                + jobName + " -l nodes=1/core=4,walltime=00:30:00 " + jobFilePath
            print command
            
            print "Launching job: " + command + " in " + self.oarRunFolder
            # execute command and get output
            p = sub.Popen(command,stdout=sub.PIPE,stderr=sub.PIPE,shell=True)
            output, errors = p.communicate()
            if output is not None and len(output)>0 :
                print(output)
            if errors is not None and len(errors)>0 :
                print("Error Launching JOB: " + command)
                print(errors)
            
        else :
            print "job.oar.sh does not exist in " + self.oarRunFolder + ". Have you created the job file?"
        os.chdir(currentFolder)
    

        
    
    
    