# myTuple = (6,7,8)
# myTupleString = ("Name", "Age")
# mixedTuple = (4,5.6, "name", (4,5))
# uniqueElementTuple = (45,)
#
# print(len(myTuple))
# print(myTuple[:2])
#
# x,y,z = myTuple
# print(x)

myDict = { "Axe": 24, "Sword": 45, "Dagger": 5, "Degree": "Games"}
print(myDict)
myDict["Grades"] = ["A", "B", "B+"]
myDict["Axe"] = 70
print(myDict)

for k,v in myDict.items():
    print(k,v)
