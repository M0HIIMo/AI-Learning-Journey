# print("---- My First List ----")

# scores = [20, 18, 15, 17, 19]

# scores.append(10)

# print(scores[5])
# print(scores[4])
# print(scores[3])
# print(scores[2])
# print(scores[1])
# print(scores[0])
# print(len(scores))

# print("---- Average Score ----")

# scores = [20, 18, 15, 17, 19, 10]

# total = 0
# for score in scores:
#     total = total + score
    
# count = len(scores)
# average = total / count

# print(f"Total: {total}")
# print(f"Count: {count}")
# print(f"Average: {average}")
# print(f"Highest: {max(scores)}")
# print(f"Lowest: {min(scores)}")

print("---- User's Numbers ----")

user_numbers = []
count = int(input("How many numbers?"))

for i in range(count):
    number = int(input(f"Enter number {i} "))
    user_numbers.append(number)
    
print("Your list:", user_numbers)
print("Sum:", sum(user_numbers))