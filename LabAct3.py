#No.1

for i in range(6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

#No.2 

x = int(input("Input: "))

sum_of_numbers = 0

formula = ""
for i in range(1, x + 1):
    sum_of_numbers += i
    formula += str(i)
    if i < x:
        formula += " + "

print("Formula:", formula)
print("The summary from 1 to", x, "is:", sum_of_numbers)

#No.3

for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()