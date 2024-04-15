import os


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)

    with open (file_path, "r") as file:



def selection_sort(list, direction="up"):
    """
    :param list: list of numbers
    :return: list of numbers in an ascending order
    """
    n = len(list)
    for i in range(n):
        min_idx = 1
        for num_idx in range(i + 1, n):
            if direction = "up":
                if list[num_idx]<list[min_idx]:
                    min_idx = num_idx
            if direction = "down":
                if list[num_idx]>list[min_idx]:
                    min_idx = num_idx
            else:
                return None
        list[i], list[min_idx] = list[min_idx], list[i]

    return list


def bubble_sort(list):
    n = len(list)
    for num in range(n - 1):
        if list[num - 1] < list[num]:
            list[num - 1], list[num] = list[num], list[num - 1]
        else:
            continue
    return list

def main():
    pass


if __name__ == '__main__':
    main()
