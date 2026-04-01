#Exceptions from python itself

14 / 0

#generatring an exception with your own code

raise RuntimeError("This is a problem!")

#Catching an Exception

try:
    #some intense operation that causes an error
    result = 14 / 0
except ZeroDivisionError:
    #do some other intense operation
    result = 14 / 2
print(result)

#don't get tempted to catch all exceptions

try:
    #some intense operation that causes an error
    result = 14 / 0
    raise RuntimeError("error! ")
except Exception:
    #do some other intense operation
    result = 14 / 2
print(result)

#catching multiple exceptions
try:
    #some intense operation that causes an error
    result = 14 / 0
    result + "100"
except (ZeroDivisionError, TypeError):
    result = 14 / 2
print(result)

#assign the resulting exception to a variable
try:
    #some intense operation that causes an error
    result = 14 / 0
    
except ZeroDivisionError as error:
    print(f"got an error --> {error}")
    result = 14 / 2
print(result)