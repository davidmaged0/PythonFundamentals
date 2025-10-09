"""thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  """"""
   
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

i = 0
while i < len(thislist):
  print(thislist[i])
  i += 1
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
#newlist= thislist.copy()
#newlist = thislist[:]
newlist=list(thislist)
#newlist.append("orange")
#newlist.sort(reverse=True)
print(newlist)
#[print(x) for x in thislist]
