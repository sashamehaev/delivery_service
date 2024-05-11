# Номер посылки 113860882
import sys


def distribute_by_platforms(robots_array, limit: int) -> int:
    count: int = 0
    left: int = 0
    right: int = len(robots_array) - 1
    while left <= right:
        if robots_array[left] + robots_array[right] <= limit:
            left += 1
            right -= 1
            count += 1
            continue
        right -= 1
        count += 1
    return count


if __name__ == '__main__':
    robots_input_list: list = sys.stdin.readline().rstrip().split()
    limit: int = int(sys.stdin.readline().rstrip())
    robots_input_list = [int(item) for item in robots_input_list]
    robots_array: list = sorted(robots_input_list)
    print(distribute_by_platforms(robots_array, limit))
