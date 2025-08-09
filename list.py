#Creating an empty list
my_list = []

# Adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting the value 15 at the second position
my_list.insert(1, 15)

#Extending my list with another list
my_list.extend([50, 60, 70])

#Removing the last element from my list
my_list.pop()

#Sorting my list in ascending order
my_list.sort()

#Finding the index of the value 30 in my list
index_of_30 = my_list.index(30)
