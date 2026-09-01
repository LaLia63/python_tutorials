# dictionary = a collection of {key:value} pairs
#                    ordered and changeable. No duplicates

capitals = {
    "USA": "Washington DC",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow",
    "Myanmar": "Nay pyi daw",
    "Japan": "Tokyo",
    "Korea": "Seoul",
    "Spain": "Madrid"
}
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Myanmar")) # returns None if key not found

# if capitals.get("Japan"):
#     print(f"That is the capital.")
# else:
#     print("That is not a valid key")

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "D.C."})
# capitals.pop("China") # remove the key:value pair
# capitals.popitem() # remove the last inserted key:value pair
# capitals.clear() # remove all key:value pairs

print(capitals)

key = capitals.keys() # returns a list of all the keys
value = capitals.values() # returns a list of all the values

for key in capitals.keys():
    print(key)
print("------------------------")
for value in capitals.values():
    print(value)

capitals_list = capitals.items() # returns a list of tuples of all the key:value pairs
for key, value in capitals.items():
    print(f"{key} : {value}")
    