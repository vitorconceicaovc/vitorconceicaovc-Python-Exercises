# number = 1
# multiple_of_3 = number / 3
# multiple_of_5 = number / 5

# while number <= 100:
    
#     if type(multiple_of_3) == "int":
#         print("Fizz")
#     elif type(multiple_of_5) == "int":
#         print("Buzz")
#     elif type(multiple_of_5) == "int" and type(multiple_of_3) == "int":
#         print("FizzBuzz")
#     else:
#         print(number)

#     number += 1
    
number = 1

while number <= 100:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    
    number += 1

    

