#How to Create Lists in Python? There are a few different ways you can create lists in Python. 
#Using for Loops  in three steps:
  #1.Instantiate an empty list.
  #2. Loop over an iterable or range of elements.
  #3. Append each element to the end of the list.

squares = []
for i in range(5): 
    squares.append(i * i)
print(squares)

#Using List Comprehensions
#List comprehensions are a third way of making lists. 
#With this elegant approach, you could rewrite the for loop from the first example in just a single line of code:
squares2 = [j * j for j in range(5)] #new_list = [expression for member in iterable]..expression is the member itself, a call to a method, or any other valid expression 
print(squares2)

print("*****Another Example: to generate all combinations of lists [0,5] & [1,2,4] *****")
#using for lopp
list1 = []
for x in [0,5]: 
    for y in[1,2,4]:
      list1.append([x,y])
print(list1)
#Using List Comprehensions
new_list = [[x,y] for x in [0,5] for y in [1,2,4]]
print(new_list)





