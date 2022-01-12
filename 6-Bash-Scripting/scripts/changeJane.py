#!/usr/bin/env python3
import sys
import subprocess

def changeName(janefile):
  with open(janefile, mode='r',encoding='UTF-8') as file:
    for line in  file.readlines():
        line2 = line.strip().replace("jane","jdoe")  
        subprocess.run(["mv",line.rstrip('\n'),line2.rstrip('\n')])
    file.close()
  return 1


def main():
  print(changeName(sys.argv[1]))

  sys.exit(0)
if __name__ == "__main__":
  main()