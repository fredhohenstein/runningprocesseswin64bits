import time, sys, random
from time import sleep
import os  
import shutil
import wmi

print("Running proceeses ona Win64bit OS!")
with open("d:\\runpyprograms\\helloworld\\version", "r") as f:
    shutil.copyfileobj(f, sys.stdout)

c = wmi.WMI ()
for process in c.Win32_Process ():
  print (process.ProcessId, process.Name)

print("Sleeping for 2 seconds")
time.sleep(5)
