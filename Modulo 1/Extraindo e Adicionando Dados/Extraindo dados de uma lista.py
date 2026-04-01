colors = ["red", "green", "blue", "yellow", "purple"]
#by index
print(colors[0]) #red
print(colors[2]) #blue

#usando método slice

print(colors[:3]) #['red', 'green', 'blue']

#extraindo do ultimo elemento
print(colors[-3]) #purple

#slice for a range of elements
print(colors[1:4]) #['green', 'blue', 'yellow']

#utilizamos pop para extrair um elemento da lista e removê-lo
removed_color = colors.pop(2)
print(removed_color) #blue
print(colors) #['red', 'green', 'yellow', 'purple']

