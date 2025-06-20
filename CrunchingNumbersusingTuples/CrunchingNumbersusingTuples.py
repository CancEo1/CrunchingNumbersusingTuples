# Important for project 1 and 2
import random

def crunch_numbers(data):
    total = 0
    # Can be used to find words in a text document if you change number to # a string and data to a .txt file
    for number in data:
        total += number
    average = round(total / len(data))
    median_index = len(data) // 2
    median = data[median_index]
    minimum = min(data)
    maximum = max(data)
    dups = get_duplicates(data)

    print("Results: ",
         "Average: ", average,
         "Median: ", median,
         "Min: ", minimum,
         "Max: ", maximum,
         "Dups: ", dups)

def get_duplicates(data):
    dups = []
    for i in range(51):
        count = data.count(i)
        if count >= 2:
            dups.append(i)
    return dups

def main():
    fixed_tuple = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
    random_list = [0] * 11
    for i in range(len(random_list)):
        random_list[i] = random.randint(0, 50)
    random_list.sort()

    print("TUPLE DATA: ", fixed_tuple)
    crunch_numbers(fixed_tuple)
    print()
    print("RANDOM DATA:", random_list)
    crunch_numbers(random_list)

    # End of crunch_numbers function
if __name__ == "__main__":
    main()
