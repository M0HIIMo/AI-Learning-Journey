# print("---- My First Dictionary ----")

# student = {
#   "name": "Ali",
#   "age": 25,
#   "city": "Tehran",
#   "score": 18
# }

# print(student)
# print(student["city"])
# print(student["age"])
# print(student["name"])
# student["email"] = "ali@example.com"

# print(student)

# student["name"] = "Paya"

# for key in student:
#     print(f"{key}: {student[key]}")

# print(student)

print("---- Phone Book ----")

contacts = {
  "mom": "09354359534",
  "dad": "09191295169",
  "sister": "09966858006"
}

name = input("Who are you looking for? ")

if name in contacts:
    print(f"{name}'s number: {contacts[name]}")
else:
    print(f"{name} not found!")
    
new_name = input("Add new contact name: ")
new_number = input("Phone number: ")

contacts[new_name] = new_number

print("Updated contacts:", contacts)

print("\n---- All Contacts ----")
for name, number in contacts.items():
    print(f"{name}: {number}")