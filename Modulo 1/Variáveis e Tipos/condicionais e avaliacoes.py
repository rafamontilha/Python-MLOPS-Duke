#all conditionals evaluete the result of the condition (expression)
condition = True
if condition:
    print("The condition was met")

#some data structures are truthy: false when empty, but true when they contain items

groceries=[]
if groceries:
    print("We have groceries!")

invites = ["Rafael", "Carol"]
if invites:
    print("We have invites!")

#other types like integers (0, and any positive integer) are also truthy
properties = 0
if properties:
    print("We have properties!")

parents = 2
if parents:
    print("We have parents!")

#operators are supported 
if properties ==0:
    print("no properties!") 

if parents > 1:
    print("We have more than one parent!")

#Else conditions

if properties:
    print("We have properties!")
else:
    print("No properties found!")

#elif useful when we want to add an else statement that needs to be mapped to a condition as well

if properties:
    print("We have properties!")
elif parents:
    print("We don't have any properties, but we have parents!")

#Negative Conditions

name = None

if not name:
    print("We don't have a name!")

#same is possible with elif conditions
name = "Rafael"
last_name = None

if not name:
    print("No name!")
elif not last_name:
    print("No last name either!")

#Compounding Conditions

has_kids = True
married = True

if has_kids and married:
    print("This person has kids and is married!")

#not can be used as well but can get harder to read

likes_books = False
is_logged_in = False

if not likes_books and not is_logged_in:
    print("This person doesn't like books and is not logged in!")