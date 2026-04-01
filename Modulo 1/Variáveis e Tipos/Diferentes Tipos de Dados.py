full_name = 'Rafael Montilha'

full_name = "Rafael Montilha"

full_name = """Rafael Montilha"""

summary = """ Triple quotes are useful when you have a ' or a " within a string"""

print(summary)

#use single quotes when you have double quotes in a string
summary = ' He said "Hello!" to me '
print(summary)
print("and use double quotes when you have single quote ' in a string")

#string support adding to other strings to compose text
first_name = "Rafael"
result = "Hello " + first_name
print(result)

#use f-strings to replace variables in a string
result = f"{first_name} is my name"
print(result)

#use type() to discover what type a variable is if you don't know
print(type(result))
type(15)

#integers support mathematical operations
14 / 2

#watchout for invalid operations
14 / "2"
14/0

#as with all other types, watch out when mixing unsupported types
14 + "6"

#types can change depending on operations

result = 3/2
print (result)
type(result)
