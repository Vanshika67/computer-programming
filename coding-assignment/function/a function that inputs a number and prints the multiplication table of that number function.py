'''Write a function that inputs a number and prints the multiplication table of that number¶'''
def mul(num):
    """
    Prints the multipliaction table of a given number
    """
    for i in range(1, 11):
        print("{multiplier} * {multiplicand} = {multiplicantion}".format(
            multiplier=num, multiplicand=i, multiplicantion=num * i))

mul(9)
