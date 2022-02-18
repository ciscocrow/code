

def load_numbers(stop_point):
    i = 0
    numbers = []
    print(f"Stop point is {stop_point}")
    for i in range(stop_point):
        print(f"At the Top i is {i}")
        numbers.append(i)

        print("numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    return numbers

numbers = load_numbers(6)

print("The numbers: ")

for num in numbers:
    print(num)
