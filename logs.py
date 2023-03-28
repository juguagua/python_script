# this script will search for all *.log file in the given directory,
# zip them using the program you specify 
# and then date stamp them

import os
from time import strftime

logsdir = "c:\puttylogs" # set the variable logsdir
zip_program = "zip.exe"

for files in os.listdir(logsdir):
    # check to ensure the files in the directory end in .log
    if files.endswith(".log"): 
        files1 = (
            files + "." + strftime("%Y-%m-%d") + ".zip"
        )
        os.chdir(logsdir) # change directory to the logsdir
        # zip the logs into dated zip files for each server
        os.system(
            zip_program + " " + files1 + " " + files
        )
        os.remove(files) # remove the original log files