"""EX04 - List Utility Functions."""

__author__ = "730462735"


def all(nums: list[int], num: int) -> bool:
    if not nums:
        return False
    for n in nums:
        if n != num:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    max_num = input[0]
    for num in input:
        if num > max_num:
            max_num = num
    return max_num


def is_equal(list1: list[int], list2: list[int]) -> bool:
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True


def extend(list1: list[int], list2: list[int]) -> None:
    for num in list2:
        list1.append(num)


print(all([1, 2, 3], 1))  # false
print(all([1, 1, 1,], 2))  # false
print(all([1, 1, 1], 1))  # false

print(max([1, 3, 2]))
print(max([100, 99, 98]))

print(is_equal([1, 0, 1], [1, 0, 1]))
print(is_equal([1, 1, 0], [1, 0, 1]))

a: list[int] = [1, 3, 5]
b: list[int] = [2, 4, 6]
extend(a, b)
print(a)

c: list[int] = [7, 8]
extend(c, b)
print(c)