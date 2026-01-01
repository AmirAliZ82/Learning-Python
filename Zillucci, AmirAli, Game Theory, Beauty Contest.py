import random
import csv
import os

def generate_random_numbers():
    return [random.randint(0, 100) for _ in range(35)]

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

desktop_path = os.path.expanduser("~/Desktop")
file_path = os.path.join(desktop_path, "output.csv")

for _ in range(10):
    with open(file_path, mode='a', newline='') as file:
        writer = csv.writer(file)

        total_average = 0

        for i in range(100):
            random_numbers = generate_random_numbers()
            avg = calculate_average(random_numbers)
            writer.writerow([i+1, avg])
            total_average += avg

        total_average /= 100

        first_average = total_average
        file.write(f"The first average is {first_average}\n")
        print(f"The first average is {first_average}")

        iteration = 1
        while total_average > 0.001:
            total_average *= 2/3
            file.write(f"Iteration {iteration}: {total_average}\n")
            print(f"Iteration {iteration}: {total_average}")
            iteration += 1
