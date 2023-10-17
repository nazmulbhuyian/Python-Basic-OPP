list

1. List is an array.
List has only value
numbers = [5, 8, 3, 12, 6]    Numbers is a list.
we get numbers element with there index
number[0] = 5
number[1] = 8
number[2] = 3
number[3] = 12
number[4] = 6
we also gelement with reverse
number[-1] = 6
number[-2] = 12
number[-3] = 3
number[-4] = 8
number[-5] = 5

2. Dictonary
Dictonary is a key value pair
It has a key and a value
person = {'name': 'nazmul', 'age': 22}
here we get all item in person
print(person)
we also get a specific item like only name
print(person['name'])



args is a special syntax used in function definitions to allow a function to accept a variable number of positional arguments.

def sum(num1, num2, num3=0, num4):
    result = num1 + num2 + num3+ num4
    return result

total = sum(99, 11, 5)
here we got a error.because we dont provide num4 argumant. but arga solve this problem.

# args
def all_sum(num1, num2, *numbers):
    print(numbers)
    sum = 0
    for num in numbers:
        print(num)
        sum = sum + num
    return sum + num1 + num2

total = all_sum(45, 46, 89, 11, 81, 5, 2, 77)
print('all sum: ', total)
here we dont get any error. because we use there args.



kargs is a special syntax used in function definitions to allow a function to accept a variable number of keyword arguments. The term "kwargs" stands for "keyword arguments," and the double asterisks (**) before it indicate that it can accept multiple keyword arguments.


kargs can not take parameters in order(serial wise)

# def famous(**kargs)
def famous_name(first, last, **addition):
    name = f' {first} {last}'
    print(addition['title'])
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first='Taher', last='Ali', title="Hujur", title2="Shayokh", last2='taheri')
print(name)