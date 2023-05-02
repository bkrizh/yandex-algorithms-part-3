# id решения в Яндекс Контесте 86788955

def broken_search(nums, target) -> int:
    left, right = 0, len(nums) - 1
    return binary_search(nums, target, left, right)


def binary_search(nums, target, left, right) -> int:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif right <= left:
        return -1
    elif not nums[left] <= nums[mid]:
        if not nums[mid] < target <= nums[right]:
            return binary_search(nums, target, left, mid - 1)
        return binary_search(nums, target, mid + 1, right)
    elif not nums[left] <= target < nums[mid]:
        return binary_search(nums, target, mid + 1, right)
    return binary_search(nums, target, left, mid - 1)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
