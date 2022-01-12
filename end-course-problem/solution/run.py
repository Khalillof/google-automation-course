#!/usr/bin/env python3
import os, requests, reports, emails, datetime

# list of dics
list_data=[]

def run():
  
  for file in os.listdir('./supplier-data/descriptions/'):
    with open('./supplier-data/descriptions/'+file) as fp:
        lines=fp.readlines()
        _data={'name':lines[0].strip(),'weight':int(lines[1].strip().split(' ')[0]),'description':lines[2].strip()}
        
        if _data['name'] == "Kiwifruit":
          _data['image_name']='	005.jpeg'
        elif _data['name'] == "Strawberry":
          _data['image_name']='	009.jpeg'
        elif _data['name'] == "Plum":
          _data['image_name']='icon.sheet.png'
        elif _data['name'] == "Watermelon":
          _data['image_name']='010.jpeg'
        elif _data['name'] == "Apple":
          _data['image_name']='001.jpeg'
        elif _data['name'] == "Avocado":
          _data['image_name']='002.jpeg'
        elif _data['name'] == "Grape":
          _data['image_name']='004.jpeg'
        elif _data['name'] == "Mango":
          _data['image_name']='007.jpeg'
        elif _data['name'] == "Lemon":
          _data['image_name']='006.jpeg'
        elif _data['name'] == "Blackberry":
          _data['image_name']='	003.jpeg'

       # add to list_data for later usage to generate reports
        list_data.append(_data)
        result=requests.post('http://35.232.76.104/fruits/',data=_data)
        #print(result.text,result.status_code)


# compine list of strings to string rows
def compin_strs(dic_list, new_line):
    compined_string = ''
    for dic in dic_list:
       compined_string += new_line + 'name: {}{}weight: {} lbs {}'.format(dic['name'] , new_line , str(dic['weight']), new_line) 
    return compined_string

def main():
  run() # this will upload data and update list_data 
  
  summary_linesR=compin_strs(list_data, '<br/>')
  summary_linesE=compin_strs(list_data, '\n')

  #print(summary)
  # TODO: turn this into a PDF report
  _title="Processed Update on {}".format(datetime.datetime.utcnow().strftime("%B %d, %Y"))
  reports.generate_report("/tmp/processed.pdf",_title,summary_linesR) 

  # TODO: send the PDF report as an email attachment
  _etitle="Upload Completed - Online Fruit Store"
  _body="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message=emails.generate_email("automation@example.com", "student-00-debcaf457eae@example.com", _etitle, _body, "/tmp/processed.pdf")
  emails.send_email(message)
if __name__ == "__main__":
    main()


    

        