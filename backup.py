import sys
import os
import shutil
import datetime
n=len(sys.argv)
print(n)
if(n==3):
    sourcePath=sys.argv[1]
    destinationPath=sys.argv[2]
    print(sourcePath)
    print(destinationPath)
    if(os.path.exists(sourcePath) and os.path.exists(destinationPath)): #returns true for both file and directory if they exists. If not, returns false
        #check if its a directory only and not a file
        if((not os.path.isfile(sourcePath))and(not os.path.isfile(destinationPath))):   #returns true if its only a file and false if its a directory
           files_in_dir = os.listdir(sourcePath)  
           print("Files and directories in source directory :")
            # prints all files
           print(files_in_dir)
           for file in files_in_dir:
                mod_sourcePath=sourcePath+'\\'+file
                mod_destinationPath=destinationPath+'\\'+file
                if(os.path.isfile(mod_sourcePath)):
                    if(os.path.exists(mod_destinationPath)):
                        tempArray=mod_destinationPath.split(".")
                        ts=str(datetime.datetime.now().timestamp())
                        ts=ts.split('.')
                        ts=ts[0]
                        mod_destinationPath= tempArray[0]+'_'+ts+'.'+tempArray[1]
                        # print(destinationPath)

                    shutil.copy(mod_sourcePath, mod_destinationPath)
                    print("copied file "+mod_sourcePath+"--to--"+mod_destinationPath)
                else: #if its a directory
                    #  print("Its a directory-skip")
                    if not os.path.exists( mod_destinationPath):
                        os.makedirs(mod_destinationPath) 
                    os.system('python backup.py'+' '+mod_sourcePath+' '+ mod_destinationPath)


        else: 
            print("Either source or directory is not a directory,please enter correct paths of the directory")         
        


    else:
        print("Either source or destination does not exist,please enter correct paths of the directory")

else:
    print("Wrong number of arguments.Please call this program with 2 commandline  arguments 1. path to source directory 2.path to destination directory")