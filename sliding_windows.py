def fixed_size_window(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        max_sum = max(max_sum, window_sum)

    return max_sum

def variable_size_window(nums, target):
    left = 0
    window_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

def lengthOfLongestSubstring(s):
    set_chars = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in set_chars:
            set_chars.remove(s[left])
            left += 1
        set_chars.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length

def length_of_longest_substring(s):
    left = 0
    chars = set()
    max_length = 0

    for right in range(len(s)):
        while s[right] in chars:
            chars.remove(s[left])
            left += 1

        chars.add(s[right])

        max_length = max(
            max_length,
            right - left + 1
        )

    return max_length

def characterReplacement(s, k):
    count = {}
    left = 0
    max_length = 0
    max_freq = 0

    for right in range(len(s)):
        if s[right] in count:
            count[s[right]] += 1
        else:
            count[s[right]] = 1

        max_freq = max(max_freq, count[s[right]])

        while right - left + 1 - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

def minSubArrayLen(target, nums):
    left = 0
    window_sum = 0
    min_length = float('inf')

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            min_length = min(min_length, right - left + 1)
            window_sum -= nums[left]
            left += 1
    return min_length if min_length != float('inf') else 0

def permutation_in_string(s1, s2):
    count_s1 = {}

    for char in s1:
        if char in count_s1:
            count_s1[char] += 1
        else:
            count_s1[char] = 1

    left = 0
    count_window = {}

    for right in range(len(s2)):
        char = s2[right]

        if char in count_window:
            count_window[char] += 1
        else:
            count_window[char] = 1

        if right - left + 1 > len(s1):
            count_window[s2[left]] -= 1

            if count_window[s2[left]] == 0:
                del count_window[s2[left]]

            left += 1

        if count_window == count_s1:
            return True

    return False
