def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def searchInsertPosition(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def findLeftBound(arr, target):
    left = 0
    right = len(arr) -1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            answer = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer

def findRightBound(arr, target):
    left = 0
    right = len(arr) -1
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            answer = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return answer

def searchRange(nums, target):
    left_bound = findLeftBound(nums, target)
    right_bound = findRightBound(nums, target)

    return [left_bound, right_bound]


import math

def minEatingSpeed(piles, h):
    left = 1
    right = max(piles)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / mid)
        if hours <= h:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

def shipWithinDays(weights, days):
    left = max(weights)
    right = sum(weights)
    answer = right

    while left <= right:
        mid = (left + right) // 2
        current_days = 1
        current_weight = 0

        for weight in weights:
            if current_weight + weight > mid:
                current_days += 1
                current_weight = weight
            else:
                current_weight += weight

        if current_days <= days:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer