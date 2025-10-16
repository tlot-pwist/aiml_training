print("dictionary example")
# employee=[
# {"id":"1", "name":"izam", "age":"44"},
# {"id":"2", "name":"man", "age":"83"},
# {"id":"3", "name":"bin", "age":"33"},
# {"id":"4", "name":"zaman", "age":"25"},
# ]
employee={"id":1,
"name":"izam",
"salary":6789.10}

# for k in kamus:
#     print(k["id"]+"->"+k["name"]+"->"+k["age"])

# print("employees details as follow: ")
# for key, value in employee.items():
#         print(key,":", value)

#     #adding key in dictionary
# employee["city"]="ketior"
# print("\ndictionary after adding city\n")

# for key, value in employee.items():
#         print(key,":",value)

# del employee["salary"]
# print("nemployee details after deleting salary\n")
# for key, value in employee.items():
#                 print(key,":", value)

print("all keys from employee")
for key in employee.keys():
    print(key)

print("\nall values from employee")
for value in employee.values():
    print(value)

print("\nkey: Value")
for key,value in employee.items():
    print(key,":",value)

print("\ndictionary as follow")
print(employee)

del employee["salary"]
print("\nafter deletion of salary")
for key,value in employee.items():
    print(key,":",value)