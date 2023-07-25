""" Potential interview questions: """

# Question: Swap the values on the on the list, first item becomes the last item etc...

lst = [1, 2, 3, 4, 5, 6, 7]
print(lst)

for i in range(len(lst)//2):
    lst[i], lst[-1 -i] = lst[-1 -i], lst[i]
    print(lst)


#print(lst)