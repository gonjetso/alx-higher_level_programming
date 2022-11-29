#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
print_message = "Last digit of %d is %d and is" % (number, last_digit)

if last_digit > 5:
    print(print_message, "greater than 5")
elif last_digit == 0:
    print(print_message, "0")
else:
    print(print_message, "less than 6 and not 0")
