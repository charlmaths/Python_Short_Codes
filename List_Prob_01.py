""" Potential interview questions: """

# Question: From a list of numbers, move '0' to the end of the list

lst = [1, 0, 3, 5, 6, 8]
print(lst)

for item in lst:
    if item == 0:
        lst.remove(item)
        lst.append(item)

print(lst)



