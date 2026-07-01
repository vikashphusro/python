from collections import Counter
from collections import deque
from collections import namedtuple

queue = deque(["middle"])

# Fast append/pop on both sides
queue.append("right")
queue.appendleft("left")
print(queue) # Output: deque(['left', 'middle', 'right'])

queue.popleft() 
print(queue) # Output: deque(['middle', 'right'])


# Define the namedtuple structure
Point = namedtuple('Point', ['x', 'y'])

# Create an instance
pt = Point(10, 20)

# Access elements by name or index
print(pt.x)  # Output: 10
print(pt[1]) # Output: 20


words = ["apple", "banana", "apple", "cherry", "banana", "banana"]
word_counts = Counter(words)

print(word_counts) 
# Output: Counter({'banana': 3, 'apple': 2, 'cherry': 1})

# Find the most common items
print(word_counts.most_common(3)) 
# Output: [('banana', 3)]