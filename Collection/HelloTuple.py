# HelloTuple.py
# Basic tuple examples in Python

# Create tuples
fruits = ("apple", "banana", "cherry")
print("Tuple:", fruits)

single_item = ("apple",)
print("Single-item tuple:", single_item)

empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Access tuple items by index
print("First item:", fruits[0])
print("Last item:", fruits[-1])

# Tuple unpacking
first, second, third = fruits
print("Unpacked:", first, second, third)

# Tuples are immutable: this will raise an error if uncommented
# fruits[1] = "blueberry"

# Use tuple methods
print("Count of 'apple':", fruits.count("apple"))
print("Index of 'banana':", fruits.index("banana"))

# Nested tuple example
nested = ((1, 2), (3, 4))
print("Nested tuple:", nested)
print("Nested item:", nested[1][0])

# Convert list to tuple and tuple to list
fruit_list = ["kiwi", "mango"]
fruit_tuple = tuple(fruit_list)
print("Converted tuple:", fruit_tuple)
print("Converted back to list:", list(fruit_tuple))
