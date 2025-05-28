numbers = int(input("Enter a number to see its multiplication table: "))

for numbers in range(1, 10):
    for numbers in range(1, 10):
        product = numbers * numbers
        print(f"{numbers} X {numbers} = {product}")