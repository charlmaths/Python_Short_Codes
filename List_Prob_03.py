'''
Function that returns success elements of a string and finally returns nil when no more
so for example calling a function gen('simon') should run gen() 6 times and would return
s,i,m,o,n,nil
'''

# String variable
string_var = "simon"

def strgen(val):
    for i in range(len(val)):
        if i < len(val) - 1:
            print(val[i], end=", ")
        else:
            print(val[i], end=", ")
    print("nil", end="\n")

strgen(string_var)

