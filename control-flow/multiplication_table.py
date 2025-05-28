numbers = int(input("Enter a number to see its multiplication table: "))

for X in range(1, 11):
    product = numbers * X
    print(f"{numbers} * {X} = {product}")