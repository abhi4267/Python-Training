'''nge Item Value
To change the value of a specific item, refer to the index number:

ExampleGet your own Python Server
Change the second item:'''

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
'''
Change a Range of Item Values
To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

Example
Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":'''

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
'''
If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

Example
Change the second value by replacing it with two new values:'''

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
'''
Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

Example
Change the second and third value by replacing it with one value:'''

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
'''

Insert Items
To insert a new list item, without replacing any of the existing values, we can use the insert() method.

The insert() method inserts an item at the specified index:

Example
Insert "watermelon" as the third item:'''

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)