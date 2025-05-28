numbers = int(input("Enter a number to see its multiplication table: "))

for X in range(1, 10):
    for Y in range(1, 10):
        product = X * Y
        print(f"{X} X {Y} = {product}")