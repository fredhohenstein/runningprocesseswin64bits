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


c = wmi.WMI()
for s in c.Win32_Service(StartMode="Auto", State="Stopped"):
    if raw_input("Restart %s? " % s.Caption).upper() == "Y":
        s.StartService()

print("Sleeping for 2 seconds")
time.sleep(5)
