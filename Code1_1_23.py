value1 = input("Enter the first value: ")
value2 = input("Enter the second value: ")
value3 = input("Enter the third value: ")

list1 =[value1, value2,value3]

# print every element in list1 using index
print(list1[0])
print(list1[1])
print(list1[2])

list1[2] = "Python"

# print list1
print(list1)
# add "Code is Life" to list1
list1.append("Code is Life")
# print list1
print(list1)

value4 = input("Enter the first value: ")
value5 = input("Enter the second value: ")
value6 = input("Enter the third value: ")

list2 = [value4, value5, value6]

# Extend list1 with the elements from list2
list1.extend(list2)
# print list1
print(list1)