firstDictionary = {
    "name": "John",
    "age": 30,
    "ID": 12345,
    "Balance": 1000.50,
    # "isActive": True,
}
print(firstDictionary)
# print(firstDictionary["name"])#print(firstDictionary.get("name"))
# print(firstDictionary.get("age"))
# print(len(firstDictionary))  # prints the number of key-value pairs
print(firstDictionary.keys())  # prints all keys
firstDictionary["isActive"] = True  # adding a new key-value pair
print(firstDictionary)
x = firstDictionary.items()
firstDictionary["age"] = 31  # updating an existing key-value pair
print(x)  # prints all key-value pairs
if "Balance" in firstDictionary:
    print("Balance is present in the dictionary")
firstDictionary.update({"age": 32, "city": "New York"})  # updating multiple key-value pairs
print(firstDictionary)