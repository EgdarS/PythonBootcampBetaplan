num1 = 42 #Data Types-Primitive-Numbers(int)
num2 = 2.3 #Data Types-Primitive-Numbers(float)
boolean = True #Data Types-Primitive-Boolean
string = 'Hello World' #Data Types-Primitive-Strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Data Types-Composite-List
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Data Types-Composite-Dictionary
fruit = ('blueberry', 'strawberry', 'banana') #Data Types-Composite-Tuples
print(type(fruit)) #Data Types-Composite-List-access value string
print(pizza_toppings[1]) #Data Types-Composite-List-access value
pizza_toppings.append('Mushrooms') #Data Types-Composite-List-add value
print(person['name']) #Data Types-Composite-Dictionary-access value
person['name'] = 'George' #Data Types-Composite-Dictionary-updates value
person['eye_color'] = 'blue' #Data Types-Composite-Dictionary-initialize
print(fruit[2]) #Data Types-Composite-Tuples-access value

if num1 > 45:
    print("It's greater") #conditional if
else:
    print("It's lower") #conditional else

if len(string) < 5:
    print("It's a short word!") #conditional if
elif len(string) > 15:
    print("It's a long word!") #conditional else if
else:
    print("Just right!") #conditional else 

for x in range(5): #for loop start
    print(x)
for x in range(2,5): #for loop start, stop
    print(x)
for x in range(2,10,3): #for loop start, stop, increment
    print(x) 
x = 0
while(x < 5): #while loop start
    print(x) #while loop stop
    x += 1 #while loop increment

pizza_toppings.pop() #Data Type-Composite-List-delete last value
pizza_toppings.pop(1) #Data Type-Composite-List-delete 2nd value 

print(person) #Data type-Comoposite-Dictionary-prints the entire person list
person.pop('eye_color') #Data Type-Composite-Dictionary-Delete eye_color value
print(person) #Data type-Composite-Dictionary-prints the entire person list without the eye_color value

for topping in pizza_toppings: 
    if topping == 'Pepperoni': #for loop sequence
        continue #for loop continue
    print('After 1st if statement')
    if topping == 'Olives': #for loop sequence
        break #for loop break

def print_hello_ten_times(): #function parameter
    for num in range(10): #function argument
        print('Hello') #function return

print_hello_ten_times()

def print_hello_x_times(x): #function parameter
    for num in range(x): #function argument
        print('Hello') #function return

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10): #function parameter 
    for num in range(x): #function argument
        print('Hello') #function return

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) #NameError: name <variable name> is not defined
# num3 = 72
# fruit[0] = 'cranberry' #TypeError: 'tuple' object does not support item assignment (tuples change value)
# print(person['favorite_team']) #KeyError: 'favorite_team'
# print(pizza_toppings[7])
#   print(boolean) #IndexError: list index out of range
# fruit.append('raspberry') #AttributeError: 'tuple' object has no attribute 'append' (tuples add value)
# fruit.pop(1) #AttributeError: 'tuple' object has no attribute 'pop' (tuples delete value)