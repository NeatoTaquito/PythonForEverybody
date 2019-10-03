x=0
columns =int(input("Choose a number of columns between 1 and 10."))
while columns < 1 or columns > 10:
    print("Try again.")
    columns =int(input("Choose a number between 1 and 10."))
row =int(input("Choose number of rows from 1 to 7."))
while row < 1 or row > 7:
    print("Try again.")
    row =int(input("Choose number of rows from 1 to 7."))
for x in range(row):
    for x in range(columns):
        print("*",end=" ")
    print()
    
