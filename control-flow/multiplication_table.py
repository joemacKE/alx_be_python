numbers = int(input("Enter a number to see its multiplication table: "))

for X in range(1, 11):
    for Y in range(1, 11):
        product = X * Y
        print(f"{X} X {Y} = {product}")