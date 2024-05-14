# Variables and Data Types
name = "Alice"
age = 30
height = 5.6
is_student = True

# Basic Operations
result = 10 + 5
difference = 20 - 8
product = 4 * 6
quotient = 15 / 3
remainder = 17 % 4
power = 2 ** 3

# Strings
message = "Hello, World!"
substring = message[7:12]
length = len(message)
uppercase = message.upper()
lowercase = message.lower()
concatenation = "Hello" + " " + "World"
formatted_string = "My name is {} and I am {} years old".format(name, age)

# Lists
numbers = [1, 2, 3, 4, 5]
first_item = numbers[0]
last_item = numbers[-1]
sliced_list = numbers[1:4]
numbers.append(6)
numbers.insert(2, 10)
numbers.remove(3)
numbers.pop()
numbers.sort()
numbers.reverse()

# Loops
for i in range(5):
    print(i)

for num in numbers:
    print(num)

while age < 40:
    age += 1

# Conditionals
if age < 18:
    print("You are a minor")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")

# Functions
def greet(name):
    print("Hello, " + name + "!")

greet("Bob")

def add(a, b):
    return a + b

result = add(4, 6)

# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

person1 = Person("Alice", 30)
person1.greet()

# File Handling
with open("example.txt", "w") as file:
    file.write("Hello, File!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
