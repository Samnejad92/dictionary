me={
    "name":"mohammad",
    "family":"ordookhani",
    "age":24,
    "email":"m.samnejad92@gmail.com"
}
isExists="name" in me
if "email" in me:
    print(me["email"])
else:
    print("Not found")

isNameExists="mohammad" in me.values()
print(isNameExists)