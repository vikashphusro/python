# HelloList.py
# Simple example showing common list operations in Python

fruits = ["apple", "banana", "cherry"]
print("Initial list:", fruits)

# Add items
fruits.append("dragonfruit")
print("After append:", fruits)

fruits.insert(1, "blueberry")
print("After insert at index 1:", fruits)

more_fruits = ["elderberry", "fig"]
fruits.extend(more_fruits)
print("After extend:", fruits)

# Delete items
fruits.remove("banana")  # remove by value
print("After remove banana:", fruits)

popped = fruits.pop()  # remove last item
print("After pop():", fruits)
print("Popped item:", popped)


