for x in thisdict:
  print(x)
  '''
Example
Print all values in the dictionary, one by one:'''

for x in thisdict:
  print(thisdict[x])
  '''
Example
You can also use the values() method to return values of a dictionary:'''

for x in thisdict.values():
  print(x)
  '''
Example
You can use the keys() method to return the keys of a dictionary:'''

for x in thisdict.keys():
  print(x)
  '''
Example
Loop through both keys and values, by using the items() method:
'''
for x, y in thisdict.items():
  print(x, y)