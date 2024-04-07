def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    return sum(square(number) for number in range(1, 65))


print(total())

for palabra in range(7):
    print(palabra)    
