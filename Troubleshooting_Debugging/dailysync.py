#!/usr/bin/env python
from multiprocessing import Pool
import subprocess
import os

tasks=[]
src = "./data/prod/"
dest = "./data/prod_backup/"

def tasker(_src):
   print("runing tasks :"+ _src)
   subprocess.call(["rsync", "-arq", _src, dest])
   
def run():

   for root, dirs,files in os.walk(src):
      for dir in dirs:
         tasks.append(os.path.join(root,dir))
   # Create a pool of specific number of CPUs
   p = Pool(len(tasks))
   # Start each task within the pool
   p.map(tasker, tasks)
   print("done with tasks")

if __name__ == "__main__":
   run()


