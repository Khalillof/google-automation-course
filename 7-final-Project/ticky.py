#!/usr/bin/env python3
import re


# To grep all the logs from ticky, use the following bash command:

# grep ticky syslog.log

# grep "ERROR" syslog.log


# To enlist all the ERROR messages of specific kind use the below syntax.

# Syntax: grep ERROR [message] [file-name]

# grep "ERROR Tried to add information to closed ticket" syslog.log



# Let's now write a few regular expressions using a python3 interpreter.

line = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"

#To match a string stored in line variable, we use the search() method by defining a pattern.

re.search(r"ticky: INFO: ([\w ]*) ", line)

#Output:
# <_sre.SRE_Match object; span=(29, 57), match='ticky: INFO: Created ticket '>

#You can also get the ERROR message as we did for the INFO log above from the ERROR log line.

line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
#To match a string stored in a line variable, we use the search() method by defining a pattern.

re.search(r"ticky: ERROR: ([\w ]*) ", line)

#Output:
#<_sre.SRE_Match object; span=(29, 65), match='ticky: ERROR: Error creating ticket '>

#Now that you know how to use regular expressions with Python, start fetching logs of ticky for a specific username. We'll need them in later sections.that you know how to use regular expressions with Python, start fetching logs of ticky for a specific username. We'll need them in later sections.

###################################################################################
# sorting

#Now, use the Python interactive shell to create a dictionary.

fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}

#Call the sorted function to sort the items in the dictionary.

sorted(fruit.items())
#Output:

[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

# We'll now sort the dictionary using the item's key. For this use the operator module.
#Pass the function itemgetter() as an argument to the sorted() function. Since the second element of tuple needs to be sorted, pass the argument 0 to the itemgetter function of the operator module.

import operator

sorted(fruit.items(), key=operator.itemgetter(0))

#Output:

[('apples', 5), ('bananas', 7), ('oranges', 3), ('pears', 2)]

#To sort a dictionary based on its values, pass the argument 1 to the itemgetter function of the operator module.

sorted(fruit.items(), key=operator.itemgetter(1))

#Output:

[('pears', 2), ('oranges', 3), ('apples', 5), ('bananas', 7)]

#Finally, you can also reverse the order of the sort using the reverse parameter. This parameter takes in a boolean argument.

#To sort the fruit object from most to least occurrence, we pass the argument reverse=True.

sorted(fruit.items(), key = operator.itemgetter(1), reverse=True)

#Output:

[('bananas', 7), ('apples', 5), ('oranges', 3), ('pears', 2)]

# You can see the fruit object is now sorted from the most to the least number of occurrences.
