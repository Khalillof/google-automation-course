#!/usr/bin/env python3
# chmod +x ticky_check.py
from collections import Counter
import re
import csv
import operator
import sys
import subprocess

errors_messages = {}
users_entries = {}


def grep_lunix(logfile, find_pattern, shell=False):

    result = None
    if shell:
        result = subprocess.run(["grep  {0} {1}".format(
            find_pattern, logfile)], shell=True, capture_output=True)
    else:
        result = subprocess.run(
            ["grep", find_pattern, logfile], capture_output=True)
    # check output
    if result.returncode == 0:
        return result.stdout
    else:
        return result.stderr


def logs_search(log_file, error_pattern):
    # error = input("What is the error? ")
    returned_errors = []

    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log_line in file.readlines():
            if re.search(r"{}".format(error_pattern), log_line):
                returned_errors.append(log_line)
        file.close()
    return returned_errors

# gen_report('< data >', "<..output_url..>")
def gen_report(data_opj, output_url):
    # with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    with open(output_url, 'w') as file:
        for d in data_opj:
            file.write(d)
        file.close()


def error_toCsv(report_url, group_lists, lables):
    try:
        with open(report_url, 'w+', newline="") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=lables)
            writer.writeheader()
            for k, v in sorted(group_lists.items(), key=operator.itemgetter(1), reverse=True):
                writer.writerow({'Error': k, 'Count': v})
            output_file.close()
    except IOError:
        print("I/O error")


def nestedDics_toCsv(report_url, dic_data, labels):
    with open(report_url, 'w+', newline="") as _file:
        wr = csv.DictWriter(_file, fieldnames=labels)
        wr.writeheader()
        temDic = {}
        for k, v in sorted(dic_data.items()):
            for a, b in v.items():
                temDic.update({labels[0]: k, a: b})
            wr.writerow(temDic)
        _file.close()


# compine list of strings to string rows
def compin_strs(str_list):
    compined_string = ''
    for line in str_list:
        compined_string += line.strip() + '\n'
    return compined_string


# check text if contain some chars
def contain_chars(_text):
    if '[' or ']' or '(' or ')' in _text:
        return True
    else:
        return False

 # search text for symboles or chars
def search_text(left, right, _text):

    if left and right in _text:
        start = _text.find(left)
        end = _text.find(right)
        _cut = _text[start:end+1]
        return _text.replace(_cut, '').strip()
    else:
        return _text

# clean text from some chars
def clean_text_recusive(_text):
    if '[' and ']' in _text:
        return clean_text_recusive(search_text('[', ']', _text))
    elif '(' and ')' in _text:
        return clean_text_recusive(search_text('(', ')', _text))
    else:
        return _text.strip()

def process_rows(str_list):
    _dic = {}
    for line in str_list:
        line = line[41:]
        if contain_chars(_dic):
            line = clean_text_recusive(line)

        if line in _dic:
            _dic[line] += 1
        else:
            _dic[line] = 1
    return _dic


def sort_by_frequency(_list):
    # sorting on bais of frequency of elements
    return [item for items, c in Counter(_list).most_common() for item in [items] * c]


def users_update(str_lines, _name):
    """
    search for any line with text betwen (...)
    patterns=re.search(r"^.*\((.*)\).*$")
    example : "Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)
    """
    for _line in str_lines:
        _user = re.findall(r"^.*\((.*)\).*$", _line)[0]

        if _user not in users_entries:
            if _name == 'INFO':
                users_entries[_user] = {_name: 1, 'ERROR': 0}
            else:
                users_entries[_user] = {'INFO': 0, _name: 1}
        else:
            users_entries[_user][_name] += 1


def main():
    info = "INFO"
    _err = "ERROR"

    #log_file = sys.argv[1]
    log_file = "./syslog.log"

    #print(grep_lunix(log_file, info))

    # """
    _infos = logs_search(log_file, info)
    _errors = logs_search(log_file, _err)

    users_update(_infos, info)
    users_update(_errors, _err)

    # compine lists
    two_lists = _infos + _errors

    # output dictionaries to csv files
    error_toCsv("error_message.csv", process_rows(two_lists), ['Error', 'Count'])
    nestedDics_toCsv("user_statistics.csv", users_entries,['Username', info, _err])
    sys.exit(0)
    # """
    
if __name__ == "__main__":
    main()

"""
Generate reports
Now, we're going to practice creating a script, named ticky_check.py, that generates two different reports from this internal ticketing
system log file i.e., syslog.log. This script will create the following reports:

The ranking of errors generated by the system: A list of all the error messages logged and how many times each error was found,
sorted by the most common error to the least common error. This report doesn't take into account the users involved.
The user usage statistics for the service: A list of all users that have used the system, including how many info messages
and how many error messages they've generated. This report is sorted by username.
To create these reports write a python script named ticky_check.py. Use nano editor for this.

nano ticky_check.py
Copied!
Add the shebang line.

#!/usr/bin/env python3
Copied!
Here's your challenge: Write a script to generate two different reports based on the ranking of errors generated by the system
and the user usage statistics for the service. You'll write the script on your own, but we'll guide you throughout.

First, import all the Python modules that you'll use in this Python script. After importing the necessary modules,
initialize two dictionaries: one for the number of different error messages and another to count the number of entries for each user
(splitting between INFO and ERROR).

Now, parse through each log entry in the syslog.log file by iterating over the file.

For each log entry, you'll have to first check if it matches the INFO or ERROR message formats. You should use regular expressions
for this. When you get a successful match, add one to the corresponding value in the per_user dictionary. If you get an ERROR message,
add one to the corresponding entry in the error dictionary by using proper data structure.

After you've processed the log entries from the syslog.log file, you need to sort both the per_user and error dictionary before
creating CSV report files.

Keep in mind that:

The error dictionary should be sorted by the number of errors from most common to least common.
The user dictionary should be sorted by username.
Insert column names as ("Error", "Count") at the zero index position of the sorted error dictionary. And insert column names as ("Username", "INFO", "ERROR") at the zero index position of the sorted per_user dictionary.

After sorting these dictionaries, store them in two different files: error_message.csv and user_statistics.csv.

Save the ticky_check.py file by clicking Ctrl-o, Enter key, and Ctrl-x.
........................
Visualize reports
First, give executable permission to the Python script ticky_check.py.

chmod +x ticky_check.py
Copied!
Run the ticky_check.py by using the following command:

./ticky_check.py
Copied!
Executing ticky_check.py will generate two report file __error_message.csv __and user_statistics.csv.

You can now visualize the __error_message.csv __and user_statistics.csv by converting them to HTML pages. To do this, pass the files one by one to the script csv_to _html.py file, like we did in the previous section.

To convert the error_message.csv into HTML file run the following command:

./csv_to_html.py error_message.csv /var/www/html/<html-filename>.html
Copied!
Replace <html-filename> with the name of your choice.

To convert user_statistics.csv into HTML file, run the following command:

./csv_to_html.py user_statistics.csv /var/www/html/<html-filename>.html
Copied!
Replace <html-filename> with the new name

Now, to view these HTML pages, open any web-browser and enter the following URL in the search bar.

[linux-instance-external-IP]/[html-filename].html

Output:

bb0dbd5305d1e78a.png

3d4041f646f56edb.png

Click Check my progress to verify the objective.
Generate two CSV report files and visualize data on the web

Congratulations!
"""
