# print("---- Even or Odd? ----")

# یک عدد از کاربر بگیر 
# number = int(input("Enter a number: "))

# چک کن ببین زوج هست یا فرد
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
print("---- Grade Calculator ----") 

score = int(input("Enter your score (0-20): "))

if score >= 17:
    print("Grade A")
elif score >= 14:
    print("Grade B")
elif score >= 10:
    print("Grade C")
else:
    print("Fail")
