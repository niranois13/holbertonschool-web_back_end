#!/usr/bin/python3
""" 0-main: Testing BasicCache """
BasicCache = __import__('0-basic_cache').BasicCache

# Initialize cache
my_cache = BasicCache()

# Test 1: Print empty cache
print("Test 1: Empty Cache")
my_cache.print_cache()
print("-" * 30)

# Test 2: Add basic key-value pairs
print("Test 2: Add key-value pairs (A, B, C)")
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print("-" * 30)

# Test 3: Retrieve existing keys
print("Test 3: Retrieve existing keys")
print(f"A: {my_cache.get('A')}")
print(f"B: {my_cache.get('B')}")
print(f"C: {my_cache.get('C')}")
print("-" * 30)

# Test 4: Retrieve non-existent key
print("Test 4: Retrieve non-existent key 'D'")
print(f"D: {my_cache.get('D')}")
print("-" * 30)

# Test 5: Add more keys, overwriting values
print("Test 5: Add more keys (D, E) and update A")
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")  # Update existing key 'A'
my_cache.print_cache()
print(f"A: {my_cache.get('A')}")
print("-" * 30)

# Test 6: Handle None inputs
print("Test 6: Handle None inputs")
my_cache.put(None, "Invalid")
my_cache.put("F", None)
print("Cache after None inputs:")
my_cache.print_cache()
print("-" * 30)

# Test 7: Handle overwriting existing keys with new values
print("Test 7: Overwriting existing keys")
my_cache.put("A", "Updated Street")
my_cache.put("B", "New World")
my_cache.print_cache()
print("-" * 30)

# Test 8: Handle special values
print("Test 8: Handle special values")
my_cache.put("G", "")
my_cache.put("H", 0)
my_cache.put("I", [])
my_cache.put("J", {})
my_cache.print_cache()
print(f"G (empty string): {my_cache.get('G')}")
print(f"H (zero): {my_cache.get('H')}")
print(f"I (empty list): {my_cache.get('I')}")
print(f"J (empty dict): {my_cache.get('J')}")
print("-" * 30)
