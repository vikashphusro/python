
############ LIST ####################################
# 1. Creating a list (allows duplicates and mixed types)
shopping_list = ["apple", "banana", "apple", "milk"]

# 2. Accessing items via 0-based indexing
print(shopping_list[1])  # Output: banana

# 3. Modifying an item in place
shopping_list[1] = "blackberry"

# 4. Adding and removing items
shopping_list.append("orange")  # Adds to the end
shopping_list.remove("apple")   # Removes the FIRST occurrence of "apple"

print("Final List:", shopping_list)
# Output: ['blackberry', 'apple', 'milk', 'orange']

###### Tuple ##############
# 1. Creating a tuple
geographic_coordinates = (40.7128, -74.0060)

# 2. Accessing items via indexing
print("Latitude:", geographic_coordinates[0])   # Output: 40.7128
print("Longitude:", geographic_coordinates[1])  # Output: -74.0060

# 3. Tuple Unpacking (a clean way to extract values)
lat, lon = geographic_coordinates
print(f"Unpacked: {lat}, {lon}")

# 4. Attempting to change a tuple will throw an error
# geographic_coordinates[0] = 34.0522  --> Raises TypeError


######## SET Example ###############
# 1. Creating a set (duplicates are automatically removed)
raw_user_ids = {101, 102, 103, 101, 102}
print("Unique IDs:", raw_user_ids)  # Output: {101, 102, 103}

# 2. Adding and removing items
raw_user_ids.add(104)
raw_user_ids.remove(102)

# 3. Mathematical Set Operations
admin_users = {101, 105}

# Intersection (Who is a user AND an admin?)
print("Common:", raw_user_ids.intersection(admin_users))  # Output: {101}

# Union (Combine all unique IDs from both sets)
print("All:", raw_user_ids.union(admin_users))  # Output: {101, 103, 104, 105}


##########Dictionary ############
# 1. Creating a dictionary (Key: Value pairs)
user_profile = {
    "username": "coder123",
    "email": "coder123@example.com",
    "login_count": 5
}

# 2. Accessing data using keys
print(user_profile["username"])  # Output: coder123

# 3. Modifying an existing value or adding a new key-value pair
user_profile["login_count"] = 6       # Updates existing key
user_profile["is_active"] = True       # Adds a brand new key

# 4. Safely accessing keys that might not exist using .get()
# If "theme" doesn't exist, it returns "dark" instead of crashing
current_theme = user_profile.get("theme", "dark") 

print("Updated Profile:", user_profile)