#!/usr/bin/env python3
import os
import requests

def update_feedback():
  
  for file in os.listdir('/data/feedback'):
    with open('/data/feedback/'+file) as fp:
        lines=fp.readlines()
        result=requests.post('http://35.222.85.88/feedback/',data={'title':lines[0].strip(),'name':lines[1].strip(),'date':lines[2].strip(),'feedback':lines[3].strip()})
        print(result.text,result.status_code)
  #result=requests.post('http://34.69.138.82/feedback',data=temlist)
  #return result.status_code == 201:

  #print(result.text)
  #return result.status_code

if __name__ == "__main__":
    update_feedback()


    

        