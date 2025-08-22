# 1. Simple Function
def greet():
    print("Hello, Welcome to Python!")

greet()


# 2. Function with Parameters
def add(a, b):
    return a + b

print("Addition:", add(5, 3))


# 3. Function with Default Parameter
def introduce(name, age=18):
    print(f"My name is {name} and I am {age} years old.")

introduce("Vanshika", 20)
introduce("Riya")  # age default 18


# 4. Function with Return
def square(n):
    return n * n

print("Square of 4:", square(4))


# 5. Function Returning Multiple Values
def calc(a, b):
    return a+b, a-b, a*b

s, d, m = calc(10, 5)
print("Sum:", s, "Difference:", d, "Multiply:", m)


# 6. Variable Length Arguments (*args)
def total_sum(*numbers):
    return sum(numbers)

print("Total Sum:", total_sum(1,2,3,4,5))


# 7. Keyword Arguments (**kwargs)
def student_info(**details):
    for key, value in details.items():
        print(f"{key} : {value}")

student_info(Name="Vanshika", Age=20, Course="Python")


# 8. Lambda Function (short fu
