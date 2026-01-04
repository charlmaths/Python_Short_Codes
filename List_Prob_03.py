'''
Function that returns success elements of a string and finally returns nil when no more
so for example calling a function gen('simon') should run gen() 6 times and would return
s,i,m,o,n,nil
'''

# String variable
string_var = "simon"

def strgen_1(val):
    for i in range(len(val)):
        if i < len(val) - 1:
            print(val[i], end=", ")
        else:
            print(val[i], end=", ")
    print("nil", end="\n")

strgen_1(string_var)

def strgen_2(val):
    for char in val:
        if val[char] == 0:
            print(val)
        elif char < len(val) - 1:
            print(val[char], end=", ")
        else:
            print(val[char], end=" ")
    print("nil", end="\n")

strgen_2(string_var)