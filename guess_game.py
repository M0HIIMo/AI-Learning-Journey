print("---- Guess Game ----")

trying = 0
secrt_number = 9
number = int(input("Enter your guess: "))
while number != secrt_number:
      if number >= secrt_number:
         print("Lower")
      else:
         print("Higher") 
      trying = trying + 1
      number = int(input("Enter your guess: "))
      
print(f"Well Done! Your trying:  {trying + 1}") 