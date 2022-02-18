the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kindo f for-loop goes through a list
for number in the_count:
    print(f"This count {number}")

# Same as above
for fruit in fruits:
    print(f"A Fruit of type: {fruit}")

#We can also go through mixes lists
#Notice we have to use {} since we don't know whats in it
for i in change:
    print(f"I got {i}")

#we can also build lists, first start with an empty oranges
elements = []

#then use the range function to count 0 - 5
for i in range(10):
    print(f"adding {i} to the list.")
    #append is a function that lists understand
    elements.append(i)

#now print
for i in elements:
    print(f"Element was: {i}")
