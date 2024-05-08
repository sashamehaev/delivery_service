# Номер посылки 113735620
import sys
from array import array


def sort_weight(robots_array: array) -> array:
    last_index: int = len(robots_array) - 1
    swapped: bool = True
    while swapped:
        swapped = False
        for index in range(last_index):
            if robots_array[index] > robots_array[index + 1]:
                robots_array[index], robots_array[index + 1] = (
                    robots_array[index + 1], robots_array[index]
                )
                swapped = True
        last_index -= 1

    return robots_array


def distribute_by_platforms(robots_array: array, limit: int) -> int:
    count: int = 0
    left: int = 0
    right: int = len(robots_array) - 1
    while left <= right:
        if robots_array[left] + robots_array[right] <= limit:
            left += 1
            right -= 1
            count += 1
            continue
        else:
            right -= 1
        count += 1
    return count


def main() -> None:
    robots_input_list: list = sys.stdin.readline().rstrip().split()
    limit: int = int(sys.stdin.readline().rstrip())
    robots_input_list = [int(item) for item in robots_input_list]
    robots_array: array = array('b', robots_input_list)
    robots_array = sort_weight(robots_array)
    print(distribute_by_platforms(robots_array, limit))


if __name__ == '__main__':
    main()
