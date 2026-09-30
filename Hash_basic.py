def twoSum(num,target):
    seen = {}
    for i, n in enumerate(num):
        need = target - n
        if need in seen:
            return [seen[need], i]
        else:
            seen[n] = i
    return []

def containDuplicate(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

def isAnagram(s,t):
    count_s = {}
    count_t = {}
    for char in s:
        if char in count_s:
            count_s[char] += 1
        else:
            count_s[char] = 1
    for char in t:
        if char in count_t:
            count_t[char] += 1
        else:
            count_t[char] = 1
    return count_s == count_t

def canConstruct(ransomNote, magazine):
    count_magazine = {}
    for char in magazine:
        if char in count_magazine:
            count_magazine[char] += 1
        else:
            count_magazine[char] = 1
    for char in ransomNote:
        if char in count_magazine:
            count_magazine[char] -= 1
            if count_magazine[char] < 0:
                return False
        else:
            return False
    return True

