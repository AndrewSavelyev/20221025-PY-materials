# The name check.
#
# Write a program that has a variable with your name stored (in lowercase) and then asks for your name as input. The program should check if your input is equal to
# the stored name even if the given name has another case, e.g., if your input is “Anton” and the stored name is “anton”, it should return True.
string = "andrew"


x = input("Enter your name: ")
ph = 0
for i in range(len(x)):
    if x[i] in string or string.capitalize():
        ph += 1
if ph == len(string):
    print("Name is correct")
else:
    print("Name is incorrect")
