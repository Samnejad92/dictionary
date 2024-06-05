# dictionary={
#     key: value
# }
myDictionary={
    "name":"Item 1",
    "Count":3,
    "Price":2500
}
myShoppingCart=[{"name":"Python","price":"free"},{"name":"Kotlin","price":2500}]
myDictionary_2=dict(name="new Dictionaey",age=25)
print(myDictionary)
print("-------------------------------------------")
print(myDictionary_2)
print("-------------------------------------------")
print(myDictionary_2["name"])
print("-------------------------------------------")
me={
    "name":"Mohammad",
    "family":"Ordookhani",
    "age":24
}
print(me["name"])
print(me["family"])
print(me["age"])
print("-------------------------------------------")
for value in me.values():
    print(value)
print("-------------------------------------------")
for key in me.keys():
    print(key)
print("-------------------------------------------")
for key in me.keys():
    print(me[key])
print("-------------------------------------------")
for item in me.items():
    print(item)
print("-------------------------------------------")
for key,value in me.items():
    print(key,value)