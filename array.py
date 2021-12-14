# append() :: to add element to the end of the list
arr = ["Javascript", "PHP", "Dart"]
print(arr)

# Finding the lenght of the array
print(len(arr))

# Adding an element to an array using appand()
arr.append("What is python?")
print(arr)

# extend() to extend all elements of a list to the another list
# insert() to insert an element at the another index
# remove() to remove an element from the list
# pop() to remove elements return element at the given index
colors = ["C1", "C2", "C3", "C4", "C5", "C6"]
# del colors[2]
# colors.remove("C4")
colors.pop(3)
print(colors)

# clear() to remove all elements from the list
# index() to return the index of the first matched element
fruits = ["Apple", "Banana", "Mango"]
fruits[1] = "Orange"
fruits[-1] = "Guava"
print(fruits)

# Concatenating two arrays using + operator
concat = [1, 2, 3]
concat = concat + [4, 5, 6]

print(concat)

# Repeating element in an array
repeat = ["a"]
print(repeat)

repeat = repeat * 5
print(repeat)

# count() to count of number of elements passed as an argument
# sort() to sort the elements in ascending order by default
# reverse() to reverse order element in a list
# copy() to return a copy of elements in a list

