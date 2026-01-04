# List_String.py Simple code to demonstrate filtering strings from a mixed list

str_list = ["apple", "banana", 1, 2, 3, 4, "cherry", None, "date", 5.5, "fig"]

for s in str_list:
    if isinstance(s, str):
        print(f"String output: {s}")
    else:
        print(f"Non-string output: {s}")

# Testing Git