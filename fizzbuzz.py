number = int(input("1つの自然数をいれてね:"))

if number % 15 == 0:
    output = "FizzBuzz"
elif number % 3 == 0:
    Åoutput = "Fizz"
elif number % 5 == 0:
    output = "Buzz"
else:
    output = str(number)

print(output)
