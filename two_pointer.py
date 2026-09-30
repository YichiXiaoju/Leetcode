def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left<right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindrome_complex(s):
    left = 0
    right = len(s) - 1

    while left<right:
        while left<right and not s[left].isalnum():
            left += 1
        while left<right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

def twoSum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return [left + 1, right + 1]

    return []

def maxArea(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left<right:
        current_area = min(height[left], height[right]) * (right - left)
        if current_area > max_area:
            max_area = current_area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area

def threeSum(nums):
    nums.sort()
    result = []

    for i in range(len(nums) - 2):

        # 固定的数字去重
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1

            elif total > 0:
                right -= 1

            else:
                result.append([nums[i], nums[left], nums[right]])

                # left 去重
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # right 去重
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result

def TrappingRainWater(height):
    left = 0
    right = len(height)-1
    left_max = 0
    right_max = 0
    water = 0

    while left<right:
        left_max = max(height[left], left_max)
        right_max = max(height[right], right_max)

        if left_max<right_max:
            water +=left_max-height[left]
            left+=1
        else:
            water +=right_max-height[right]
            right-=1

        return water

