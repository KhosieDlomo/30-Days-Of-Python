#Day 10. ~ Loops
#Level 1
#1. iterating feom 0 to 10
'''for loop'''
for numb in range(11):
    print(numb)
iterate = 0
print()
while iterate <= 10:
    '''while loop'''
    print(iterate)
    iterate += 1
    
print()

#Iterating from 10 to 0 using for and while
for i in range(10, -1, -1):
    print(i)
print()

num = 10
while num >= 0:
    print(num)
    num -= 1
print()

#3. printing triangle
for i in range(7):
    print('#' * (i + 1))
print()

#4. nested loop
n = int(input('n: '))
for i in range(n):
    print('#' * n)
print()

#5. pattern
num = 10
for i in range(num + 1):
    count = i * i
    print(f'{i} x {i} = {count}')
print()

#6.iterating through a list
language = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for lst in language:
    print(lst)
print()

#7. iterating and printing even num
even = []
for i in range(101):
    if i % 2 == 0:
        even.append(i)
print(even)   
print()

#8. iterating and printing odd num
odd = []
for n in range(0,101):
    if n % 2 != 0:
        odd.append(n)
print(odd)
print()

#Level 2
#1. iterating from 0 to 100 n print the sum of all number
num = []
for j in range(101):
    num.append(j)
    add = sum(num)
print(f'The sum of all numbers is {add}.')
print()

#2.  iterating from 0 to 100 and printing seum of even and odd numbers
even_lst = []
odd_lst = []
for i in range(101):
    if i % 2 == 0:
        even_lst.append(i)
        even_num = sum(even_lst)
    else:
        odd_lst.append(i)
        odd_num = sum(odd_lst)
print(f'The sum of all evens is {even_num}. And the sum of all odds is {odd_num}.')

#level 3
#1. looping through the countries and extract all 
# import countries
# country_lst = []
# for country in countries:
#     if 'land' in country:
#         country_lst.append(country)
#     print(country_lst)
 
#2. reversing the orderr using loop
fruit_lst = ['banana', 'orange', 'mango', 'lemon']
for fruit in fruit_lst:
   sort_lst = sorted(fruit_lst, reverse=True)
print(sort_lst)

#3. 



