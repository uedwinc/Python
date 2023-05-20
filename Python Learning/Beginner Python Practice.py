
#Print the area of a circle given the radius

radius = float(input('Insert radius of circle\n >>> '))
pi = 3.142
area = pi * radius**2
print('You entered', radius, 'The area of the circle is', area)

#Convert temperature from Fahrenheit to Celcius

f = float(input('Enter temperature in Fahrenheit\n >>> '))
cel = (f - 32) * 5/9
print(f, 'Faherenheit is equal to', cel, 'Celcius')

#Obtain the sum of two integers

num_1 = int(input('Enter first value: '))
num_2 = int(input('Enter second value: '))
print('Sum of first and second values is', num_1 + num_2)

#OR

num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
print('The sum of ' + str(num_1) + ' and ' + str(num_2) + ' is ' + str(num_1 + num_2))

#Obtain the product of two integers

number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))
product = number_1*number_2
print('The product of', number_1, 'and', number_2, 'is', product)

# Bob, Ann, Jane and Ashwin want to order pizza - they know they will each eat
# 4 slices of pizza. The local pizza shop sells pizzas of only 6 slices
# What is the minimum number of pizzas needed - Use floor division

total_slices = 4 * 4
number_of_pizzas = (total_slices + 5)//6
slices_left = number_of_pizzas*6 - total_slices
print('Number of pizzas required is',number_of_pizzas,'there will be',slices_left,\
'remaining slices.')


# Write code that asks the user to input a number between 1 and 5 inclusive.
# The code will take the integer value and print out the string value. So for
# example if the user inputs 2 the code will print two. Reject any input that
# is not a number in that range

number = int(input('Enter a number between 1-5 >>> '))
if number >= 1 and number <= 5:
    print(str(number))
else:
    print('Not applicable')

# The above solution could not return the string value of the integer
    
# Better Solution

user_input = int(input('Please enter an integer between 1-5:> '))
if user_input == 1:
    print('one')
elif user_input == 2:
    print('two')
elif user_input == 3:
    print('three')
elif user_input == 4:
    print('four')
elif user_input == 5:
    print('five')
else:
    print('Out of range')


# Repeat the previous task but this time the user will input a string and the
# code will ouput the integer value. Convert the string to lowercase first.

user_input = str(input('Please enter a string between one to five:> '))
user_input = user_input.lower()
if user_input == 'one':
    print(1)
elif user_input == 'two':
    print(2)
elif user_input == 'three':
    print(3)
elif user_input == 'four':
    print(4)
elif user_input == 'five':
    print(5)
else:
    print('Out of range')
    

# Create a variable containing an integer between 1 and 10 inclusive. Ask the
# user to guess the number. If they guess too high or too low, tell them they
# have not won. Tell them they win if they guess the correct number.    
 
guess = int(input('Guess the number: >>> '))
if guess >= 1 and guess <= 10:
    print('You won')
else:
    print('Try again')
    
    
# A better solution would be:

secret_number = 3
guess = input('Guess the number between 1-10:> ')
if guess.isdigit():
    guess = int(guess)
    if guess == secret_number:
        print('You guessed the correct number! You win!')
    elif guess > secret_number and guess <= 10:
        print('You guessed too high. Sorry you lose!')
    elif guess < secret_number and guess >= 1:
        print('You guessed too low. Sorry you lose!')
    else:
        print('Out of range')
else:
    print('That\'s not even an integer! What are you playing at?!')


# Ask the user to input their name. Check the length of the name. If it is
# greater than 5 characters long, write a message telling them how many characters
# otherwise write a message saying the length of their name is a secret
    
user_name = str(input('Enter your name: '))
if len(user_name) > 5:
    print('Your name has', len(user_name), 'characters')
else:
    print('The number of characters in your name is a secret')
    
# Another solution would be:

name = input('Please enter your name:> ')
name_len = len(name)
if name_len > 5:
    print('Your name contains',name_len,'characters.')
else:
    print('I\'m not telling you the length of your name.')    
    

# Ask the user for two integers between 1 and 20. If they are both greater than
# 15 return their product. If only one is greater than 15 return their sum, if
# neither are greater than 15 return zero
    
integer_1 = int(input('Enter an integer between 1 and 20: '))
integer_2 = int(input('Enter another integer between 1 and 20: '))
if integer_1 > 15 and integer_2 > 15:
    print(integer_1 * integer_2)
elif integer_1 > 15 and integer_2 < 15:
    print(integer_1 + integer_2)
elif integer_1 < 15 and integer_2 > 15:
    print(integer_1 + integer_2)
else:
    print(0)

# Another Solution:

int_1 = int(input('Please enter an integer between 1-20:> '))
int_2 = int(input('Please enter another integer between 1-20:> '))

if int_1 > 15 and int_2 > 15:
    print(int_1 * int_2)
elif int_1 > 15 or int_2 > 15:
    print(int_1 + int_2)
else:
    print(0)


# Ask the user for two integers, then swap the contents of the variables. So if
# var_1 = 1 and var_2 = 2 initially, once the code has run var_1 should equal 2
# and var_2 should equal 1.

int_1 = int(input('Please enter an integer: '))
int_2 = int(input('Please enter another integer: '))
print('Before swapping first integer =',int_1,'and second integer =',int_2)
int_1,int_2 = int_2,int_1
print('After swapping first integer =', int_1,'and second integer = ',int_2)


# Loops and Lists

for i in range(10):
    print(i, end=' ')

for i in range(1,16):
    print(i, end=' ')

for i in range(0,101,4):
    print(i, end=' ')

for i in range(100,0,-1):
    print(i, end=' ')

word = 'python'

for i in word:
    print(i)


data = [53, 76, 25, 98, 56, 42, 69, 81]

data[:4]
data[1]

for num in data:
    print(num, end= ' ')

# Let's create a function to calculate the sum of the values in the data list

total = 0
for num in data:
    total = total + num
print('The sum of \'data\' is', total)

# However, python has a built-in sum function that should be used instead

total_2 = sum(data)
print('The sum of \'data\' is', total_2)

# Let's create a function to find the max of the data list

max_value = 0
for num in data:
    if num > max_value:
        max_value = num
print('The max value of the \'data\' list is', max_value)

# Remember, the above code could only work because all the values in the data list
# are positive. In the event that there are negative values, it won't work.

# Again, python has a built-in max function that should be used instead

max_v = max(data)
print('The max value is', max_v)

# We can use the range function to access the values in a list

my_list = [1,11,21,31,41,51]
for i in range(6):
    print(my_list[i])

# let's try manipulating the list

my_list = [1,11,21,31,41,51]
for i in range(5):
    print(my_list[i])
    print(my_list[i+1])
    print()

# Let's create a sort function using for loops and lists. 
# This process is called Bubble sort.

data_copy = data[:]
for i in range(len(data_copy)):
    for j in range(0,len(data_copy)-i-1):
        if data_copy[j] > data_copy[j+1]:
            data_copy[j],data_copy[j+1] = data_copy[j+1],data_copy[j]
print(data_copy)

# Bubble sort can be inefficient so it's better to use python's built-in sort function

sort = sorted(data)
print(sort)


new_list = [8,26,44]

new_list.append(90)
new_list

new_list.remove(8)
new_list

new_list.extend([19,20,88])
new_list

print(new_list.index(20))


# While Loops

# While for loops runs an operation a certain number of times,
# while loops runs an operation until certain conditions are met.

n = 10
while n > 0:
    print(n)
    n = n-1

# Another example:

user_input = int(input('Please enter ages of class member. \n Type -1 to end:> '))
ages = []
while user_input > 0:
    ages.append(user_input)
    user_input = int(input('The next age:> '))
print('The ages are',ages)


# We can also put a counter in a while loop

count = 0
class_names = []
name = input('Please enter name. \n Type n to stop:> ')
while name != 'n':
    count +=1
    class_names.append(name)
    print(f'{name} has been added.')
    name = input('Next name?:> ')  
print(f'There are {count} people in the class. They are {class_names}')


# Modulus

# Modulus gives you the remainder of a division.
# Example:

15 % 3
# This will return 0

9 % 4
# This returns 1


# We can use modulus to play a game of Fizzbuzz

n = 100
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i,'Fizzbuzz!!!')
    elif i % 5 == 0:
        print(i, 'Buzz')
    elif i % 3 == 0:
        print(i, 'Fizz')
    else:
        print(i)


# Remember, the order of conditionals is important - The code below will not work
# to give us fizzbuzz because the initial conditions are met first.

n = 100
for i in range(1,n+1):
    if i % 3 == 0:
        print(i,'Fizz')
    elif i % 5 == 0:
        print(i, 'Buzz')
    elif i % 3 == 0 and i % 5 == 0:
        print(i, 'Fizzbuzz!!')
    else:
        print(i)

# You can convert a range to a list:

print(list(range(10)))

print(list(range(0,20,4)))

print(type(range(10)))
    

# Ask the user for two numbers between 1 and 100. Then count from the
# lower number to the higher number. Print the results to the screen.

num_1 = int(input('Please enter a number between 1-100:> '))
num_2 = int(input('Please enter a number between 1-100:> '))

while num_1 < 0 or num_2 < 0 or num_1 > 100 or num_2 > 100 or num_1 == num_2:
    print('Numbers must be different values between 1 and 100. Try again')
    num_1 = int(input('Please enter a number between 1-100:> '))
    num_2 = int(input('Please enter a number between 1-100:> '))
    
if num_1 < num_2:
    for i in range(num_1,num_2+1):
        print(i,end=' ')
else:
    for i in range(num_2,num_1+1):
        print(i,end=' ')
    
    
# Ask the user to input a string and then print it out to the screen in
# reverse order (use a for loop).

word = str(input('Type in any word:> '))
reverse_string = ''
for char in word:
    reverse_string = char + reverse_string
print(reverse_string)

# There is another way to handle the above task:

word = str(input('Type in any word:> '))
print(word[::-1])


# Ask the user for a number between 1 and 12 and then display a times
# table for that number.

user_input = input('Please enter a number between 1 and 12:> ')

while (not user_input.isdigit()) or (int(user_input) < 1 or int(user_input) >12):
    print('Must be an integer between 1 and 12')
    user_input = input('Please enter valid number:> ' )
user_input = int(user_input)
print('===============================')
print()
print(f'This is the {user_input} times table')
print()
for i in range(1,13):
    print(f'{i} x {user_input} = {i*user_input}')


# Can you amend the solution to question above so that it just prints out all
# times tables between 1 and 12? (no  need to ask user for input)

for i in range(1,13):
    print('===============================')
    print()
    print(f'This is the {i} times table')
    print()
    for j in range(1,13):
        print(f'{j} x {i} = {j*i}')


# Ask the user to input a sequence of numbers. Then calculate the mean
# and print the result

user_input = input('Please enter any number. Type exit to stop:> ')
numbers = []
while user_input.lower() != 'exit':
    while not user_input.isdigit():
        print('That is not a number! Numbers only please:> ')
        user_input = input('Try again:> ')
    numbers.append(int(user_input))
    user_input = input('Please enter next number:> ')
total = 0
for number in numbers:
    total += number

print(f'Mean is {total/len(numbers)}')

# OR
 
print(sum(numbers)/len(numbers))


# Write code that will calculate 15 factorial. (factorial is product of
# positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)

n = 15
fact = 1
for i in range(1,n+1):
    fact = fact * i
    
print(fact)   

# Can you modify the code to ask user for input first?

n = int(input('Please enter any number:> '))
fact = 1
for i in range(1,n+1):
    fact = fact * i
print(fact)


# Write code to calculate Fibonacci numbers. Create list containing 
# first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
# two. Series starts 0 1 1 2 3 5 8 13 ....)

### Number of fib numbers required
n = 20

## Set a and b to the first two numbers in the sequence
a = 0
b = 1 

## List in which to store numbers
fib_nums = []

## Use a for loop to create the sequence, repeat n times
for i in range(n):
    fib_nums.append(a)
    a,b = b,a+b 
print(f'The first {n} Fibonacci numbers are, {fib_nums}')



#      *****
#      *
#      **** 
#      *
#      *
#      *
# Can you draw the above using python? (comment the solution code)

star = '*'

for i in range(1,7):
    for j in range(1,6):
        if i == 1 and j < 6:
            print(star,end='')
        elif i == 2 and j == 1:
            print()
            print(star)
        elif i == 3 and j < 5:
            print(star,end='')
        elif i == 4 and j == 1:
            print()
            print(star)  
        elif i == 5 and j == 1:
            print(star)
        elif i == 6 and j == 1:
            print(star) 
    

# Write some code that will determine all odd and even numbers
# between 1 and 100. Put the odds in a list named odd and the evens
# in a list named even.

# Numbers required
n = 100

# Instantiate empty lists
evens = []
odds = []

for i in range(n+1):
    if not i % 2:
        evens.append(i)
    else:
        odds.append(i)
print(f'The evens are {evens}')
print()
print(f'The odds are {odds}') 



































