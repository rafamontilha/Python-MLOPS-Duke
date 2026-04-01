#assign variables
name = "Rafael"
last_name = "Montilha"

#no need to worry about the type of variable, python will understand it

height = 1,79
distance = 1,33
date = friday


#lack of checking can make things tricky, for example:  
height = "1,79"
height

# re-assigning variables
name = "Rafael" 
name = "Montilha"
name

#using print() with variables
print(name)

#create new variables from existing ones
#full_name = name + " " + last_name
full_name = None
full_name = f"{name} {last_name}"
full_name

#watch out for confusing variable!
name = "Rafael"
new_name = name
print(new_name)
name = "Alfredo"
print(new_name)
print(name)

#the print() function helps display values
#its adds separation when using commas
name = "Rafael"
print(name+" "+last_name, "is my name","and I am", height, "meters tall")