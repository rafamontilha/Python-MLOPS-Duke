fruits = ['apple', 'orange']
fruits.append('banana') 
print(fruits) # ['apple', 'orange', 'banana']

fruits.insert(0, 'grapes')  
print(fruits) # ['grapes', 'apple', 'orange', 'banana']

veggies = ['carrots', 'celery']
fruits.extend(veggies)
print(fruits) # ['grapes', 'apple', 'orange', 'banana', 'carrots', 'celery'] 

removed = fruits.pop(2) 
print(removed) # orange
print(fruits) # ['grapes', 'apple', 'banana', 'carrots', 'celery']

dict = {'name': 'Mary'}
print(dict.get('age', 25)) # 25 (default used)