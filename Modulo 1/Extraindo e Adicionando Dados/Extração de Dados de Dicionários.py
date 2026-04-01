#criando um dicionário de contatos
contact_information = {}

#exluindo um contato (e uma possivel exceção)

contact_information("height") #KeyError: 'height'

#para contornar vamos usar o método try-except
try:
    contact_information["height"]
except KeyError:
    print("6ft") #6ft

#outra forma de contornar o erro é usando o método get
result = contact_information.get("height")
print("height of contact information is", result) #height of contact informatios is None

#podemos definir um valor padrão caso a chave não exista
result = contact_information.get("height", "6ft")
print("height of contact information is", result) #height of contact informatios is 6ft

contact_information["age"] = 30
print("Age of contact information is", contact_information.pop("age"))
print(contact_information)