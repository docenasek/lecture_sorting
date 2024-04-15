import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    iteration = 0
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for key, value in row.items():
                if iteration == 0:
                    data[key] = [int(value)]
                else:
                    data[key].append(int(value))
            iteration = iteration + 1
        return data



def selection_sort(list, direction="up"):
    """
    :param list: list of numbers
    :return: list of numbers in an ascending order
    """
    n = len(list)
    for i in range(n):
        min_idx = 1
        for num_idx in range(i + 1, n):
            if direction == "up":
                if list[num_idx] < list[min_idx]:
                    min_idx = num_idx
            if direction == "down":
                if list[num_idx] > list[min_idx]:
                    min_idx = num_idx
            else:
                return None
        list[i], list[min_idx] = list[min_idx], list[i]

    return list


def bubble_sort(list):
    n = len(list)
    for num in range(n - 1):
        for idx in range(n - num - 1):
            if list[idx] > list[idx + 1]:
                list[idx], list[idx + 1] = list[idx + 1], list[idx]
    return list

def insertion_sort()

def main():
    pass


if __name__ == '__main__':
    data = read_data("numbers.csv")
    list = data['series_1']
    print(bubble_sort(list))
    main()
