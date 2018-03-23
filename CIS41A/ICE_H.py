"""
Gautam Mehta
ICE_H
"""
'''
Part 1
'''
d = {"apple":"sauce", "peach":"cobbler", "carrot":"cake", "strawberry": "sorbet", "banana":"cream pie"}
d["mango"]= "sticky rice"
d["strawberry"]="shortcake"
d.pop("carrot")
print ("e)")
print ("apple desert is:",d["apple"])
print ("f)")
if "cream pie" in d.values():
    print ("A banana desert exists.")
else:
    print ("A banana desert does not exist.")
print ("g)")
if "pear" not in d.values():
    print ("A pear desert does not exist.")
else:
    print ("A pear desert does exist.")
print ("h)")
for i in d.items():
    print (i[0], i[1])
print ("i)")
for i in sorted(d.items()):
    print (i[0], i[1])
"""
Execution Results:
e)
apple desert is: sauce
f)
A banana desert exists.
g)
A pear desert does not exist.
h)
apple sauce
peach cobbler
strawberry shortcake
banana cream pie
mango sticky rice
i)
apple sauce
banana cream pie
mango sticky rice
peach cobbler
strawberry shortcake
"""
print ("\n")
'''
Part 2
'''
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California"]
capitals = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento"]

zippeddict = dict(zip(states, capitals))
for i in sorted(zippeddict.items()):
    print (i[0],i[1])
"""
Execution Results:
Alabama Montgomery
Alaska Juneau
Arizona Phoenix
Arkansas Little Rock
California Sacramento
"""
'''
Part 3
'''
print ("\n")
states2= ["California", "Colorado", "Connecticut"]
capitols = ["Sac.", "Denver", "Hartford"]
x = dict(zip(states2, capitols))
zippeddict.update(x)
for i in sorted(zippeddict.items()):
    print (i[0],i[1])

"""
Execution Results:
Alabama Montgomery
Alaska Juneau
Arizona Phoenix
Arkansas Little Rock
California Sac.
Colorado Denver
Connecticut Hartford
"""