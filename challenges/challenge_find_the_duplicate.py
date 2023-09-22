def is_valid(nums, num):
    is_validations = (
        type(num) != int or
        len(nums) == 2 and nums[0] != nums[1] or
        num < 1
    )
    return is_validations


def find_duplicate(nums):
    if len(nums) < 2:
        return False
    nums.sort()
    for index, num in enumerate(nums):
        if is_valid(nums, num):
            return False
        if nums[index] == nums[index + 1]:
            return num


# print(find_duplicate([1, 3, 4, 2, 2]))
# print(find_duplicate([3, 1, 3, 4, 2]))
# print(find_duplicate([1, 1]))
# print(find_duplicate([1, 1, 2]))
# print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))
# print(find_duplicate([]))
# print(find_duplicate([1, 2]))
# print(find_duplicate(["a", "b"]))
# print(find_duplicate([-1, -1]))
# print(find_duplicate([1]))
