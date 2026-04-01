# LIST
nums = [1, 2, 3] # Ordered collection in square brackets
print(nums[0]) # Access first item using INDEX 0 

for n in nums: # ITERATE over list
  print(n) 

# DICTIONARY  
airports = {"SFO": "San Francisco", "LAX": "Los Angeles"} # Key-value pairs in {}
print(airports["SFO"]) # Use KEY to access VALUE

for code in airports: 
  print(airports[code]) # VALUE for each KEY
  
# TUPLE  
colors = ("red", "green", "blue") # Immutable ordered collection
print(colors[2]) 

# SET
unique_codes = {"SFO", "LAX", "SFO"} # Only 1 SFO 
print(len(unique_codes)) # Length is 2 (no duplicates)
unique_codes.pop() # Remove item (no index needed)

# MEMBERSHIP check with IN  
print("SFO" in airports) # True, has key

# METHOD to add items
unique_codes.add("ORD")