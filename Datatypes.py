'''#In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

x = 1    # int
y = 2.8  # float
z = 1j 

print(type(x))
print(type(y))
print(type(z))

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))