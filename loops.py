# print("---- Counting from 1 to 5 ----")

# متد اول
# for number in range(1, 6):
#     print(number)
    
# print("---- Countdown ----")

# count = 5
# while count > 0:
#     print(count)
#     count = count - 2

# print("Blast off!")

# print("---- Multiplication Table ----")

# number = int(input("Enter a number: "))

# for i in range(1, 11):
#     result = number * i
#     print(f"{number} × {i} = {result}")

print("---- Sum Calculator ----")

total = 0
count = int(input("How many numbers? "))

for i in range(count):
    number = int(input(f"Enter number {i+1}: "))
    total = total + number

print("Sum:", total)