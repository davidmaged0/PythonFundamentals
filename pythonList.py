## Change Item Values in a List
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
##print(len(thislist))
#thislist[1:3] = ["blackcurrant", "watermelon", "pear"]
#To add an item to the end of the list, use the append() method:
thislist.append("orange") 
#thislist.append("pineapple")
#To add an item at the specified index, use the insert() method:
thislist.insert(1, "orange") 
print(thislist)
##Extend List
thislist2 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist2.extend(tropical)
print(thislist2)
##
thislist = ["apple", "banana", "cherry"]
#thistuple = ("kiwi", "orange")
#thislist.extend(thistuple)
#print(thislist)
#print(type(thislist))
#To remove an item in a list, use the remove() method:
#thislist.remove("banana")
#print(thislist)
#The pop() method removes the specified index, (or the last item if index is not
#thislist.pop()
#thislist.pop(-1)
#del thislist[0:2]
thislist.clear()
print(thislist)