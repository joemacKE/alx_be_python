def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Error: Cannot Divide by zero.")
    except ValueError:
        print("Erro: Please enter numeric values only.")
    else:
        print(f"The result of the devision is: {result}")