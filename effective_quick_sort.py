# id решения в Яндекс Контесте 86812464

import random


def quicksort(nums, fst, lst):
    if fst >= lst:
        return nums
    i, j = fst, lst
    pivot = nums[random.randint(fst, lst)]
    while i <= j:
        while nums[i] < pivot:
            i += 1
        while nums[j] > pivot:
            j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)


if __name__ == '__main__':
    part = []
    newpart = []
    n = int(input())
    for i in range(n):
        part = input().split()
        part = [-int(part[1]), int(part[2]), part[0]]
        newpart.append(part)
    quicksort(newpart, 0, len(newpart)-1)
    for el in newpart:
        print(el[2])
