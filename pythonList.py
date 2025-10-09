# join two lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
# for item in list2:
#     list1.append(item)
# list3 = list1 + list2
list1.extend(list2)
print(list1.count("a"))
print(list1.reverse())
print(list1)