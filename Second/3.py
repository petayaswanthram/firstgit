def display_multiples(number, count):
    print(f"The first {count} multiples of {number} are:")
    for i in range(1, count + 1):
        multiple = number * i
        print(f"{number} x {i} = {multiple}")
display_multiples(5, 10)