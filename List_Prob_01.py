""" Potential interview questions: """

# Question: From a list of numbers, move '0' to the end of the list

lst = [1, 0, 3, 5, 6, 8]
print(lst)

new_list = lst
i = 0
while i < len(new_list):
    if new_list[i] == 0:
        new_list.remove(new_list[i])
        new_list.append(0)
    i = i + 1

print(new_list)



